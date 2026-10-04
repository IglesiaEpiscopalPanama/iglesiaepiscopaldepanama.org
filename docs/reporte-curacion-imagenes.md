# Reporte de curación institucional — 3 de octubre de 2026

Selección final ajustada para dar más presencia al clero en la home. Actualización exclusivamente de imágenes y documentación. Sin rediseño, cambios de copys, DNS, GitHub Pages ni CNAME. Selección revisada y aprobada para publicación por el usuario.

## Inventario y decisiones

| Carpeta | Inventariadas | Renombradas | Usar | Respaldo | No usar |
|---|---:|---:|---:|---:|---:|
| catedral-san-lucas | 16 | 16 | 1 | 10 | 5 |
| san-lucas-02 | 5 | 5 | 1 | 4 | 0 |
| liderazgo | 6 | 3 | 1 | 5 | 0 |
| vida-diocesana | 7 | 3 | 1 | 6 | 0 |
| **Total** | **34** | **27** | **4** | **25** | **5** |

La correspondencia completa anterior → actual, dimensiones, orientación, tamaño, procedencia probable, descripción, decisión y hashes de originales están en [inventario-imagenes.md](inventario-imagenes.md). Los siete nombres ya semánticos se mantienen, con su correspondencia histórica conservada. La oficialidad de las publicaciones sociales está confirmada por el usuario; la red concreta de cada archivo se registra como procedencia probable.

## Imágenes publicadas

- Hero desktop **y móvil**: `catedral-san-lucas/catedral-san-lucas-fachada-principal.jpg`, antes `IMG_20261003_072842.jpg`, original propio 4064 × 3048. Misma composición horizontal completa; no requiere otra toma móvil. Se conserva el concepto «Patrimonio y Catedral» y los pies de foto aprobados.
- Quiénes somos / About us: `san-lucas-02/catedral-san-lucas-interior-procesion.jpg`, antes `626723804_18556670092053081_6031592452908874287_n.jpg`. Sustituye la selección anterior interior-comunidad, conservada como respaldo.
- Servicio a la comunidad / Service to the community: imagen 1 `liderazgo/clero-diocesano-grupo-05.jpg`; imagen 2 `vida-diocesana/vida-diocesana-celebracion-02.jpg`. Se mantienen la galería existente y sus textos aprobados; el texto alternativo describe cada nueva fotografía.
- Liderazgo: se mantiene la sección textual. Mejor respaldo: `liderazgo/clero-diocesano-03.jpg`. El encuentro institucional de dos personas se conserva sin atribuir nombres ni roles individuales por apariencia.

Sin uso en la home y conservadas como respaldo: `liderazgo-encuentro-institucional.jpg`, `encuentro-comunitario-02.jpg` y `reunion-comunitaria-01.jpg`.

Los 25 respaldos se enumeran individualmente en el inventario. Los cinco excluidos del uso del sitio son las tomas propias antes terminadas en `072833`, `072921`, `072941`, `073047` y `073055`: respectivamente fachada-detalle, perspectiva-lateral-02, perspectiva-lateral-04, fachada-calle-vertical y fachada-jardin-vertical-03. Se conservan sus originales; son encuadres incompletos o variantes menos fuertes/redundantes.

Se respetan las cuatro fotografías web y la captura de liderazgo eliminadas antes de esta tarea. No se reintroducen. Se retiran también sus derivados obsoletos y los dos WebP de clero que ya no utiliza la galería.

## Optimización y archivos

Ajuste final: cuatro WebP preparados en `assets/img/web/`, calidad 86, sin ampliar ni recortar. Hero y celebración mantienen exactamente sus archivos anteriores:

- `catedral-san-lucas-interior-{640,1280}.webp`: regenerados desde interior-procesion, 640 × 362 y 1280 × 724.
- `clero-diocesano-grupo-05-{640,1280}.webp`: nuevos, 640 × 480 y 1280 × 960.
- Fachada: versiones existentes de 320/480/768/1280, intactas.
- Celebración: versiones existentes de 640/1280, intactas.

Dos sustituyen versiones existentes y dos son nuevos. Se mantienen las dos versiones de encuentro comunitario como respaldo sin uso en la home y el logo sin pérdida. Los originales renombrados conservan sus bytes y hashes. Hero con prioridad alta y `srcset`; imágenes posteriores con carga diferida; todas tienen dimensiones explícitas. La vista previa social de ambos idiomas apunta a la nueva fachada local con dimensiones actualizadas.

Archivos afectados por este ajuste: `index.html`, `en/index.html`, `README.md` (recuento WebP), `docs/inventario-imagenes.md`, este reporte, `docs/curate_images.py`, cuatro WebP y las evidencias actualizadas en `docs/verificacion-imagenes/`. No se modifican los originales ni el script de verificación. `assets/css/styles.css` y `assets/js/main.js` no cambian.

## Validación

Diez comprobaciones en Edge mediante Playwright: ambos idiomas en **1440, 768, 390, 360 y 320 px**. Sin desbordamiento horizontal, errores JavaScript, peticiones remotas de recursos ni respuestas 404 de los recursos de las páginas. Todas las imágenes cargan con dimensiones explícitas. Navegación móvil comprobada al abrir y cerrar con Escape. El servidor temporal devuelve 204 a la petición automática de favicon, puesto que el proyecto no incluye uno.

Revisión visual de capturas desktop y móvil, del resumen de los diez anchos y de la página completa: fachada y torre completas, encuadre sin recorte, ES y EN consistentes. Las imágenes respetan sus proporciones intrínsecas y reservan espacio durante la carga. Móvil usa 320 o 480 px a densidad 1×; 390 px a densidad 2× selecciona 768 px en lugar de 1280.

Comprobación adicional: recursos y enlaces locales existentes, anclas válidas, texto institucional y estructura HTML idénticos a HEAD (4751351), salvo los atributos de las dos imágenes sustituidas, 34 hashes de originales correctos, sin URLs localhost en las páginas y `git diff --check` correcto.

- [ES desktop completo](verificacion-imagenes/es-1440-completa.jpg)
- [ES móvil completo](verificacion-imagenes/es-390-completa.jpg)
- [EN desktop completo](verificacion-imagenes/en-1440-completa.jpg)
- [Resumen de diez vistas](verificacion-imagenes/responsive-resumen.jpg)
- [Resultados estructurados](verificacion-imagenes/responsive.json)

CNAME intacto, igualdad de bytes con el commit anterior verificada. SHA-256: `d0c8605bece886bb91e5359961cba003d12c4dd878666deeb3527e6063147da4`.

Base publicada: `4751351` — `feat: curate and update institutional imagery`. Commit de este ajuste: `feat: refine diocesan imagery on homepage`. Commit y push autorizados tras la validación final. Las capturas enlazadas se mantienen actualizadas como documentación previamente versionada; no se añaden nuevos artefactos temporales pesados.
