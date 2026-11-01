"""Generate the Heavy Bag concept sketch sheets (SVG).

Run:  python3 design/sketches/make_sketches.py
Then: node design/sketches/make_pdf.js   (combines the sheets into one PDF)

Each sheet is A3 landscape at 1680 x 1188 units (4 units per printed mm).
Bag sheets use 1 unit = 1 mm of product, i.e. scale 1:4 when printed on A3.
The weight-system sheet uses 2 units = 1 mm, i.e. scale 1:2 on A3.
All dimensions are concept dimensions in mm, to be confirmed with samples.
"""

from pathlib import Path

OUT = Path(__file__).parent
W, H = 1680, 1188

ALU = "#c4581c"     # aluminium frame
HDPE = "#2e8b57"    # HDPE / plastic structure
DIM = "#1f5fbf"     # dimensions
STEEL = "#cfd3d8"   # weights fill

STYLE = f"""
  text {{ font-family: Helvetica, Arial, sans-serif; fill: #111; }}
  .o  {{ fill: none; stroke: #111; stroke-width: 2.4; stroke-linejoin: round; }}
  .of {{ fill: #fff; stroke: #111; stroke-width: 2.4; stroke-linejoin: round; }}
  .t  {{ fill: none; stroke: #111; stroke-width: 1.2; }}
  .h  {{ fill: none; stroke: #666; stroke-width: 1.3; stroke-dasharray: 9 6; }}
  .z  {{ fill: none; stroke: #111; stroke-width: 1.4; stroke-dasharray: 3 3; }}
  .c  {{ fill: none; stroke: #888; stroke-width: 1; stroke-dasharray: 18 5 3 5; }}
  .al {{ fill: none; stroke: {ALU}; stroke-width: 3; stroke-dasharray: 10 5; }}
  .alf {{ fill: {ALU}; stroke: {ALU}; stroke-width: 1; }}
  .pe {{ fill: #cfe8d9; stroke: {HDPE}; stroke-width: 1.6; }}
  .wt {{ fill: {STEEL}; stroke: #111; stroke-width: 1.4; }}
  .lap {{ fill: #9aa3ad; stroke: #111; stroke-width: 1.2; }}
  .pad {{ fill: #f1ece2; stroke: #111; stroke-width: 1.2; }}
  .d  {{ fill: none; stroke: {DIM}; stroke-width: 1.1; }}
  .dt {{ fill: {DIM}; font-size: 17px; }}
  .lbl {{ font-size: 18px; font-weight: bold; letter-spacing: 1px; }}
  .sm {{ font-size: 15px; }}
  .note {{ font-size: 16px; }}
  .co {{ fill: #fff; stroke: #111; stroke-width: 1.6; }}
  .cot {{ font-size: 15px; font-weight: bold; }}
"""


