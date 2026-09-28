# assets

## zen-symbolic.png

Zen Browser ships its icon as white concentric rings on a near-black tile. Tinted
down to a single bar colour that renders as a dark box, and Qt cannot cut the
plate away at runtime, so the mark is pre-baked here instead: luminance lifted to
alpha, rings dilated so they carry the weight of the Nerd Font glyphs beside
them, and filled at the theme foreground's HSL lightness (the tint preserves
lightness, so a pure white silhouette would render brighter than the glyphs).

`ICON_OVERRIDES` in `Model.js` maps the `zen` window class to the icon-theme name
`zen-symbolic`, which is resolved through the widget's normal icon scan — so the
file has to be installed where that scan looks:

    cp assets/zen-symbolic.png ~/.local/share/icons/hicolor/128x128/apps/

Regenerate for a different theme (`L` = the foreground's HSL lightness, 0-255):

    magick ICON -colorspace gray -auto-level -level 25%,90% \
      -morphology Dilate Disk:3 mask.png
    magick -size 128x128 "xc:rgb(L,L,L)" mask.png \
      -alpha off -compose CopyOpacity -composite zen-symbolic.png

Derived from Zen Browser's own icon; see that project for its licensing.
