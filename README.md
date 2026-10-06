# arieb-007.github.io

Personal research site, served by GitHub Pages from the `main` branch. Plain HTML and CSS, no build step.

| File | What it is |
| --- | --- |
| `index.html` | Home: research statement, questions, papers with figures, background |
| `publications.html` | Full publication list by year, with links and code, plus earlier projects |
| `reading.html` | Bookshelf |
| `style.css` | Shared styles, light and dark |
| `figures/*.png` | A detail cropped from each paper's main figure (from the papers' GitHub repos), used on the home page and as thumbnails on the publications page |
| `figures/dose.png` | For the ablation paper: a full-resolution redraw of its two-panel dose figure, rendered by `figures_src/dose_fig.py` (reference screenshot in `figures_src/dose_paper_figure.png`) |
| `figures_src/` | Sources for figures: the plotting script, and original full-size figures that the crops in `figures/` come from |
| `favicon.svg` | Site icon |

## Common edits

- **New paper:** add an `<li>` under the right year in `publications.html`. If it belongs on the home page, see the next-but-one item.
- **Replace or add a figure:** tiles are 16:10 with a white background and `object-fit: contain`, so export a crop at about 1200×750 (white background) into `figures/` and point the two `src` attributes at it (home page and publications page). The ablation paper's tile is made by `python3 figures_src/dose_fig.py` (run from the repo root); it redraws the paper's dose figure; to use the paper's own export instead, drop it in `figures/` and point the two `src` attributes at it.
- **New paper on the home page:** copy one `<li>` in the `.papers` list in `index.html`. The grid is 2 across, so keep the count even.
