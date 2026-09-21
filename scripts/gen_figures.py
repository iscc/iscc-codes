"""Generate the ISCC brand figures under docs/images as self-contained SVG files.

Each figure is laid out in code following the ISCC identity (Edition 01): white field,
near-black text and connectors, thin rules, square corners, coral as the single emphasis
and the fixed ISCC-UNIT colours wherever a unit is named. Text is set in Readex Pro and
JetBrains Mono and converted to glyph outlines from the theme's WOFF2 files, so the SVGs
render identically as <img>, in the lightbox and in any converter without font loading.

Run from the repository root:

    uv run --group figures python scripts/gen_figures.py
"""

import re
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "zensical_iscc/assets/iscc/fonts"
ICONS = ROOT / "scripts/figures/icons"
OUTPUT = ROOT / "docs/images"

INK = "#212529"
PAPER = "#F8F9FA"
WHITE = "#FFFFFF"
CORAL = "#F56169"
MUTED = "#636B71"
RULE = "#D2D6D9"
UNIT_COLOURS = {
    "Meta-Code": ("#7AC2F7", INK),
    "Semantic-Code": ("#4596F5", INK),
    "Content-Code": ("#0054B2", WHITE),
    "Data-Code": ("#123663", WHITE),
    "Instance-Code": ("#A6DB50", INK),
}
FONT_FILES = {
    "light": "readex-pro-300.woff2",
    "regular": "readex-pro-400.woff2",
    "medium": "readex-pro-500.woff2",
    "mono": "jetbrains-mono-400.woff2",
}

# A genuine ISCC-CODE of an image, verified with iscc-core: it decomposes into the five
# units below. The four-unit code is composed from the same units without the Semantic-Code.
ISCC_CODE = "ISCC:KED572P4AOF5K6QXQA4T6OJD5UGX7UBPFW2TVQNTHBCKFRFCANCZARQ4K6NSFZQSH4GQ"
ISCC_CODE_FOUR_UNITS = "ISCC:KEC572P4AOF5K6QX2AXS3NJ2YGZTQRFCYSRAGRMQIYOFPGZC4YJD6DI"
UNITS = [
    ("Meta-Code", "AAA572P4AOF5K6QX", "metadata similarity"),
    ("Semantic-Code", "CEAYAOJ7HER62DL7", "meaning, reserved"),
    ("Content-Code", "EEA5ALZNWU5MDMZY", "content similarity"),
    ("Data-Code", "GAAUJIWEUIBULECG", "bitstream similarity"),
    ("Instance-Code", "IAARYV43ELTBEPYN", "exact checksum"),
]

_fonts = {}
_glyphs = {}


def font(key):
    """Load and cache one theme font by role key."""
    if key not in _fonts:
        _fonts[key] = TTFont(FONTS / FONT_FILES[key])
    return _fonts[key]


def glyph(key, character):
    """Return the outline path, advance width and em size of one character."""
    cache_key = (key, character)
    if cache_key not in _glyphs:
        face = font(key)
        name = face.getBestCmap().get(ord(character))
        if name is None:
            raise ValueError(f"{character!r} is not in the {key} font subset")
        glyph_set = face.getGlyphSet()
        pen = SVGPathPen(glyph_set)
        glyph_set[name].draw(pen)
        _glyphs[cache_key] = (pen.getCommands(), face["hmtx"][name][0], face["head"].unitsPerEm)
    return _glyphs[cache_key]


def text_width(value, size, key="regular", tracking=0):
    """Measure a text run in canvas units, including optional letter spacing in em."""
    width = sum(glyph(key, c)[1] * size / glyph(key, c)[2] for c in value)
    return width + tracking * size * max(len(value) - 1, 0)


def icon_markup(name, x, y, size, colour=INK):
    """Place a curated Carbon icon at a position, scaled uniformly from its 32 px grid."""
    source = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", source).group(1)
    desc = re.search(r"<desc>(.*?)</desc>", source).group(1)
    body = re.search(r'<g fill="#212529">(.*?)</g></svg>', source, re.S).group(1).replace("<defs />", "")
    return (
        f'<g transform="translate({x:g} {y:g}) scale({size / 32:.5f})" fill="{colour}">'
        f"<title>{title}</title><desc>{desc}</desc>{body}</g>"
    )


