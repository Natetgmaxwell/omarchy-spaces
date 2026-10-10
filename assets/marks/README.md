# App marks

Source SVGs for `Marks.js`, the one-colour vector logos the `glyph` icon style
draws in the bar foreground colour.

- Brand marks: Simple Icons (CC0), `cdn.jsdelivr.net/npm/simple-icons@15.0.0/icons/<slug>.svg`
- `mdi-*`: Material Design Icons (Apache 2.0), `cdn.jsdelivr.net/npm/@mdi/svg@7.4.47/svg/<name>.svg`
  — used where a brand has no usable mark (Zoom's is a wordmark; Google Contacts,
  Hermes and OpenPods have none). Marked `padded: true` because of their 2px inset.
- `custom-gbrain.svg`: drawn after gbrain Atlas's hub-and-nodes logo.

To add an app: drop its single-path 24x24 SVG here, add an entry to `MARKS` in
`Marks.js` with the path run through `normalize.py` (Qt's PathSvg misreads the
minified arc flags Simple Icons ships, and draws garbage without it), then map
its window class, web app host and/or desktop entry name in `MARK_MATCH`
(Model.js). Matching is exact, never substring.
