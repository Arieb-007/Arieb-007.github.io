# arieb-007.github.io

Personal research site, served by GitHub Pages from the `main` branch. Plain HTML and CSS, no build step.

| File | What it is |
| --- | --- |
| `index.html` | Home: research statement, questions, papers with figures, background |
| `publications.html` | Full publication list by year, with links and code, plus earlier projects |
| `reading.html` | Bookshelf |
| `style.css` | Shared styles, light and dark |
| `figures/*.svg` | One schematic per paper, used on the home page and as thumbnails on the publications page |
| `favicon.svg` | Site icon |

## Common edits

- **New paper:** add an `<li>` under the right year in `publications.html`. If it belongs on the home page, see the next-but-one item.
- **Replace a schematic with the real figure:** drop a PNG or SVG into `figures/` and change the two `src` attributes (home page and publications page). Figures sit in a 4:3 tile with `object-fit: contain`, so any aspect ratio works. The schematics are transparent and switch colours with dark mode; a PNG from the paper will keep its own white background, which is fine.
- **New paper on the home page:** copy one `<li>` in the `.papers` list in `index.html`. The grid is 3 across on desktop, so keep the count a multiple of 3 if you can.
