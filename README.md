# Iglesia Episcopal de Panamá

Sitio institucional de la Iglesia Episcopal de Panamá, Diócesis de Panamá.
Sitio de una sola página por idioma, realizado con HTML5, CSS3 y
JavaScript vanilla. No necesita compilación, paquetes ni backend.

Dominio oficial: https://iglesiaepiscopaldepanama.org/
Publicación mediante GitHub Pages. El dominio y la configuración de publicación
ya están establecidos; los cambios de contenido no requieren modificarlos.

## Estructura

```text
index.html             Página completa en español
en/index.html          Página completa en inglés
assets/css/styles.css  Estilos compartidos y diseño responsive
assets/js/main.js      Navegación móvil accesible
assets/img/            Originales institucionales y copias web optimizadas
docs/inventario-imagenes.md  Inventario, usos, dimensiones y hashes de imágenes
CNAME                  Dominio existente: conservar sin cambios
README.md              Guía del proyecto
```

## Edición y revisión

1. Edite `index.html` y `en/index.html` en paralelo para mantener ambos idiomas
   completos y consistentes. Las traducciones son estáticas; los nombres propios
   de congregaciones e instituciones educativas se conservan en español.
2. Los estilos están en `assets/css/styles.css`. Use las variables iniciales para
   ajustar la paleta y las fuentes del sistema, sin servicios externos.
3. Abra `index.html` directamente en un navegador; el sitio funciona también
   sin servidor y sin JavaScript. Para comprobar rutas equivalentes a GitHub
   Pages puede usar cualquier servidor estático local disponible.
4. Revise ambas páginas en móvil y escritorio, los enlaces ES/EN, la navegación
   por teclado, los enlaces de teléfono y correo, y `git diff --check`.
5. Confirme los cambios de contenido con la Diócesis antes de publicarlos.
   Revise `git status` y `git diff` antes de realizar un commit o push.

## Identidad y contenido

La presentación usa el logo oficial proporcionado por la institución, conservado
sin modificaciones en `assets/img/logo-iglesia-episcopal.png`. La copia WebP
del logo es sin pérdida y conserva exactamente sus píxeles. El diseño editorial
utiliza fotografías reales locales de patrimonio y vida comunitaria. No se
utilizan fotos de stock, imágenes generadas,
fuentes remotas ni formularios de contacto. No se ha creado un favicon derivado;
puede añadirse cuando la Diócesis proporcione un recurso adecuado para ese uso.

El contenido inicial se basa en los datos proporcionados por la institución.
Antes de publicar, confirme la vigencia del liderazgo episcopal y de la
representación legal, el directorio, los datos registrales y el contacto público.
El texto sobre misión y servicio es descriptivo, no una declaración oficial.
No se publican datos fiscales, bancarios, documentos de identidad ni contactos
personales. El contacto publicado corresponde a la Secretaría.

Conserve `CNAME` intacto. No es necesario cambiar DNS, GitHub Pages ni la
configuración del dominio para editar el sitio.

## Fotografías: originales y versiones web

```text
assets/img/
  logo-iglesia-episcopal.png       Logo original intacto
  iglesia-episcopal/
    catedral-san-lucas/           16 fotografías propias de fachada y patrimonio
    san-lucas-02/                5 fotografías institucionales del interior
    liderazgo/                   6 fotografías institucionales
    vida-diocesana/              7 fotografías de celebraciones y comunidad
  web/                          12 WebP fotográficos y 1 logo WebP sin pérdida
```

El inventario completo, la correspondencia entre nombres originales y finales,
los usos y los hashes SHA-256 están en `docs/inventario-imagenes.md`.
La captura antigua de liderazgo y las cuatro fotos web depuradas no se conservan. No se
identifican personas a partir de su apariencia ni se inventan fechas de fotografías.
La Catedral San Lucas se presenta como referencia patrimonial de la Diócesis;
los datos de contacto corresponden únicamente a la oficina diocesana.

Las fotografías del sitio usan `srcset` y `sizes`, dimensiones explícitas y
`decoding="async"`. El hero tiene prioridad alta; las imágenes posteriores usan
carga diferida. Se mantiene el encuadre completo, sin recortar personas.

Para añadir imágenes, conserve el original y genere copias web proporcionales
sin ampliar su resolución. No enlace imágenes remotas. La fachada propia actual
tiene 4064 × 3048 px y se publica en versiones de 320, 480, 768 y 1280 px.
La misma composición completa se usa en desktop y móvil. El usuario confirmó
el carácter institucional de las fotografías de las redes oficiales.

El sitio no requiere las herramientas usadas para preparar las imágenes;
las copias optimizadas ya están incluidas en el repositorio.

La curación puede reproducirse con `python docs/curate_images.py` (Pillow).
La verificación usa `node docs/verify_images.cjs` (Playwright y Edge), con
`PLAYWRIGHT_MODULE` si Playwright está instalado fuera del proyecto.
Resultados y capturas: `docs/verificacion-imagenes/`.