class Sheet:
    def __init__(self):
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    # --- primitives -------------------------------------------------------
    def rect(self, x, y, w, h, cls="o", rx=0):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" class="{cls}"/>')

    def line(self, x1, y1, x2, y2, cls="t"):
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>')

    def path(self, d, cls="o"):
        self.add(f'<path d="{d}" class="{cls}"/>')

    def circle(self, x, y, r, cls="t"):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>')

    def text(self, x, y, s, cls="sm", anchor="start", rotate=None):
        tr = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{tr}>{s}</text>')

    # --- drafting helpers -------------------------------------------------
    def dim_h(self, x1, x2, y, label, y_from=None):
        """Horizontal dimension at height y; extension lines from y_from."""
        if y_from is not None:
            for x in (x1, x2):
                self.line(x, y_from, x, y + (6 if y > y_from else -6), "d")
        self.add(f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" class="d" '
                 f'marker-start="url(#a)" marker-end="url(#a)"/>')
        self.text((x1 + x2) / 2, y - 6, label, "dt", "middle")

    def dim_v(self, y1, y2, x, label, x_from=None):
        if x_from is not None:
            for y in (y1, y2):
                self.line(x_from, y, x + (6 if x > x_from else -6), y, "d")
        self.add(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" class="d" '
                 f'marker-start="url(#a)" marker-end="url(#a)"/>')
        self.text(x - 7, (y1 + y2) / 2, label, "dt", "middle", rotate=-90)

    def callout(self, n, x, y, tx, ty):
        """Numbered balloon at (tx, ty) with a leader to the point (x, y)."""
        self.line(x, y, tx, ty, "t")
        self.circle(x, y, 2.5, "alf" if False else "t")
        self.circle(tx, ty, 13, "co")
        self.text(tx, ty + 5, str(n), "cot", "middle")

    def view_label(self, x, y, s, scale=None):
        self.text(x, y, s, "lbl", "middle")
        if scale:
            self.text(x, y + 20, scale, "sm", "middle")

    def notes(self, x, y, title, items, width_chars=58):
        self.text(x, y, title, "lbl")
        y += 30
        for n, body in items:
            lines = wrap(body, width_chars)
            if n is not None:
                self.circle(x + 11, y - 5, 11, "co")
                self.text(x + 11, y, str(n), "cot", "middle")
            for i, ln in enumerate(lines):
                self.text(x + 32, y + i * 20, ln, "note")
            y += 20 * len(lines) + 8
        return y

    def legend(self, x, y):
        self.text(x, y, "LEGEND", "lbl")
        rows = [
            ('<line x1="0" y1="0" x2="46" y2="0" class="o"/>', "Visible outline"),
            ('<line x1="0" y1="0" x2="46" y2="0" class="h"/>', "Hidden / internal part"),
            ('<line x1="0" y1="0" x2="46" y2="0" class="z"/>', "Zip line"),
            ('<line x1="0" y1="0" x2="46" y2="0" class="al"/>', "Aluminium frame (6061-T6)"),
            ('<rect x="0" y="-8" width="46" height="16" class="pe"/>', "HDPE sheet / moulded plastic"),
            ('<rect x="0" y="-8" width="46" height="16" class="wt"/>', "Weights"),
            ('<line x1="0" y1="0" x2="46" y2="0" class="c"/>', "Centre line / load line"),
            ('<circle cx="23" cy="0" r="8" class="t"/><line x1="15" y1="0" x2="31" y2="0" class="t"/>'
             '<line x1="23" y1="-8" x2="23" y2="8" class="t"/>', "Loaded centre of mass (CoM)"),
        ]
        for i, (sym, lbl) in enumerate(rows):
            yy = y + 30 + i * 26
            self.add(f'<g transform="translate({x},{yy - 5})">{sym}</g>')
            self.text(x + 60, yy, lbl, "note")
        return y + 30 + len(rows) * 26

    def title_block(self, title, subtitle, sheet_no, scale):
        x, y, w, h = 1060, 1040, 590, 120
        self.rect(x, y, w, h, "t")
        self.line(x, y + 46, x + w, y + 46, "t")
        self.line(x + 400, y + 46, x + 400, y + h, "t")
        self.text(x + 14, y + 32, f"HEAVY BAG — {title}", "lbl")
        self.text(x + 14, y + 72, subtitle, "note")
        self.text(x + 14, y + 98, "Concept sketch · dims in mm · confirm with sample", "sm")
        self.text(x + 414, y + 72, f"Sheet {sheet_no} of 3", "note")
        self.text(x + 414, y + 98, scale, "sm")

    def frame(self):
        self.rect(20, 20, W - 40, H - 40, "t")

    def svg(self):
        body = "\n".join(self.parts)
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<style>{STYLE}</style>
<defs>
  <marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
    <path d="M0,1 L10,5 L0,9 z" fill="{DIM}"/>
  </marker>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="14" markerHeight="14" markerUnits="userSpaceOnUse" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="#111"/>
  </marker>
