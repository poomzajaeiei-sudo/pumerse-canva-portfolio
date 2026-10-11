# Pumerse Studio — Creator application portfolio

Ten original, commercially useful, single-page design samples created with Python, SVG, CairoSVG and Pillow. These designs were created outside Canva. No Canva API, paid services, stock photography, third-party templates or external logos were used. All illustrations, layouts and sample wordmarks are original vector compositions. Names, brands, contact details and commercial offers are fictional demonstration content. No application has been submitted and no Canva acceptance is implied.

## Files and page sizes

Every numbered SVG has a matching PNG in `png/`. Each file contains exactly one page; sample 04 is a cover only, not a multi-page carousel.

| # | Filename stem | Format | Layout direction |
|---|---|---|---|
| 01 | `01-minimalist-resume` | A4 portrait | Restrained two-column editorial resume |
| 02 | `02-creative-resume` | A4 portrait | Purple sidebar, serif headline, peach accents |
| 03 | `03-instagram-promotion` | 1080 × 1080 px | Lime campaign with original desk illustration |
| 04 | `04-carousel-cover` | 1080 × 1080 px | Cobalt educational cover with modular graphic cards |
| 05 | `05-coffee-poster` | A4 portrait | Warm serif-led poster with original coffee illustration |
| 06 | `06-wellness-poster` | A4 portrait | Botanical sage event poster |
| 07 | `07-business-pitch` | 1600 × 900 px, 16:9 | Dark pitch slide with opportunity panel |
| 08 | `08-educational-slide` | 1600 × 900 px, 16:9 | Three-card lesson with visual examples |
| 09 | `09-daily-planner` | A4 portrait | Writable priorities, time blocks and reflection |
| 10 | `10-service-price-list` | A4 portrait | Three service tiers and inquiry panel |

A4 SVGs explicitly declare **210 × 297 mm**. Their coordinate grids and PNG previews are 794 × 1123 pixels; preview pixels are rounded and are not print-resolution exports. For printing, open the SVG in free Inkscape and export a PDF at its physical A4 size, or a PNG at 300 dpi. Presentation files use an exact 16:9 canvas.

`contact-sheet.png` shows all ten samples. `index.html` is an offline browsing gallery. `validation.json` records XML parsing, text page-boundary checks and successful PNG rendering for each sample. `generate.py` reproduces all designs and exports.

## Open and edit locally

1. Open `index.html` in a web browser to browse all previews, then use its SVG links to view the vector originals. No server or account is needed.
2. Open `contact-sheet.png` in any image viewer for the overview.
3. Install the three included fonts from `fonts/` for consistent local display.
4. Open an SVG in **Inkscape**, a free, open-source vector editor. Use its Text tool to change text; ungroup if needed and select rectangles, lines and paths to change colors or geometry. Text remains real SVG text; it has not been flattened or converted to outlines. Save as SVG to retain editability.

## Import into Canva Free, when supported

Canva's upload support and feature availability can change. Canva import has **not** been tested through a Canva account. SVG upload, preservation of editable text, ungrouping and font handling are not guaranteed on Canva Free.

For **each numbered sample** in the table:

1. Create a new blank design matching its size: **A4 document**, **1080 × 1080 px**, or **1600 × 900 px**. Keep exactly one page.
2. In Uploads, choose Upload files and select the matching file from `svg/`.
3. If Canva accepts it, place it on the page and align it to the canvas edges. Check dimensions, line breaks and font substitution against the matching PNG.
4. Try the available text/ungroup controls. If the upload behaves like one graphic, it is not a native editable Canva layout. Keep the source SVG for free editing in Inkscape, or rebuild using the steps below.
5. If SVG upload or necessary editing controls are unavailable or marked Pro, skip them. Do not purchase an upgrade for this portfolio.

## Free alternative: rebuild with native Canva Free elements

