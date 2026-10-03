# Iglesia Episcopal de Panamá

Sitio institucional de la Iglesia Episcopal de Panamá, Diócesis de Panamá.
Primera versión de una sola página por idioma, realizada con HTML5, CSS3 y
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
assets/img/            Logo oficial e imágenes institucionales
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
sin modificaciones en `assets/img/logo-iglesia-episcopal.png`. El arco del hero es
un marco geométrico de CSS. No se utilizan fotos de stock, imágenes generadas,
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
