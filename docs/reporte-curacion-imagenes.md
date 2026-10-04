# Reporte de curación institucional — 3 de octubre de 2026

Actualización exclusivamente de imágenes y documentación. Sin rediseño, cambios de copys, DNS, GitHub Pages ni CNAME. No push.

## Inventario y decisiones

| Carpeta | Inventariadas | Renombradas | Usar | Respaldo | No usar |
|---|---:|---:|---:|---:|---:|
| catedral-san-lucas | 16 | 16 | 1 | 10 | 5 |
| san-lucas-02 | 5 | 5 | 1 | 4 | 0 |
| liderazgo | 6 | 3 | 0 | 6 | 0 |
| vida-diocesana | 7 | 3 | 2 | 5 | 0 |
| **Total** | **34** | **27** | **4** | **25** | **5** |

La correspondencia completa anterior → actual, dimensiones, orientación, tamaño, procedencia probable, descripción, decisión y hashes de originales están en [inventario-imagenes.md](inventario-imagenes.md). Los siete nombres ya semánticos se mantienen, con su correspondencia histórica conservada. La oficialidad de las publicaciones sociales está confirmada por el usuario; la red concreta de cada archivo se registra como procedencia probable.

## Imágenes publicadas

- Hero desktop **y móvil**: `catedral-san-lucas/catedral-san-lucas-fachada-principal.jpg`, antes `IMG_20261003_072842.jpg`, original propio 4064 × 3048. Misma composición horizontal completa; no requiere otra toma móvil. Se conserva el concepto «Patrimonio y Catedral» y los pies de foto aprobados.
- Quiénes somos: `san-lucas-02/catedral-san-lucas-interior-comunidad.jpg`, antes `771892358_18614615908053081_8298882562867333621_n.jpg`. Interior actual con arquitectura y comunidad; sustituye la foto web eliminada.
- Comunidad: se mantiene `vida-diocesana/encuentro-comunitario-02.jpg` y se añade `vida-diocesana/vida-diocesana-celebracion-02.jpg`, antes `CLP-0928.jpg.jpeg`, en el espacio visual ya existente.
- Liderazgo: se mantiene la sección textual. Mejor respaldo: `liderazgo/clero-diocesano-03.jpg`. El encuentro institucional de dos personas se conserva sin atribuir nombres ni roles individuales por apariencia.

Los 25 respaldos se enumeran individualmente en el inventario. Los cinco excluidos del uso del sitio son las tomas propias antes terminadas en `072833`, `072921`, `072941`, `073047` y `073055`: respectivamente fachada-detalle, perspectiva-lateral-02, perspectiva-lateral-04, fachada-calle-vertical y fachada-jardin-vertical-03. Se conservan sus originales; son encuadres incompletos o variantes menos fuertes/redundantes.

Se respetan las cuatro fotografías web y la captura de liderazgo eliminadas antes de esta tarea. No se reintroducen. Se retiran también sus derivados obsoletos y los dos WebP de clero que ya no utiliza la galería.

## Optimización y archivos

Ocho WebP generados en `assets/img/web/`, calidad 86, sin ampliar ni recortar:

- `catedral-san-lucas-fachada-{320,480,768,1280}.webp`.
- `catedral-san-lucas-interior-{640,1280}.webp`.
- `vida-diocesana-celebracion-{640,1280}.webp`.

Tres sustituyen versiones existentes y cinco son nuevos. Se mantienen las dos versiones de encuentro comunitario y el logo sin pérdida. Los originales renombrados conservan sus bytes y hashes. Hero con prioridad alta y `srcset`; imágenes posteriores con carga diferida; todas tienen dimensiones explícitas. La vista previa social de ambos idiomas apunta a la nueva fachada local con dimensiones actualizadas.

Archivos afectados: `index.html`, `en/index.html`, `README.md`, `docs/inventario-imagenes.md`, imágenes originales y WebP. Se añaden este reporte, `docs/curate_images.py`, `docs/verify_images.cjs` y las evidencias en `docs/verificacion-imagenes/`. `assets/css/styles.css` y `assets/js/main.js` no cambian.

## Validación

Diez comprobaciones en Edge mediante Playwright: ambos idiomas en **1440, 768, 390, 360 y 320 px**. Sin desbordamiento horizontal, errores JavaScript, peticiones remotas de recursos ni respuestas 404 de los recursos de las páginas. Todas las imágenes cargan con dimensiones explícitas. Navegación móvil comprobada al abrir y cerrar con Escape. El servidor temporal devuelve 204 a la petición automática de favicon, puesto que el proyecto no incluye uno.

Revisión visual de capturas desktop y móvil, del resumen de los diez anchos y de la página completa: fachada y torre completas, encuadre sin recorte, ES y EN consistentes. Las imágenes respetan sus proporciones intrínsecas y reservan espacio durante la carga. Móvil usa 320 o 480 px a densidad 1×; 390 px a densidad 2× selecciona 768 px en lugar de 1280.

Comprobación adicional: recursos y enlaces locales existentes, anclas válidas, texto institucional idéntico al commit inicial, 34 hashes de originales correctos, sin URLs localhost en las páginas y `git diff --check` correcto.

- [ES desktop completo](verificacion-imagenes/es-1440-completa.jpg)
- [ES móvil completo](verificacion-imagenes/es-390-completa.jpg)
- [EN desktop completo](verificacion-imagenes/en-1440-completa.jpg)
- [Resumen de diez vistas](verificacion-imagenes/responsive-resumen.jpg)
- [Resultados estructurados](verificacion-imagenes/responsive.json)

CNAME intacto, igualdad de bytes con el commit anterior verificada. SHA-256: `d0c8605bece886bb91e5359961cba003d12c4dd878666deeb3527e6063147da4`.

Commit único solicitado: `feat: curate and update institutional imagery`. Su hash y el estado final se reportan al cerrar la tarea; no se hace push.