class Figure:
    """Accumulate SVG markup for one figure and write it with outlined text."""

    def __init__(self, width, height, title, desc):
        self.width, self.height, self.title, self.desc = width, height, title, desc
        self.defs = {}
        self.body = [f'<rect width="{width}" height="{height}" fill="{WHITE}"/>']

    def add(self, markup):
        """Append raw markup."""
        self.body.append(markup)

    def rect(self, x, y, w, h, fill=WHITE, stroke=INK, stroke_width=2):
        """Draw a square-cornered field, optionally without a stroke."""
        stroke_attrs = f' stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ""
        self.add(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"{stroke_attrs}/>')

    def line(self, x1, y1, x2, y2, stroke=RULE, width=1, dashed=False):
        """Draw a thin rule or connector segment."""
        dash = ' stroke-dasharray="7 6"' if dashed else ""
        self.add(f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{stroke}" stroke-width="{width}"{dash}/>')

    def arrow(self, points, dashed=False):
        """Draw an orthogonal route with one modest solid arrowhead at its end."""
        commands = " ".join(f'{"M" if i == 0 else "L"} {x:g} {y:g}' for i, (x, y) in enumerate(points))
        dash = ' stroke-dasharray="7 6"' if dashed else ""
        self.add(f'<path d="{commands}" fill="none" stroke="{INK}" stroke-width="2"{dash}/>')
        (px, py), (x, y) = points[-2], points[-1]
        length = abs(x - px) + abs(y - py)
        dx, dy = (x - px) / length, (y - py) / length
        left = (x - 8 * dx + 4 * dy, y - 8 * dy - 4 * dx)
        right = (x - 8 * dx - 4 * dy, y - 8 * dy + 4 * dx)
        self.add(f'<path d="M {x:g} {y:g} L {left[0]:g} {left[1]:g} L {right[0]:g} {right[1]:g} Z" fill="{INK}"/>')

    def text(self, x, y, value, size=20, key="regular", colour=INK, align="left", tracking=0):
        """Set a text run as glyph outlines; y is the baseline."""
        width = text_width(value, size, key, tracking)
        if align == "center":
            x -= width / 2
        elif align == "right":
            x -= width
        uses = []
        advance = 0.0
        for character in value:
            path, glyph_width, units = glyph(key, character)
            glyph_id = f"g-{key}-{ord(character)}"
            if path:
                self.defs.setdefault(glyph_id, f'<path id="{glyph_id}" d="{path}"/>')
                scale = size / units
                uses.append(
                    f'<use xlink:href="#{glyph_id}" transform="translate({x + advance:.2f} {y:.2f}) scale({scale:.6f} {-scale:.6f})"/>'
                )
            advance += glyph_width * size / units + tracking * size
        self.add(f'<g fill="{colour}" aria-label="{value.replace("&", "&amp;")}">{"".join(uses)}</g>')
        return width

    def icon(self, name, x, y, size=24, colour=INK):
        """Place a curated Carbon icon with its top-left corner at x, y."""
        self.add(icon_markup(name, x, y, size, colour))

    def save(self, path):
        """Write the SVG with an accessible title and description."""
        markup = (
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {self.width} {self.height}" width="{self.width}" height="{self.height}" '
            f'role="img" aria-labelledby="title desc">'
            f"<title id=\"title\">{self.title}</title><desc id=\"desc\">{self.desc}</desc>"
            f"<defs>{''.join(self.defs.values())}</defs>{''.join(self.body)}</svg>\n"
        )
        path.write_text(markup, encoding="utf-8", newline="\n")


def label_box(fig, x, y, w, h, title, subtitle=None, icon=None, fill=WHITE, colour=INK, sub_colour=MUTED):
    """Draw a node with a medium-weight title and a smaller muted subtitle.

    Without an icon the text is centred; with one, the icon sits at the left and the text
    is left-aligned beside it.
    """
    fig.rect(x, y, w, h, fill=fill)
    mid = y + h / 2
    if icon:
        fig.icon(icon, x + 22, mid - 14, 28, colour)
        tx, align = x + 66, "left"
    else:
        tx, align = x + w / 2, "center"
    if subtitle:
        fig.text(tx, mid - 3, title, 22, "medium", colour, align)
        fig.text(tx, mid + 21, subtitle, 16, "regular", sub_colour, align)
    else:
        fig.text(tx, mid + 8, title, 22, "medium", colour, align)


def bit_row(fig, x, y, cell, bits, fill=WHITE, colour=INK, size=24, key="mono"):
    """Draw a row of equal cells, one character per cell, as a single outlined field."""
    fig.rect(x, y, cell * len(bits), cell, fill=fill)
    for index, bit in enumerate(bits):
        if index:
            fig.line(x + index * cell, y + 1, x + index * cell, y + cell - 1, RULE, 1)
        fig.text(x + index * cell + cell / 2, y + cell / 2 + size * 0.36, bit, size, key, colour, "center")


def figure_iscc_code_units():
    """Figure 1: how an ISCC-CODE is composed of five ISCC-UNITs derived from the content."""
    fig = Figure(
        1200, 660, "ISCC-CODE structure",
        "Metadata, normalized content and raw bytes feed five ISCC-UNITs, from Meta-Code to "
        "Instance-Code, which combine into one ISCC-CODE.",
    )
    field_w, gap, x0 = 216, 8, 44
    centres = [x0 + i * (field_w + gap) + field_w / 2 for i in range(5)]
    right = x0 + 5 * field_w + 4 * gap

    # Axis from the abstract and persistent to the concrete and volatile.
    fig.text(x0, 46, "ABSTRACT & PERSISTENT", 13, "mono", MUTED, tracking=0.06)
    fig.text(right, 46, "CONCRETE & VOLATILE", 13, "mono", MUTED, "right", tracking=0.06)
    fig.line(x0, 58, right, 58, INK, 1)
    fig.line(x0, 52, x0, 58, INK, 1)
    fig.line(right, 52, right, 58, INK, 1)

    # Sources, aligned above the units they feed.
    sources = [
        (x0, field_w, "Metadata", "title and description", [centres[0]], [False]),
        (x0 + field_w + gap, 2 * field_w + gap, "Normalized content", "text, image, audio or video",
         [centres[1], centres[2]], [True, False]),
        (x0 + 3 * (field_w + gap), 2 * field_w + gap, "Raw bytes", "the encoded file",
         [centres[3], centres[4]], [False, False]),
    ]
    top, height = 82, 80
    for x, w, title, subtitle, targets, dashes in sources:
        label_box(fig, x, top, w, height, title, subtitle)
        for cx, dashed in zip(targets, dashes):
            fig.arrow([(cx, top + height), (cx, 222)], dashed)

    # The five ISCC-UNITs in their fixed colours, each with its genuine unit string.
    for (name, code, essence), cx in zip(UNITS, centres):
        colour, text_colour = UNIT_COLOURS[name]
        fig.rect(cx - field_w / 2, 222, field_w, 120, fill=colour, stroke=None)
        fig.text(cx, 290, code, 18, "mono", text_colour, "center")
        fig.text(cx, 378, name, 22, "medium", INK, "center")
        fig.text(cx, 404, essence, 16, "regular", MUTED, "center")

    # Collect the units into the composite ISCC-CODE.
    fig.line(centres[0], 432, centres[4], 432, INK, 1)
    for cx in centres:
        fig.line(cx, 424, cx, 432, INK, 1)
    fig.arrow([(600, 432), (600, 470)])
    fig.rect(x0, 470, right - x0, 60, fill=CORAL, stroke=None)
    label_w = fig.text(x0 + 24, 507, "ISCC-CODE", 20, "medium", INK)
    fig.text(x0 + 24 + label_w + 28, 507, ISCC_CODE, 17, "mono", INK)

    # Legend: what the colours and the dashed connector mean, in words.
    y, x = 588, x0
    for colour in ("#7AC2F7", "#4596F5", "#0054B2", "#123663"):
        fig.rect(x, y - 12, 14, 14, fill=colour, stroke=None)
        x += 18
    fig.text(x + 10, y, "Similarity-preserving, compared by Hamming distance", 16)
    x = x0 + 600
    fig.rect(x, y - 12, 14, 14, fill="#A6DB50", stroke=None)
    fig.text(x + 28, y, "Cryptographic checksum, exact match or none", 16)
    y = 618
    fig.line(x0, y - 5, x0 + 40, y - 5, INK, 2, dashed=True)
    fig.text(x0 + 52, y, "Reserved in ISO 24138:2024, not yet standardized", 16)
    return fig


def similarity_hash_rows():
    """Return the three input digests, their signed bit counts and the resulting digest."""
    inputs = ["0110100101101001", "0011110000011000", "1110010011100100"]
    counts = [sum(1 if row[i] == "1" else -1 for row in inputs) for i in range(16)]
    output = "".join("1" if count >= 0 else "0" for count in counts)
    return inputs, [f"{count:+d}" for count in counts], output


def figure_similarity_hash():
    """Figure 2: the similarity hash as a bitwise majority vote over equal-size digests."""
    fig = Figure(
        1200, 500, "Similarity hash",
        "Three input hash digests are combined bit by bit: each output bit is 1 where more "
        "inputs have that bit set than not, which keeps similar inputs close.",
    )
    inputs, counts, output = similarity_hash_rows()
    cell, x0 = 46, 44
    rows_right = x0 + 16 * cell
    label_x = rows_right + 64
    rows = [56, 128, 200]
    for y, bits in zip(rows, inputs):
        bit_row(fig, x0, y, cell, bits)
    # Bracket and label for the inputs.
    bx = rows_right + 22
    fig.line(bx, rows[0], bx, rows[-1] + cell, INK, 1)
    fig.line(bx - 8, rows[0], bx, rows[0], INK, 1)
    fig.line(bx - 8, rows[-1] + cell, bx, rows[-1] + cell, INK, 1)
    fig.line(bx, (rows[0] + rows[-1] + cell) / 2, bx + 8, (rows[0] + rows[-1] + cell) / 2, INK, 1)
    fig.text(label_x, 148, "Input hash digests", 22, "medium")
    fig.text(label_x, 174, "equal size, one per feature", 16, "regular", MUTED)

    fig.arrow([(x0 + 8 * cell, rows[-1] + cell), (x0 + 8 * cell, 300)])
    bit_row(fig, x0, 300, cell, counts, PAPER, INK, 20)
    fig.text(label_x, 328, "Bit counts", 22, "medium")
    fig.text(label_x, 354, "ones minus zeros per position", 16, "regular", MUTED)

    fig.arrow([(x0 + 8 * cell, 300 + cell), (x0 + 8 * cell, 410)])
    bit_row(fig, x0, 410, cell, output, CORAL)
    fig.text(label_x, 438, "Similarity hash digest", 22, "medium")
    fig.text(label_x, 464, "1 where the count is zero or positive", 16, "regular", MUTED)
    return fig


def figure_calculated_not_assigned():
    """Figure 3: independent parties calculate the same ISCC-CODE from the same file."""
    fig = Figure(
        1280, 660, "Calculated, not assigned",
        "An author, a publisher, a library and anyone else run the open ISO 24138 algorithm on "
        "the same file and each obtain the same ISCC-CODE, without registration or a central "
        "database.",
    )
    parties = ["Author", "Publisher", "Library", "Anyone"]
    x_party, x_calc, x_code, w_node, w_code = 44, 340, 636, 256, 600
    height = 88
    for index, party in enumerate(parties):
        y = 52 + index * 120
        mid = y + height / 2
        label_box(fig, x_party, y, w_node, height, party, "same file", icon="document")
        fig.arrow([(x_party + w_node, mid), (x_calc, mid)])
        label_box(fig, x_calc, y, w_node, height, "Calculate", "ISO 24138 algorithm", icon="generate-codes")
        fig.arrow([(x_calc + w_node, mid), (x_code, mid)])
        fig.rect(x_code, y, w_code, height)
        fig.text(x_code + w_code / 2, mid + 6, ISCC_CODE_FOUR_UNITS, 16, "mono", INK, "center")

    # The single emphasis: the point of the figure, in words.
    fig.rect(44, 548, 1192, 60, fill=CORAL, stroke=None)
    w = fig.text(68, 586, "Calculated, not assigned.", 24, "medium")
    fig.text(68 + w + 28, 586, "The same file gives the same code, wherever it is calculated.", 18)
    return fig


# Genuine codes computed with iscc-core for one image (visual-art.webp from the brand kit,
# saved as PNG) and a copy trimmed by 2 % on each side and saved as JPEG at quality 50.
# Each entry: unit name, verdict, and the 64-bit bodies of A and B as bit strings.
COMPARISON = [
    ("Content-Code", "6 of 64 bits differ: close",
     "1110101100001101100100001101000011001100011101110011010101101100",
     "1110101100001101100100001111000011001110000100110011110101101100"),
    ("Data-Code", "36 of 64 bits differ: far apart",
     "0100000011001100001100101110111011111110000000101100101001011000",
     "0110011111010000000101100010000100100101110101100111010011110011"),
    ("Instance-Code", "no exact match",
     "0011001010110011011010000001010101010100110010001000110100110010",
     "1000101101101010000001010111101110101001100010101110100010101101"),
]


def figure_similarity_comparison():
    """Figure 4: comparing the units of an image and a cropped, re-compressed copy bit by bit."""
    fig = Figure(
        1200, 620, "Comparing ISCC-UNITs",
        "An original image and a cropped, re-compressed copy: their Content-Codes differ in 6 of "
        "64 bits and are close, their Data-Codes differ in 36 bits, and their Instance-Codes "
        "have no exact match.",
    )
    x0, right = 44, 1156
    # The two files being compared.
    for x, letter, title, subtitle in [
        (x0, "A", "Original image", "PNG, 1.5 MB"),
        (620, "B", "Cropped copy", "2 % trimmed each side, JPEG quality 50, 108 KB"),
    ]:
        fig.rect(x, 44, 536, 72)
        fig.text(x + 22, 89, letter, 24, "mono")
        fig.text(x + 62, 77, title, 22, "medium")
        fig.text(x + 62, 101, subtitle, 16, "regular", MUTED)

    cell, cells_x = 16.5, 100
    for index, (name, verdict, bits_a, bits_b) in enumerate(COMPARISON):
        y = 150 + index * 140
        colour = UNIT_COLOURS[name][0]
        fig.rect(x0, y - 12, 14, 14, fill=colour, stroke=None)
        fig.text(x0 + 24, y, name, 20, "medium")
        fig.text(right, y, verdict, 18, "regular", INK, "right")
        rows = [(y + 18, "A", bits_a), (y + 48, "B", bits_b)]
        for position, (a, b) in enumerate(zip(bits_a, bits_b)):
            if a != b:
                fig.rect(cells_x + position * cell, y + 14, cell, 60, fill=CORAL, stroke=None)
        for row_y, letter, bits in rows:
            fig.text(x0 + 16, row_y + 17, letter, 14, "mono", MUTED)
            fig.rect(cells_x, row_y, 64 * cell, 22, fill="none", stroke=RULE, stroke_width=1)
            for position, bit in enumerate(bits):
                if bit == "1":
                    fig.rect(cells_x + position * cell + 1.5, row_y + 1.5, cell - 3, 19, fill=INK, stroke=None)

    # Legend, in words.
    y, x = 590, x0
    fig.rect(x, y - 12, 14, 14, fill=INK, stroke=None)
    x += fig.text(x + 24, y, "bit set", 16) + 24 + 40
    fig.rect(x, y - 12, 14, 14, fill="none", stroke=MUTED, stroke_width=1)
    x += fig.text(x + 24, y, "bit clear", 16) + 24 + 40
    fig.rect(x, y - 12, 14, 14, fill=CORAL, stroke=None)
    fig.text(x + 24, y, "position where A and B differ", 16)
    return fig


FIGURES = {
    "iscc-algo-design3": figure_iscc_code_units,
    "iscc-similarity-hash": figure_similarity_hash,
    "iscc-decentralized-issuance": figure_calculated_not_assigned,
    "iscc-similarity-comparison": figure_similarity_comparison,
}


def main():
    """Render every figure into docs/images, keeping the established file names and URLs."""
    for name, build in FIGURES.items():
        path = OUTPUT / f"{name}.svg"
        build().save(path)
        print(f"{path.relative_to(ROOT)}: {path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
