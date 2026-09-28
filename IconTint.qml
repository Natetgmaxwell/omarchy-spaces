import QtQuick
import Qt5Compat.GraphicalEffects

// The "theme" icon style's tint, kept in its own file so Spaces.qml does not
// import Qt5Compat at load time. qt6-5compat is not part of a default Omarchy
// install, and a top-level import would stop the entire widget from loading
// where it is absent rather than degrading one icon style. Reached through a
// Loader, so a missing module surfaces as Loader.Error and icons fall back to
// the monochrome path, which needs only QtQuick.Effects from core Qt.
//
// Colorize sets hue and saturation but leaves the source's lightness alone, so
// artwork keeps its internal contrast and alpha cutouts instead of collapsing
// into a flat silhouette.
Colorize {}
