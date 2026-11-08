# Concept drawings v0.2

Current review sources: `geometry.json`, `make_sketches.py`, and three SVG
sheets. These are provisional packaging drawings, not validated engineering
or manufacturing drawings. Read `../../docs/tech-pack.md` for stack-ups.

SVG, PNG and PDF exports have been regenerated from the current sketch
generator. Rerun drawing generation and raster/PDF export together after
future changes. Product design review does not authorize sharing.

## Regenerate / check

From repository root, Python3 standard library only:

```sh
python3 design/sketches/validate_geometry.py
python3 design/sketches/make_sketches.py
python3 design/sketches/validate_geometry.py --svg-dir design/sketches
# Optional isolated rendering, no writes beside generator:
python3 design/sketches/make_sketches.py --output-dir /tmp/heavy-bag-svg
```

For optional PNGs, install/use an SVG renderer such as CairoSVG:

```sh
for sheet in 1-laptop-bag 2-big-pack 3-weight-system; do
  cairosvg "design/sketches/$sheet.svg" -o "design/sketches/$sheet.png"
done
```

The existing `make_pdf.js` uses Playwright Chromium and regenerates both PNGs
and the combined PDF. In a disposable development environment with Node:

```sh
npm install --no-save --package-lock=false playwright
npx playwright install chromium
node design/sketches/make_pdf.js
```

The PNG-only CairoSVG step above is optional; it is unnecessary if using
Playwright. Do not add dependency-install artifacts to the product patch.
Review the resulting pages for clipping and scales before distribution; pixel
size is not a guarantee of A3 printing scale. The SVG sheets label individual
views with scales and mark symbolic handle/proposal details as not to scale.

The geometry check catches arithmetic/regression mistakes only; it cannot
validate strength, ergonomics, coating production, zip access or impact safety.
