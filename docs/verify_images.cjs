// Run with the bundled Playwright runtime; the temporary server closes on exit.
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '..');
const out = path.join(__dirname, 'verificacion-imagenes');
const types = {'.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.webp':'image/webp', '.jpg':'image/jpeg'};
const server = http.createServer((req,res) => {
  const pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
  // Browsers request a favicon implicitly; the project has no supplied favicon.
  if (pathname === '/favicon.ico') { res.writeHead(204).end(); return; }
  const file = path.resolve(root, '.' + (pathname.endsWith('/') ? pathname+'index.html' : pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  fs.readFile(file,(error,data) => {
    res.writeHead(error ? 404 : 200, {'Content-Type':types[path.extname(file)] || 'application/octet-stream'});
    res.end(error ? 'Not found' : data);
  });
});
(async () => {
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({headless:true,channel:'msedge'});
  const results=[];
  try {
    for (const lang of ['es','en']) for (const width of [1440,768,390,360,320]) {
      const context=await browser.newContext({viewport:{width,height:1000},deviceScaleFactor:1});
      const page=await context.newPage();
      const errors=[]; const requests=[];
      page.on('pageerror',e=>errors.push(e.message));
      page.on('console',msg=>{if(msg.type()==='error') errors.push(msg.text());});
      page.on('response',r=>{if(r.status()>=400) errors.push(`${r.status()} ${r.url()}`);});
      page.on('requestfailed',r=>errors.push(`Failed ${r.url()}`));
      page.on('request',r=>requests.push(r.url()));
      await page.goto(base+(lang==='es' ? '/' : '/en/'),{waitUntil:'networkidle'});
      // Load every lazy image and detect overflow throughout the document.
      await page.evaluate(async()=>{
        document.documentElement.style.scrollBehavior='auto';
        for(const image of document.images) { image.loading='eager'; await image.decode(); }
      });
      await page.waitForLoadState('networkidle');
      const state=await page.evaluate(()=>({
        overflow:document.documentElement.scrollWidth>innerWidth,
        images:[...document.images].map(i=>({src:i.getAttribute('src'),currentSrc:new URL(i.currentSrc).pathname,width:i.naturalWidth,height:i.naturalHeight,renderedWidth:i.getBoundingClientRect().width,loaded:i.complete&&i.naturalWidth>0,dimensions:i.hasAttribute('width')&&i.hasAttribute('height')})),
        hero:{objectFit:getComputedStyle(document.querySelector('.hero-figure img')).objectFit,ratio:document.querySelector('.hero-figure img').getBoundingClientRect().width/document.querySelector('.hero-figure img').getBoundingClientRect().height}
      }));
      assert.equal(state.overflow,false,`${lang} ${width}: overflow`);
      assert.equal(errors.length,0,errors.join('\n'));
      assert.ok(state.images.every(i=>i.loaded&&i.dimensions));
      assert.ok(requests.every(u=>u.startsWith(base)), 'Remote image/resource request');
      assert.ok(Math.abs(state.hero.ratio-4/3)<.01,'Hero proportions');
      if(width<=760) {
        await page.locator('.menu-toggle').click();
        assert.equal(await page.locator('.menu-toggle').getAttribute('aria-expanded'),'true');
        await page.keyboard.press('Escape');
        assert.equal(await page.locator('.menu-toggle').getAttribute('aria-expanded'),'false');
      }
      await page.screenshot({path:path.join(out,`${lang}-${width}-hero.jpg`),type:'jpeg',quality:85});
      if((lang==='es'&&[1440,390].includes(width))||(lang==='en'&&width===1440))
        await page.screenshot({path:path.join(out,`${lang}-${width}-completa.jpg`),fullPage:true,type:'jpeg',quality:82});
      results.push({language:lang,viewport:width,...state,errors,remoteRequests:requests.filter(u=>!u.startsWith(base))});
      await context.close();
    }
    // Retina mobile must also choose a smaller resource than the 1280 desktop copy.
    const context=await browser.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true});
    const page=await context.newPage(); await page.goto(base,{waitUntil:'networkidle'});
    const retina=await page.locator('.hero-figure img').evaluate(i=>({resource:new URL(i.currentSrc).pathname,width:i.naturalWidth}));
    assert.ok(!retina.resource.includes('1280'),'Oversized retina mobile hero');
    fs.writeFileSync(path.join(out,'responsive.json'),JSON.stringify({results,retina},null,2)+'\n');
    console.log(JSON.stringify({viewports:results.length,errors:0,overflow:0,retina},null,2));
  } finally { await browser.close(); server.close(); }
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
