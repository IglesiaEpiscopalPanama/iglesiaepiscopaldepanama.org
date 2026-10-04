"""Reproducible local image curation; originals retain their bytes."""
from pathlib import Path
from PIL import Image, ImageOps
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/img/iglesia-episcopal'
WEB = ROOT / 'assets/img/web'
entries = []

def register(folder, old, new, description, origin, decision='respaldo', use='Archivo editorial', reason='Alternativa para futuras actualizaciones'):
    source = BASE / folder / old
    target = BASE / folder / new
    if source != target and source.exists():
        assert not target.exists(), target
        source.rename(target)
    with Image.open(target) as im:
        width, height = ImageOps.exif_transpose(im).size
    entries.append(dict(folder=folder, original=old, name=new, width=width, height=height, bytes=target.stat().st_size,
                        description=description, origin=origin, decision=decision, use=use, reason=reason,
                        sha256=hashlib.sha256(target.read_bytes()).hexdigest()))

facades = [
('072833','fachada-detalle','Fachada cercana con columnas; extremo superior de la torre cortado','no usar'),
('072837','fachada-vertical','Torre y pórtico en encuadre vertical','respaldo'),
('072842','fachada-principal','Torre, pórtico, escalinatas y vegetación; fachada completa','usar'),
('072846','fachada-entorno','Catedral y entorno urbano con cruce peatonal en primer plano','respaldo'),
('072856','fachada-vertical-entorno','Fachada y torre con cielo y calle en formato vertical','respaldo'),
('072917','perspectiva-vertical','Pórtico y escalinatas en perspectiva vertical; torre oculta','respaldo'),
('072920','perspectiva-lateral-01','Pórtico, escalinatas y costado con árbol a la derecha','respaldo'),
('072921','perspectiva-lateral-02','Variante cercana del pórtico, escalinatas y costado','no usar'),
('072939','perspectiva-lateral-03','Vista oblicua del pórtico, jardín y muro lateral','respaldo'),
('072941','perspectiva-lateral-04','Variante de la vista oblicua del pórtico y jardín','no usar'),
('072958','perspectiva-frontal','Pórtico y puerta central desde abajo; torre fuera del encuadre','respaldo'),
('073009','cartel-historico','Cartel informativo sobre la Catedral San Lucas','respaldo'),
('073036','fachada-jardin-vertical-01','Catedral con torre, jardín y calle en encuadre vertical','respaldo'),
('073047','fachada-calle-vertical','Catedral distante con calle y cruce peatonal en primer plano','no usar'),
('073052','fachada-jardin-vertical-02','Variante vertical de la catedral y jardín','respaldo'),
('073055','fachada-jardin-vertical-03','Variante cercana de la catedral y jardín','no usar'),
]
for time, suffix, description, decision in facades:
    register('catedral-san-lucas',f'IMG_20261003_{time}.jpg',f'catedral-san-lucas-{suffix}.jpg',description,'fotografía propia del proyecto',decision,
             'Hero desktop y móvil; patrimonio' if decision == 'usar' else 'Patrimonio / detalle arquitectónico',
             'Fachada y torre completas; encuadre legible en todos los tamaños' if decision == 'usar' else ('Variante redundante o encuadre menos completo' if decision == 'no usar' else 'Alternativa patrimonial; no publicada'))

for old,new,description,origin,decision in [
('626449065_18556670014053081_5084294089189867489_n.jpg','interior-asamblea','Asistentes de pie en bancas, arcos y altar','Instagram oficial','respaldo'),
('626723804_18556670092053081_6031592452908874287_n.jpg','interior-procesion','Procesión entre las bancas hacia el altar','Instagram oficial','respaldo'),
('627015037_18556670722053081_8310266187939695882_n.jpg','interior-liturgia','Celebrantes alrededor del altar durante la liturgia','Instagram oficial','respaldo'),
('628136157_1308438154645589_8403246888726780219_n.jpg','interior-estandartes','Asistentes con estandartes entre las bancas','Facebook oficial','respaldo'),
('771892358_18614615908053081_8298882562867333621_n.jpg','interior-comunidad','Interior con arcos, luminarias, bancas y asistentes de pie','Instagram oficial','usar')]:
    register('san-lucas-02',old,f'catedral-san-lucas-{new}.jpg',description,origin,decision,'Quiénes somos / historia / presencia', 'Sustituye el interior web eliminado; muestra arquitectura y comunidad' if decision=='usar' else 'Alternativa de vida litúrgica')

