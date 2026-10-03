// Enhance the mobile navigation; links remain available without JavaScript.
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#primary-navigation');
if (menuButton && navigation) {
  const mobile = window.matchMedia('(max-width: 760px)');
  const setOpen = (open) => {
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.hidden = mobile.matches && !open;
  };
  document.documentElement.classList.add('js');
  setOpen(false);
  menuButton.addEventListener('click', () => {
    setOpen(menuButton.getAttribute('aria-expanded') !== 'true');
  });
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      menuButton.focus();
    }
  });
  mobile.addEventListener('change', () => setOpen(false));
}