</defs>
<rect width="{W}" height="{H}" fill="#fff"/>
{body}
</svg>
"""


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def d_handle(s, cx, top_y, width=170, height=62, grip=28):
    """Rigid D-handle seen from the front: outer outline plus inner hand opening."""
    x0, x1 = cx - width / 2, cx + width / 2
    s.rect(x0, top_y - height, width, height, "of", rx=18)
    s.rect(cx - width / 2 + 24, top_y - height + grip, width - 48, height - grip + 2, "of", rx=8)
    # cover the joint with the bag top so the opening reads as open at the bottom
    s.line(cx - width / 2 + 24, top_y, cx + width / 2 - 24, top_y, "o")


# ======================================================================
# Sheet 1 — Laptop bag ("Heavy Brief")
# ======================================================================
def laptop_bag():
    s = Sheet()
    s.frame()
    BW, BH, BD = 420, 400, 130
    bx, by = 110, 250
    cx = bx + BW / 2

    # ---- FRONT VIEW ----
    s.rect(bx, by, BW, BH, "of", rx=24)
    d_handle(s, cx, by)
    # weight band seam and front pocket
    s.line(bx, by + 300, bx + BW, by + 300, "t")
    s.rect(bx + 40, by + 120, 340, 165, "o", rx=14)
    s.line(bx + 58, by + 138, bx + 362, by + 138, "z")
    s.rect(cx - 30, by + 175, 60, 16, "t", rx=3)
    s.text(cx, by + 210, "logo (deboss)", "sm", "middle")
    # hidden internals
    s.rect(bx + 32, by + 40, 356, 248, "h", rx=10)           # 16" laptop
    s.line(bx + 8, by + 297, bx + BW - 8, by + 297, "h")      # false floor
    s.rect(bx + 14, by + 302, 392, 92, "h", rx=4)            # weight tray
    for i in range(1, 4):                                    # 95 mm modules
        x = bx + 14 + 6 + i * 95
        s.line(x, by + 306, x, by + 390, "h")
    # aluminium U-frame: bridge + two end stays + cradle
    s.line(bx + 10, by + 10, bx + BW - 10, by + 10, "al")
    s.line(bx + 10, by + 10, bx + 10, by + BH - 4, "al")
    s.line(bx + BW - 10, by + 10, bx + BW - 10, by + BH - 4, "al")
    s.line(bx + 10, by + BH - 4, bx + BW - 10, by + BH - 4, "al")
    # D-rings and feet
    for x in (bx - 4, bx + BW - 12):
        s.rect(x, by + 26, 16, 22, "t", rx=6)
    for x in (bx + 30, bx + BW - 60):
        s.rect(x, by + BH, 30, 6, "o", rx=2)
    s.line(cx, by - 90, cx, by + BH + 30, "c")
    # dims
    s.dim_h(bx, bx + BW, by + BH + 50, "420", by + BH + 8)
    s.dim_v(by, by + BH, bx - 40, "400", bx)
    s.dim_v(by - 62, by, bx + 80, "62", None)
    s.dim_v(by + 300, by + BH, bx + BW + 40, "100 weight band", bx + BW)
    s.view_label(cx, by + BH + 100, "FRONT VIEW")
    # callouts
    s.callout(1, cx + 40, by - 48, cx + 130, by - 95)
    s.callout(2, bx + BW - 10, by + 60, bx + BW + 60, by + 30)
    s.callout(3, bx + 300, by + 220, bx + BW + 60, by + 160)
    s.callout(4, bx + 250, by + 350, bx + BW + 60, by + 250)
    s.callout(5, bx + 60, by + 297, bx - 60, by + 250)
    s.callout(6, bx + 300, by + 138, bx + BW + 60, by + 95)
    s.callout(12, bx + 45, by + BH + 3, bx - 60, by + BH + 30)

    # ---- END VIEW (weight hatch side) ----
    sx = 690
    s.rect(sx, by, BD, BH, "of", rx=20)
    s.rect(sx + 50, by - 62, 30, 62, "of", rx=8)
    s.rect(sx + 5, by + 296, BD - 10, 100, "z", rx=10)       # hatch zip
    s.rect(sx + 9, by + 302, 112, 92, "o", rx=6)              # tray end cap
    s.rect(sx + 35, by + 330, 60, 18, "o", rx=8)              # pull grip
    s.circle(sx + 65, by + 372, 8, "o")                        # latch button
    s.rect(sx + 57, by + 26, 16, 22, "t", rx=6)               # D-ring
    s.line(sx + 15, by + 10, sx + 15, by + BH - 4, "al")
    s.dim_h(sx, sx + BD, by + BH + 50, "130", by + BH + 8)
    s.callout(7, sx + 80, by + 339, sx + 100, by + 250)
    s.callout(8, sx + 65, by + 372, sx - 30, by + 440)
    s.view_label(sx + BD / 2, by + BH + 100, "END VIEW")

    # ---- SECTION A-A ----
    ax = 900
    s.rect(ax, by, BD, BH, "of", rx=20)
    s.rect(ax + 50, by - 62, 30, 62, "of", rx=8)
    s.rect(ax + 48, by + 3, 34, 9, "alf")                       # bridge section
    s.rect(ax + 5, by + 292, BD - 10, 5, "pe")                  # false floor
    s.rect(ax + 9, by + 300, 112, 95, "pe", rx=4)               # tray shell
    s.rect(ax + 13, by + 304, 104, 87, "of")                    # tray inside
    yb = by + 391
    for hgt in (33, 33, 16.5):                                  # brick stack
        yb -= hgt
        s.rect(ax + 16, yb, 98, hgt, "wt", rx=3)
    s.rect(ax + 14, yb - 5, 102, 4, "pe")                       # clamp plate
    s.rect(ax + 6, by + 40, 34, 250, "pad", rx=6)               # laptop sleeve
    s.rect(ax + 14, by + 46, 17, 240, "lap", rx=3)              # laptop
    s.line(ax + 104, by + 120, ax + 104, by + 288, "t")         # front pocket wall
    s.text(ax + 72, by + 200, "main", "sm", "middle")
    s.text(ax + 117, by + 215, "pkt", "sm", "middle", rotate=-90)
    s.line(ax + 65, by - 90, ax + 65, by + BH + 20, "c")
    s.circle(ax + 64, by + 330, 9, "t")
    s.line(ax + 55, by + 330, ax + 73, by + 330, "t")
    s.line(ax + 64, by + 321, ax + 64, by + 339, "t")
    s.text(ax + 76, by + 327, "CoM", "sm")
    s.dim_v(by + 300, by + 395, ax + BD + 30, "95", ax + BD)
    s.callout(9, ax + 20, by + 160, ax - 30, by + 120)
    s.callout(10, ax + 65, by + 358, ax - 30, by + 330)
    s.callout(11, ax + 65, by + 7, ax + 120, by - 40)
    s.callout(5, ax + 60, by + 294, ax - 30, by + 270)
    s.view_label(ax + BD / 2, by + BH + 100, "SECTION A–A")

    # ---- TOP VIEW ----
    tx, ty = bx, 860
    s.rect(tx, ty, BW, BD, "of", rx=22)
    s.rect(tx + 18, ty + 16, BW - 36, BD - 32, "z", rx=14)     # main zip
    s.rect(cx - 85, ty + 50, 170, 30, "of", rx=14)              # handle
    s.rect(cx - 61, ty + 52, 122, 26, "t", rx=6)
    s.line(tx - 20, ty + BD / 2, tx + BW + 20, ty + BD / 2, "c")
    s.text(tx - 34, ty + BD / 2 + 6, "A", "lbl", "middle")
    s.text(tx + BW + 34, ty + BD / 2 + 6, "A", "lbl", "middle")
    s.add(f'<line x1="{tx + BW + 10}" y1="{ty + 110}" x2="{tx + BW + 70}" y2="{ty + 110}" '
          f'class="o" marker-end="url(#arr)"/>')
    s.text(tx + BW + 12, ty + 128, "tray out", "sm")
    s.dim_h(tx, tx + BW, ty + BD + 40, "420", ty + BD + 6)
    s.callout(13, tx + 40, ty + 16, tx - 40, ty - 10)
    s.view_label(cx, ty + BD + 90, "TOP VIEW")

    # ---- NOTES ----
    y = s.notes(1110, 70, "LAPTOP BAG — “HEAVY BRIEF” (working name)", [
        (None, "One-hand suitcase carry, up to 30 kg total (bag + 16\" laptop + contents + up to 24 kg weights). Must hang straight and feel the same in either hand."),
        (1, "Rigid top handle, ~30 mm grip, bolted/riveted to the aluminium bridge (11). Not sewn-only. Rated 90 kg static."),
        (2, "Aluminium U-frame: top bridge + one stay in each end panel + bottom cradle under the tray. All load goes handle → frame → tray."),
        (3, "16\" MacBook Pro (356 × 248 × 17 mm) in padded sleeve against back wall (9)."),
        (4, "Weight tray in a 100 mm base band, centred under the handle. 4 modules of 95 × 100 mm; full 24 kg with steel bricks or steel bar. See sheet 3."),
        (5, "Rigid HDPE false floor separates the weights from laptop and contents."),
        (6, "Front organiser pocket, zipped."),
        (7, "Tray slides out of a zipped hatch in one end panel, on HDPE runners. Tray end cap has a pull grip."),
        (8, "Two-step release: open hatch zip, then press latch and pull. Tray can't fall out by accident."),
        (10, "Clamp plate + 2 cam straps press any stack (10–85 mm) to stop rattle."),
        (12, "Four protective base feet."),
        (13, "Main zip, 2-way, heavy coil, runs over the top."),
        (None, "Detachable shoulder strap clips to the two D-rings."),
    ])
    s.legend(1110, y + 12)
    s.title_block("LAPTOP BAG", "Front, end, section and top views", 1, "Scale 1:4 at A3")
    return s


# ======================================================================
# Sheet 2 — Backpack ("Big Pack")
# ======================================================================
def big_pack():
    s = Sheet()
    s.frame()
    PW, PH, PD = 310, 480, 160
    fx, fy = 110, 190
    cx = fx + PW / 2

    # ---- FRONT VIEW ----
    s.rect(fx, fy, PW, PH, "of", rx=46)
    d_handle(s, cx, fy)
    s.path(f"M{fx + 22},{fy + 270} L{fx + 22},{fy + 60} Q{fx + 22},{fy + 18} {fx + 64},{fy + 18} "
           f"L{fx + PW - 64},{fy + 18} Q{fx + PW - 22},{fy + 18} {fx + PW - 22},{fy + 60} "
           f"L{fx + PW - 22},{fy + 270}", "z")                    # main zip
    s.rect(fx + 45, fy + 250, 220, 200, "o", rx=16)               # front pocket
    s.line(fx + 62, fy + 268, fx + 248, fy + 268, "z")
    s.rect(cx - 30, fy + 300, 60, 16, "t", rx=3)
    s.text(cx, fy + 336, "logo (deboss)", "sm", "middle")
    s.rect(fx + 12, fy + 170, 286, 300, "h", rx=6)                # weight carrier
    for i in (1, 2):
        s.line(fx + 12 + i * 95, fy + 174, fx + 12 + i * 95, fy + 466, "h")
        s.line(fx + 16, fy + 170 + i * 100, fx + 294, fy + 170 + i * 100, "h")
    for x in (fx + 40, fx + PW - 70):
        s.rect(x, fy + PH, 30, 6, "o", rx=2)
    s.line(cx, fy - 90, cx, fy + PH + 30, "c")
    s.dim_h(fx, fx + PW, fy + PH + 50, "310", fy + PH + 8)
    s.dim_v(fy, fy + PH, fx - 40, "480", fx)
    s.dim_v(fy + 170, fy + 470, fx + PW + 34, "300 weight zone", fx + PW)
    s.callout(1, cx + 40, fy - 48, cx + 130, fy - 95)
    s.callout(4, fx + 200, fy + 420, fx + PW + 70, fy + 400)
    s.callout(6, fx + 230, fy + 268, fx + PW + 70, fy + 240)
    s.view_label(cx, fy + PH + 88, "FRONT VIEW")

    # ---- BACK VIEW ----
    kx = 520
    s.rect(kx, fy, PW, PH, "of", rx=46)
    d_handle(s, kx + PW / 2, fy)
    s.line(kx + 50, fy + 30, kx + PW - 50, fy + 30, "z")          # weight slot zip
    s.rect(kx + PW / 2 - 14, fy + 24, 28, 12, "t", rx=4)          # slot buckle tab
    s.rect(kx + 40, fy + 60, 230, 340, "z", rx=20)                # strap stow panel
    for side in (-1, 1):
        x_top = kx + PW / 2 + side * 55
        x_bot = kx + PW / 2 + side * 120
        s.path(f"M{x_top - 28},{fy + 70} L{x_top + 28},{fy + 70} "
               f"L{x_bot + 26},{fy + 390} L{x_bot - 26},{fy + 390} Z", "o")
        s.rect(kx + PW / 2 + side * 125 - 12, fy + 455, 24, 14, "t", rx=4)  # strap anchor
    s.rect(kx + PW / 2 - 70, fy + 200, 140, 12, "o", rx=6)        # sternum strap
    s.rect(kx + 60, fy + 415, 190, 50, "pad", rx=12)              # lumbar pad
    s.line(kx + 18, fy + 20, kx + 18, fy + PH - 10, "al")
    s.line(kx + PW - 18, fy + 20, kx + PW - 18, fy + PH - 10, "al")
    s.callout(7, kx + 220, fy + 30, kx + PW + 60, fy + 10)
    s.callout(8, kx + PW / 2, fy + 30, kx + PW + 60, fy + 70)
    s.callout(9, kx + 255, fy + 120, kx + PW + 60, fy + 130)
    s.callout(2, kx + 18, fy + 300, kx - 40, fy + 330)
    s.callout(12, kx + 150, fy + 440, kx + PW + 60, fy + 420)
    s.view_label(kx + PW / 2, fy + PH + 88, "BACK VIEW (straps out)")

    # ---- SECTION B-B (side) : back panel on the left ----
    ax = 930
    s.rect(ax, fy, PD, PH, "of", rx=30)
    s.rect(ax + 15, fy - 62, 50, 62, "of", rx=10)                 # handle edge-on
    s.rect(ax + 12, fy + 3, 58, 9, "alf")                          # bridge
    s.rect(ax + 4, fy + 40, 12, 420, "pad", rx=4)                 # back padding
    s.rect(ax + 16, fy + 20, 4, 450, "pe")                         # frame sheet
    s.line(ax + 18, fy + 20, ax + 18, fy + 470, "al")
    s.rect(ax + 20, fy + 30, 58, 442, "t", rx=4)                   # weight sleeve
    s.rect(ax + 22, fy + 170, 52, 300, "pe", rx=4)                 # carrier
    for r in range(3):
        s.rect(ax + 26, fy + 172 + r * 100, 33, 96, "wt", rx=3)
        s.rect(ax + 59.5, fy + 172 + r * 100, 12, 96, "wt", rx=2)
    s.rect(ax + 80, fy + 60, 28, 380, "pad", rx=6)                 # laptop sleeve
    s.rect(ax + 86, fy + 66, 17, 356, "lap", rx=3)
    s.line(ax + 138, fy + 250, ax + 138, fy + 450, "t")
    s.text(ax + 123, fy + 160, "main", "sm", "middle", rotate=-90)
    s.text(ax + 150, fy + 360, "pkt", "sm", "middle", rotate=-90)
    s.line(ax + 40, fy - 90, ax + 40, fy + PH + 20, "c")
    s.circle(ax + 52, fy + 330, 9, "t")
    s.line(ax + 43, fy + 330, ax + 61, fy + 330, "t")
    s.line(ax + 52, fy + 321, ax + 52, fy + 339, "t")
    s.text(ax + 64, fy + 327, "CoM", "sm")
    s.dim_h(ax, ax + PD, fy + PH + 50, "160", fy + PH + 8)
    s.callout(3, ax + 95, fy + 120, ax + PD + 28, fy + 60)
    s.callout(10, ax + 45, fy + 230, ax - 35, fy + 200)
    s.callout(11, ax + 40, fy + 7, ax + 110, fy - 40)
    s.callout(5, ax + 18, fy + 450, ax - 35, fy + 470)
    s.view_label(ax + PD / 2, fy + PH + 88, "SECTION B–B")

    # ---- WEIGHT CARRIER ----
    wx, wy = 110, 850
    s.rect(wx, wy, 297, 312, "pe", rx=8)
    s.rect(wx + 6, wy + 6, 285, 300, "of", rx=4)
    for r in range(3):
        for c in range(3):
            s.rect(wx + 9 + c * 95, wy + 9 + r * 100, 89, 94, "wt", rx=4)
            s.text(wx + 9 + c * 95 + 44, wy + 9 + r * 100 + 53, "2.5", "sm", "middle")
    s.rect(wx + 34, wy + 10, 229, 292, "h")                         # ruck plate outline
    s.rect(wx + 108, wy - 22, 80, 22, "o", rx=8)                    # pull loop
    s.dim_h(wx, wx + 297, wy - 40, "297", wy - 4)
    s.dim_v(wy, wy + 312, wx - 30, "312", wx)
    s.text(wx + 330, wy + 40, "Weight carrier (front, 1:4)", "lbl")
    for i, ln in enumerate([
        "3 × 3 modules of 95 × 100 mm (sheet 3).",
        "Up to 9 steel bricks × 2.5 kg = 22.5 kg,",
        "plus a half-brick layer to reach 24 kg.",
        "Dashed: standard ruck plate 229 × 292 mm",
        "fits the same sleeve (carrier removed).",
        "Lifts out by the pull loop through slot (7).",
    ]):
        s.text(wx + 330, wy + 74 + i * 22, ln, "note")

    # ---- NOTES ----
    y = s.notes(1150, 70, "BACKPACK — “BIG PACK”", [
        (None, "Same 30 kg total rating and one-hand suitcase carry as the laptop bag. Worn as a backpack it's a rest mode (or rucking)."),
        (1, "Rigid top handle on the aluminium bridge (11), placed over the loaded centre of mass — close to the back panel, not mid-bag."),
        (2, "Two aluminium stays in the back panel, joined by the top bridge and a bottom cradle; HDPE frame sheet between them."),
        (3, "16\" MacBook Pro in padded sleeve, in front of the weight sleeve."),
        (4, "Weight carrier sits low in a sleeve against the frame sheet: weight closest to the spine."),
        (5, "Frame sheet and stays carry the load to the bottom cradle."),
        (6, "Front organiser pocket."),
        (7, "Top-loading weight slot: zip across the top of the back panel; carrier lifts out by its pull loop."),
        (8, "Two-step release: buckle tab over the zip pull, then unzip."),
        (9, "Shoulder straps tuck behind a zip panel during the hand carry — nothing dangles when switching hands."),
        (10, "Carrier holds 3 × 3 bricks, ruck plates, fill-your-own shells or flat plates; cam strap clamps it."),
        (12, "Strap anchors, lumbar pad and base feet."),
    ])
    s.legend(1150, y + 12)
    s.title_block("BACKPACK", "Front, back and section views; weight carrier", 2, "Scale 1:4 at A3")
    return s


# ======================================================================
# Sheet 3 — Weight system ("one tray, any weight")
# ======================================================================
def weight_system():
    s = Sheet()
    s.frame()
    k = 2  # 2 units per mm (1:2 at A3)

    # ---- LAPTOP TRAY: top view ----
    tx, ty = 90, 130
    TL, TW = 392, 112
    s.rect(tx, ty, TL * k, TW * k, "pe", rx=10)
    s.rect(tx + 6 * k, ty + 4 * k, 380 * k, 104 * k, "of", rx=4)
    for i in range(4):
        s.rect(tx + (6 + i * 95) * k + 3, ty + 6 * k, 95 * k - 6, 100 * k, "wt", rx=6)
        s.text(tx + (6 + i * 95 + 47.5) * k, ty + 60 * k, "95 × 100", "sm", "middle")
    for x in (120, 270):                                           # cam straps
        s.rect(tx + x * k, ty - 6, 25 * k, TW * k + 12, "t", rx=4)
    s.rect(tx + TL * k, ty + 30 * k, 18 * k, 52 * k, "pe", rx=8)   # end cap
    s.rect(tx + TL * k + 8, ty + 42 * k, 10 * k, 28 * k, "of", rx=6)
    s.dim_h(tx, tx + TL * k, ty - 30, "392", ty - 8)
    s.dim_v(ty, ty + TW * k, tx - 30, "112", tx)
    s.dim_h(tx + 6 * k, tx + 101 * k, ty + TW * k + 36, "95 module", ty + TW * k + 6)
    s.callout(1, tx + 135 * k, ty + 2, tx + 135 * k, ty - 60)
    s.callout(2, tx + (TL + 9) * k, ty + 56 * k, tx + (TL + 40) * k, ty + 20 * k)
    s.view_label(tx + TL * k / 2, ty + TW * k + 100, "LAPTOP-BAG WEIGHT TRAY — TOP (lid off)", "1:2")

    # ---- LAPTOP TRAY: side elevation with three loadings ----
    ey = 560
    s.rect(tx, ey, TL * k, 95 * k, "pe", rx=8)
    s.rect(tx + 6 * k, ey + 4 * k, 380 * k, 87 * k, "of", rx=3)
    floor = ey + 91 * k
    # left half: steel bricks (2 full + 1 half layer); right half: steel bar in sleeves
    yb = floor
    for hgt in (33, 33, 16.5):
        yb -= hgt * k
        for i in range(2):
            s.rect(tx + (6 + i * 95) * k + 3, yb, 95 * k - 6, hgt * k - 3, "wt", rx=5)
    s.rect(tx + 6 * k, yb - 5 * k, 190 * k, 4 * k, "pe")
    yb = floor
    for _ in range(8):
        yb -= 10 * k
        s.rect(tx + 196 * k, yb, 190 * k - 4, 10 * k - 2, "wt", rx=3)
    s.rect(tx + 196 * k, yb - 5 * k, 190 * k, 4 * k, "pe")
    s.line(tx + 196 * k - 2, ey + 6, tx + 196 * k - 2, ey + 95 * k - 6, "c")
    s.text(tx + 101 * k, ey - 14, "steel bricks: 2.5 + 2.5 + 1.25 kg per module", "sm", "middle")
    s.text(tx + 291 * k, ey - 14, "steel flat bar 100 × 10, 8 layers", "sm", "middle")
    s.dim_v(ey, ey + 95 * k, tx - 30, "95", tx)
    s.callout(3, tx + 100 * k, yb - 3 * k + 1, tx + 100 * k, ey - 60)
    s.view_label(tx + TL * k / 2, ey + 95 * k + 50, "TRAY — SIDE ELEVATION (two loadings shown)", "1:2")

    # ---- BRICK + SHELL ----
    bx, by = 90, 850
    s.rect(bx, by, 95 * k, 100 * k, "wt", rx=8)
    s.text(bx + 95, by + 108, "2.5 kg", "lbl", "middle")
    s.rect(bx + 95 * k + 40, by, 33 * k, 100 * k, "wt", rx=8)
    s.rect(bx + 95 * k + 40 + 33 * k + 30, by + 0, 16.5 * k, 100 * k, "wt", rx=6)
    s.dim_h(bx, bx + 95 * k, by + 100 * k + 30, "95", by + 100 * k + 6)
    s.dim_v(by, by + 100 * k, bx - 26, "100", bx)
    s.dim_h(bx + 95 * k + 40, bx + 95 * k + 40 + 33 * k, by + 100 * k + 30, "33", by + 100 * k + 6)
    s.dim_h(bx + 95 * k + 40 + 33 * k + 30, bx + 95 * k + 40 + 33 * k + 30 + 16.5 * k,
            by + 100 * k + 30, "16.5", by + 100 * k + 6)
    s.text(bx + 95 * k + 40 + 33 * k + 30 + 16.5 * k + 14, by + 30, "half brick", "sm")
    s.text(bx + 95 * k + 40 + 33 * k + 30 + 16.5 * k + 14, by + 50, "1.25 kg", "sm")
    s.view_label(bx + 180, by + 100 * k + 75, "STEEL BRICK — front + edge", "1:2")

    sx = 560
    s.rect(sx, by, 95 * k, 100 * k, "pe", rx=10)
    s.rect(sx + 70, by - 18, 50, 18, "o", rx=4)                     # cap
    s.rect(sx + 95 * k + 40, by, 33 * k, 100 * k, "pe", rx=10)
    s.view_label(sx + 140, by + 100 * k + 75, "FILL-YOUR-OWN SHELL — same footprint", "1:2")
    s.callout(4, sx + 120, by - 10, sx + 220, by - 30)

    # ---- NOTES ----
    y = s.notes(1110, 70, "WEIGHT SYSTEM — “ONE TRAY, ANY WEIGHT”", [
        (None, "The bags sell a standard weight interface. Every weight source fits the same module, so one tray (laptop bag) and one carrier (Big Pack) take them all."),
        (None, "MODULE: 95 × 100 mm footprint. Laptop tray = 4 × 1 modules, 85 mm usable height. Big Pack carrier = 3 × 3 modules, 50 mm."),
        (1, "Two cam straps press a clamp plate onto any stack from 10 to 85 mm: no rattle with any source."),
        (2, "Tray end cap with pull grip and latch; slides on HDPE runners. Tray: aluminium or glass-filled nylon, HDPE liner."),
        (3, "Clamp plate (HDPE, 4 mm)."),
        (4, "Fill-your-own shell: HDPE, screw cap with snap seal. Ships empty; fill with steel shot (~1 kg), sand or water. Long 4-module shell (380 × 100 × 35) for the laptop tray holds ~5 kg of shot."),
        (None, "STEEL BRICK: 95 × 100 × 33 mm steel, 2.5 kg; half brick 16.5 mm, 1.25 kg. TPU or rubber coated, R3 edges, weight laser-marked on face. No lead."),
        (None, "LOCAL STEEL BAR: 100 × 10 mm mild steel cut to 380 mm (3.0 kg, laptop tray) or 285 mm (2.2 kg, Big Pack). We supply TPU sleeves with end caps."),
        (None, "PLATES: standard ruck plate 229 × 292 mm goes straight into the Big Pack sleeve. 1\" gym plates up to 150 mm diameter lie flat in the Big Pack carrier. Gym plates don't fit the laptop tray."),
        (None, "CAPACITY: laptop tray 24 kg with bricks or bar; ~13–16 kg with shot shells. Big Pack 24 kg with any source."),
    ])
    s.legend(1110, y + 12)
    s.title_block("WEIGHT SYSTEM", "Tray, carrier module, bricks and shells", 3, "Scale 1:2 at A3")
    return s


if __name__ == "__main__":
    for name, fn in [("1-laptop-bag", laptop_bag), ("2-big-pack", big_pack), ("3-weight-system", weight_system)]:
        (OUT / f"{name}.svg").write_text(fn().svg())
        print("wrote", OUT / f"{name}.svg")