for old,new,description,origin,reason in [
('631571735_1311892790966792_276013069756403984_n.jpg','clero-diocesano-grupo-04.jpg','Grupo amplio de clero con vestiduras en un recinto deportivo','Facebook oficial','Grupo institucional amplio; fondo deportivo menos sobrio'),
('631939145_1311894000966671_6856171340860385978_n.jpg','clero-diocesano-grupo-05.jpg','Grupo de clero en recinto deportivo; teléfono visible en primer plano','Facebook oficial','Respaldo documental; teléfono en primer plano'),
('680219048_18581680249053081_832038721497099236_n.jpg','liderazgo-encuentro-institucional.jpg','Dos personas, una con vestiduras litúrgicas, junto a una entrada','Instagram oficial','Material institucional validado por el usuario; no se vinculan personas a roles individuales sin identificación documental'),
('clero-diocesano-01.jpg','clero-diocesano-01.jpg','Grupo de clero con vestiduras frente a una fachada','Facebook oficial','Se conserva como alternativa; sustituido en la galería por vida diocesana'),
('clero-diocesano-02.jpg','clero-diocesano-02.jpg','Grupo con vestiduras frente a una fachada de piedra y placa','Instagram oficial','Alternativa de grupo; no atribuir lugar o evento'),
('clero-diocesano-03.jpg','clero-diocesano-03.jpg','Grupo con vestiduras, incluida mitra, junto a una entrada con rejas','Facebook oficial','Mejor respaldo visual de liderazgo por cercanía y contexto litúrgico; sección textual conservada')]:
    register('liderazgo',old,new,description,origin,'respaldo','Liderazgo / clero institucional',reason)

for old,new,description,origin,decision,reason in [
('808109881_1618323276671498_8252943004275149811_n.jpg','vida-diocesana-celebracion-01.jpg','Persona con mitra acompaña a asistentes durante una celebración','Facebook oficial','respaldo','Buen registro pastoral; escena más cerrada'),
('CLP-0928.jpg.jpeg','vida-diocesana-celebracion-02.jpg','Personas con vestiduras y asistentes en una procesión en recinto deportivo','archivo institucional','usar','Escena nítida de celebración y comunidad; sin interfaz social'),
('CLP-0930.jpg.jpeg','vida-diocesana-celebracion-03.jpg','Celebrante con vestiduras en un ambón junto a flores y banderas','archivo institucional','respaldo','Alternativa de celebración; menos representativa de comunidad'),
('celebracion-liturgica-01.jpg','celebracion-liturgica-01.jpg','Celebrante en ambón y asistentes en primer plano','Facebook oficial','respaldo','Alternativa de vida de fe'),
('encuentro-comunitario-01.jpg','encuentro-comunitario-01.jpg','Grupo reunido en sala con una persona de pie dirigiéndose al grupo','Facebook oficial','respaldo','Alternativa del encuentro'),
('encuentro-comunitario-02.jpg','encuentro-comunitario-02.jpg','Personas sentadas en círculo escuchan a una persona de pie','Instagram oficial','usar','Se mantiene la imagen actual: encuadre limpio y comunidad visible'),
('reunion-comunitaria-01.jpg','reunion-comunitaria-01.jpg','Personas sentadas alrededor de mesas en una sala','Facebook oficial','respaldo','Alternativa para formación y reuniones')]:
    register('vida-diocesana',old,new,description,origin,decision,'Vida diocesana / servicio / comunidad',reason)

