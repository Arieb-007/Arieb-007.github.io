# arieb-007.github.io

Personal research site, served by GitHub Pages from the `main` branch. Plain HTML and CSS, no build step.

| File | What it is |
| --- | --- |
| `index.html` | Home: research statement, questions, papers with figures, background |
| `publications.html` | Full publication list by year, with links and code, plus earlier projects |
| `reading.html` | Bookshelf |
| `style.css` | Shared styles, light and dark |
| `figures/*.png` | A detail cropped from each paper's main figure (from the papers' GitHub repos), used on the home page and as thumbnails on the publications page |
| `figures/dose.svg` | Placeholder schematic for the ablation paper until its real figure is added |
| `figures_src/` | Drop original full-size figures here; crops in `figures/` are derived from them |
| `favicon.svg` | Site icon |

## Common edits

- **New paper:** add an `<li>` under the right year in `publications.html`. If it belongs on the home page, see the next-but-one item.
- **Replace or add a figure:** tiles are 16:10 with a white background and `object-fit: contain`, so export a crop at about 1200×750 (white background) into `figures/` and point the two `src` attributes at it (home page and publications page). The ablation paper still uses `figures/dose.svg`, a schematic; replace it with the paper's figure.
- **New paper on the home page:** copy one `<li>` in the `.papers` list in `index.html`. The grid is 2 across, so keep the count even.