1. Create the matching blank, single-page canvas. Upload its PNG and use it as a temporary visual reference. You can lower its transparency and lock it while rebuilding, or keep it open beside Canva.
2. Add native text boxes. Copy the exact sample wording from the SVG: open it in a text editor and read its `<text>` elements, or copy the text using Inkscape. Recreate headlines, subheads and body copy as separate boxes.
3. Choose commercially permitted fonts offered free in your Canva account. **DejaVu Sans** and **DejaVu Serif** are the original fonts; if unavailable, use free **Open Sans** and **Libre Baskerville** where offered. Font upload may require a paid feature; do not rely on it. Adjust widths and line breaks against the preview when substituting fonts.
4. Rebuild with free basic rectangles, circles, lines and custom-drawn shapes. Avoid template galleries, stock assets and elements carrying Pro indicators.
5. Use Position/alignment controls, consistent margins and the palette below. Delete the reference PNG after rebuilding. Confirm every visible part can be selected and edited and that the design still has only one page.
6. Compare at full-page and 100% views for cut-off text and crowded spacing. Export using an available free format.

### Rebuilding notes by sample

- **01:** Left section-label column; right experience column; green header rule. Keep body text left-aligned.
- **02:** Full-height purple sidebar; peach monogram circle and highlight card; serif name. Maintain separate contact and experience blocks.
- **03:** Lime background; green circle; rounded notebook, horizontal lines and angled pencil. Build the pencil from simple polygons and a circle rather than stock artwork.
- **04:** Cobalt background; three colored rounded cards with editable `Aa`, `01` and arrow text.
- **05:** Warm background; circle backdrop; cup silhouette, outlined handle and curved steam lines. Draw these shapes directly or trace them with the available free drawing tools.
- **06:** Two custom leaf silhouettes over a pale circle; date panel and three numbered activities.
- **07:** Dark background; lime opportunity panel; three process steps. Figures are illustrative targets, not verified business results.
- **08:** Three equal cards; size example, contrast callout and grouped-line spacing example.
- **09:** Priority panel; hourly rules, task checkboxes and two reflection fields. Leave the blank writing areas clear.
- **10:** Three aligned price rows; separators; green inquiry panel. Keep rates aligned at the right.

### Identity and palette

Shared identity: concise uppercase labels, restrained footer signature, generous spacing, and useful information first. Core colors: ink `#202E2B`, cream `#F6F3EA`, forest `#315C4C`, terracotta `#C45A38`. Additional palettes: purple `#3C3C73` / peach `#F0AD83`; lime `#DFFA74`; cobalt `#304EC8` / pale blue `#DDE8FF`; sage `#E8EFE5`. Exact colors and coordinates are editable in each SVG.

## Fonts, cost and usage

Bundled unmodified DejaVu Sans regular/bold and DejaVu Serif regular permit commercial use and redistribution under their included license; see `fonts/LICENSE.txt` for full terms and notices. The design assets use no raster images or externally fetched font resources. SVGs rely on the font family being installed; the PNG previews retain the intended rendering independently of installed fonts.

Original artwork and layouts in this portfolio may be used, edited and submitted by Pumerse Studio, including commercially. Bundled fonts retain their separate license. All work used free tools, with no purchases or service registrations.

## Regenerate

Use Python 3 with the free packages `CairoSVG` and `Pillow` and a system Cairo installation. From this directory:

```sh
python -m pip install CairoSVG==2.9.1 Pillow==12.3.0
python generate.py
```

The script expects the included fonts and creates/refreshes the SVGs, PNGs, contact sheet and validation report. Fontconfig must resolve DejaVu fonts for CairoSVG output (install the included fonts if your system lacks them). XML and text-boundary assertions fail rather than silently clipping content. The rendered contact sheet was also visually reviewed for hierarchy, alignment and spacing. Browser/Inkscape editing and Canva import were not interactively tested; SVG compatibility was checked through XML parsing and CairoSVG rendering.