copies=[]
for folder,name,stem,widths in [
('catedral-san-lucas','catedral-san-lucas-fachada-principal.jpg','catedral-san-lucas-fachada',[320,480,768,1280]),
('san-lucas-02','catedral-san-lucas-interior-comunidad.jpg','catedral-san-lucas-interior',[640,1280]),
('vida-diocesana','vida-diocesana-celebracion-02.jpg','vida-diocesana-celebracion',[640,1280])]:
    with Image.open(BASE/folder/name) as original:
        im=ImageOps.exif_transpose(original).convert('RGB')
        for width in widths:
            height=round(im.height*width/im.width)
            target=WEB/f'{stem}-{width}.webp'
            im.resize((width,height),Image.Resampling.LANCZOS).save(target,'WEBP',quality=86,method=6)
            copies.append(dict(name=target.relative_to(ROOT).as_posix(),width=width,height=height,bytes=target.stat().st_size,source=f'{folder}/{name}'))

# Retire derivatives of the removed web originals and the unused clergy image.
for name in ['catedral-san-lucas-interior-1080.webp','clero-diocesano-480.webp','clero-diocesano-960.webp']:
    (WEB/name).unlink(missing_ok=True)

for language,relative in [('es','index.html'),('en','en/index.html')]:
    p=ROOT/relative; html=p.read_text(encoding='utf-8'); prefix='../' if language=='en' else ''
    html=html.replace('assets/img/iglesia-episcopal/catedral-san-lucas/catedral-san-lucas-2-768x512.jpg','assets/img/web/catedral-san-lucas-fachada-1280.webp')
    html=html.replace('property="og:image:width" content="768"','property="og:image:width" content="1280"').replace('property="og:image:height" content="512"','property="og:image:height" content="960"')
    for match in list(re.finditer(r'<img\b[^>]+>',html)):
        tag=match.group()
        if 'catedral-san-lucas-fachada-' in tag:
            tag=re.sub(r'srcset="[^"]+"',f'srcset="'+', '.join(f'{prefix}assets/img/web/catedral-san-lucas-fachada-{w}.webp {w}w' for w in [320,480,768,1280])+'"',tag)
            tag=tag.replace('width="768" height="512"','width="1280" height="960"')
        elif 'catedral-san-lucas-interior-' in tag:
            tag=tag.replace('interior-1080','interior-1280').replace('1080w','1280w').replace('width="1080" height="811"','width="1280" height="960"')
        elif 'clero-diocesano-' in tag:
            tag=tag.replace('clero-diocesano-960','vida-diocesana-celebracion-1280').replace('clero-diocesano-480','vida-diocesana-celebracion-640').replace('480w','640w').replace('960w','1280w').replace('width="960" height="720"','width="1280" height="853"')
            tag=re.sub(r'alt="[^"]*"','alt="'+('Personas con vestiduras litúrgicas y asistentes durante una procesión' if language=='es' else 'People in liturgical vestments and attendees during a procession')+'"',tag)
        html=html.replace(match.group(),tag)
    p.write_text(html,encoding='utf-8',newline='\n')

lines=['# Inventario de imágenes institucionales — 3 de octubre de 2026','',
'34 originales revisados visualmente. Renombrados sin alterar sus bytes; dimensiones tras orientación EXIF. Tamaños en bytes. Ninguna imagen externa incorporada. Las procedencias sociales son **probables**, inferidas del patrón del nombre actual o del nombre histórico del inventario anterior; la oficialidad está confirmada por el usuario, pero no se dispone del enlace de cada publicación. No se identifican personas por apariencia.','',
'## Selección editorial','',
'- Hero desktop y móvil: `catedral-san-lucas/catedral-san-lucas-fachada-principal.jpg` (antes `IMG_20261003_072842.jpg`). Misma foto horizontal: torre y fachada completas, sin recortes; no hace falta una composición móvil diferente.','- Quiénes somos: `san-lucas-02/catedral-san-lucas-interior-comunidad.jpg`. Sustituye el interior web eliminado.','- Liderazgo: presentación textual conservada sin rediseño. Mejor respaldo: `liderazgo/clero-diocesano-03.jpg`. El encuentro de dos personas se conserva sin atribuir roles individuales no documentados.','- Comunidad: `vida-diocesana/encuentro-comunitario-02.jpg` y `vida-diocesana/vida-diocesana-celebracion-02.jpg`. Se conservan los pies de foto y copys aprobados.','- 4 usar, 25 respaldo, 5 no usar. «No usar» significa excluida del sitio, conservada en archivo; no se borran las fotos propias redundantes.','']
for folder in ['catedral-san-lucas','san-lucas-02','liderazgo','vida-diocesana']:
    items=[e for e in entries if e['folder']==folder]
    lines += [f'## {folder} — {len(items)} imágenes','',f'Carpeta: `assets/img/iglesia-episcopal/{folder}/`','',
              '| Nombre anterior → actual | Dimensiones | Orientación | Bytes | Descripción objetiva | Procedencia probable | Uso sugerido | Decisión / motivo |','|---|---|---|---:|---|---|---|---|']
    for e in items:
        orientation='horizontal' if e['width']>e['height'] else 'vertical'
        lines.append(f"| {e['original']} → **{e['name']}** | {e['width']} × {e['height']} | {orientation} | {e['bytes']} | {e['description']} | {e['origin']} | {e['use']} | **{e['decision']}**: {e['reason']} |")
    lines.append('')
lines += ['## WebP de publicación','', 'Calidad 86, Lanczos, sin ampliar ni recortar. Originales intactos. Hero: `srcset` de 320/480/768/1280 px; dimensión intrínseca 4:3, prioridad alta. Resto: carga diferida, dimensiones explícitas. Sin cambios de CSS ni layout.','', '| Archivo | Dimensiones | Bytes | Fuente |','|---|---|---:|---|']
for p in sorted(WEB.glob('*.webp')):
    with Image.open(p) as im: width,height=im.size
    source=next((c['source'] for c in copies if Path(c['name']).name==p.name),'vida-diocesana/encuentro-comunitario-02.jpg' if 'encuentro' in p.name else 'assets/img/logo-iglesia-episcopal.png (sin pérdida)')
    lines.append(f'| {p.relative_to(ROOT).as_posix()} | {width} × {height} | {p.stat().st_size} | {source} |')
lines += ['', '## Depuración previa respetada','', 'No se reintroducen `catedral-san-lucas-2-768x512.jpg`, `catedral-san-lucas-4.jpg`, `catedral-san-lucas-5.jpg`, `catedral-san-lucas-6.jpg` ni `liderazgo/referencia-liderazgo-01.png`, ya eliminados por el usuario. Las copias web antiguas de fachada e interior se sustituyen; la copia interior 1080 y las dos copias de clero sin uso se retiran. `og:image` apunta a la nueva fachada WebP local mediante el dominio institucional.','', '## Trazabilidad SHA-256 de originales','', '| Archivo anterior | Archivo actual | SHA-256 conservado |','|---|---|---|']
for e in entries: lines.append(f"| {e['folder']}/{e['original']} | {e['folder']}/{e['name']} | `{e['sha256']}` |")
prior=subprocess.check_output(['git','show','f95cc84:docs/inventario-imagenes.md'],cwd=ROOT).decode('utf-8')
lines += ['', '## Trazabilidad histórica conservada', '', 'Nombres anteriores a esta tarea de los siete archivos ya semánticos, del inventario `f95cc84`. Sus nombres actuales y bytes se mantienen.', '', '| Nombre histórico | Ruta actual |', '|---|---|']
for line in prior.splitlines():
    if line.startswith('| ') and '_n.jpg |' in line and any(f in line for f in ['liderazgo/','vida-diocesana/']):
        cells=[s.strip() for s in line.split('|')]
        lines.append(f'| {cells[1]} | {cells[2]} |')
(ROOT/'docs/inventario-imagenes.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(ROOT/'docs/verificacion-imagenes/curacion.json').write_text(json.dumps({'originals':entries,'generated':copies},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(entries)} inventariadas; {sum(e["original"]!=e["name"] for e in entries)} renombradas; {len(copies)} WebP generados')
