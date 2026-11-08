"""Generate the Heavy Bag concept sketch sheets (SVG).

Run:  python3 design/sketches/make_sketches.py
Then: node design/sketches/make_pdf.js   (combines the sheets into one PDF)

Each sheet is A3 landscape at 1680 x 1188 units (4 units per printed mm).
Bag sheets use 1 unit = 1 mm of product, i.e. scale 1:4 when printed on A3.
The weight-system sheet uses 2 units = 1 mm, i.e. scale 1:2 on A3.
All dimensions are provisional packaging in mm, not engineering validated.
Use --output-dir to render to isolated scratch storage. Source: geometry.json.
"""

from pathlib import Path
import argparse
import html
import json

SOURCE = Path(__file__).resolve().parent
G = json.loads((SOURCE / "geometry.json").read_text())
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
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{tr}>{html.escape(str(s))}</text>')

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


# Envelope order is explicit: laptop L,D,H; backpack W,H,D.
# Coordinates below are body-space mm, except the labelled 2x detail views.
def receiver_handle(s, cx, body_top):
    """Symbolic modular handle, not a commercial-handle fit specification."""
    pitch = G['handle']['receiver_pitch_mm']
    for x in (cx - pitch / 2, cx + pitch / 2):
        s.rect(x - 10, body_top - 8, 20, 12, 'alf', rx=2)
        s.circle(x, body_top - 3, 3, 't')
    s.path(f'M{cx-pitch/2},{body_top-8} L{cx-pitch/2},{body_top-65} '
           f'L{cx+pitch/2},{body_top-65} L{cx+pitch/2},{body_top-8}', 'o')
    s.rect(cx - 60, body_top - 80, 120, 30, 'pad', rx=10)
    s.text(cx, body_top - 97, 'Interchangeable module (symbolic)', 'sm', 'middle')


def footer(s, title, sheet):
    s.text(60, 1090, 'PROVISIONAL PACKAGING ONLY — NOT ENGINEERING VALIDATED', 'lbl')
    s.text(60, 1118, 'Blue: dimensions · orange: frame/receivers · green: barrier/enclosure · grey: weight', 'sm')
    s.text(60, 1143, 'SVG / PNG / PDF exports regenerated from current generator. See tech-pack v0.2.', 'sm')
    s.title_block(title, 'Product-design / POC revision v0.2', sheet, 'Views as labelled')


def laptop_bag():
    s = Sheet(); s.frame()
    q = G['laptop']; bw, bh, bd = q['body_mm']
    cl, cd, ch = q['cassette_outer_mm']
    sw, sh, sd = q['sleeve_outer_mm']
    bx, by = 110, 240
    base = by + bh
    s.rect(bx, by, bw, bh, 'of', rx=10)
    receiver_handle(s, bx + bw / 2, by)
    # Keep shell outline corners symbolic; critical clear envelopes are square.
    for x in (bx + 8, bx + bw - 8):
        s.line(x, by + 10, x, base - 5, 'al')
    s.line(bx + 8, by + 10, bx + bw - 8, by + 10, 'al')
    s.line(bx + 8, base - 5, bx + bw - 8, base - 5, 'al')
    s.rect(bx + (bw-cl)/2, base-q['cassette_top_mm'], cl, ch, 'pe')
    for i in range(4):
        s.rect(bx + (bw-cl)/2 + 6 + i*99, base-112, 97, 88, 'wt', rx=2)
    sy = base-q['sleeve_bottom_mm']-sh
    s.rect(bx+(bw-sw)/2, sy, sw, sh, 'pad', rx=4)
    s.rect(bx+(bw-356)/2, sy+12, 356, 248, 'lap', rx=3)
    s.line(bx+20, sy, bx+20, by+10, 't')
    s.line(bx+bw-20, sy, bx+bw-20, by+10, 't')
    s.rect(bx+14, base-124, bw-28, 4, 'pe')
    s.rect(bx+28, base-130, bw-56, 6, 'pad')
    s.text(bx+bw/2, sy+125, '356 × 248 laptop surrogate', 'sm', 'middle')
    s.dim_h(bx, bx+bw, base+35, str(bw), base)
    s.dim_v(by, base, bx-35, str(bh), bx)
    s.view_label(bx+bw/2, base+72, 'FRONT — 1:4 AT A3')

    ax = 760
    s.rect(ax, by, bd, bh, 'of', rx=8)
    s.rect(ax+14, base-116, cd, ch, 'pe')
    floor = base-14
    for h in (35,35,18):
        floor -= h
        s.rect(ax+20, floor, 102, h, 'wt')
    s.rect(ax+18, floor-4, 106, 4, 'pe')
    s.rect(ax+14, base-124, 122, 4, 'pe')
    s.rect(ax+22, base-130, 106, 6, 'pad')
    s.rect(ax+14, sy, sd, sh, 'pad')
    s.rect(ax+24, sy+12, 17, 248, 'lap')
    s.line(ax+15, by+8, ax+15, sy, 'al')
    s.dim_h(ax, ax+bd, base+35, str(bd), base)
    s.dim_v(base-142, base-130, ax-25, '12 free', ax)
    s.dim_v(base-116, base-10, ax+bd+35, '106 cassette', ax+bd)
    s.view_label(ax+bd/2, base+72, 'SECTION — 1:4')
    s.text(ax+bd/2, by-15, 'Suspend sleeve from upper structure', 'sm', 'middle')
    # End-hatch clear-opening detail; enclosure projects inside with2mm/face.
    hx,hy=770,80
    s.rect(hx-8,hy-8,134,126,'al')
    s.rect(hx,hy,118,110,'z')
    s.rect(hx+2,hy+2,114,106,'pe')
    s.dim_h(hx,hx+118,hy-20,'118 clear',hy)
    s.dim_v(hy,hy+110,hx+150,'110 clear',hx+118)
    s.text(hx+59,hy-48,'END HATCH — 1:4','lbl','middle')

    # Supported-slide proposal: top schematic uses true body-space dimensions.
    x, y = 110, 830
    s.rect(x, y, bw, bd, 'o')
    s.rect(x+bw+10, y, 450, bd, 'pad')
    s.text(x+bw+235, y-15, 'Adjacent stable support ≥450 long', 'sm', 'middle')
    s.rect(x+bw-65, y+(bd-cd)/2, cl, cd, 'pe')
    for gx in (x+bw-50, x+bw-65+cl-30):
        s.rect(gx, y+60, 20, 24, 'h')
    s.line(x+bw-10, y+5, x+bw-10, y+bd-5, 'd')
    s.text(x+220, y+60, 'Bag set down', 'sm', 'middle')
    s.text(x+bw+130, y+82, 'Two stowable lifting grips', 'sm', 'middle')
    s.view_label(555, y+bd+35, 'PROPOSAL A: SUPPORTED SLIDE — NOT SELECTED')
    s.text(110, 1044, 'Travel stop before loss of runner support; deliberate final release only after support.', 'sm')

    s.notes(1060, 70, 'LAPTOP BAG — HEAVY BRIEF', [
        (None, 'For office workers who lift heavy. Start light; 30 kg total maximum, not a required goal. Targets untested.'),
        (1, '440 W × 430 H × 150 D body. 406 L × 114 D × 106 H cassette; clear bay 414 × 122 × 110.'),
        (2, 'Clear hatch 118 D × 110 H after zip and lining intrusion. End-frame load path must route around hatch, not cross extraction path.'),
        (3, 'Base stack: 10 cradle + 106 cassette + 4 clearance + 4 barrier + 6 impact pad + 12 free gap + 272 padded sleeve + 16 top = 430.'),
        (4, 'Suspended sleeve clear 370 × 260 × 25; outer 382 × 272 × 37. Replaceable pads. Test hard bottom-out with a surrogate, not a real laptop.'),
        (5, 'Frame-mounted modular fabric or standard rigid handle. Captive bolts POC. Double weight handle meaning/geometry TBD; see sheet 3.'),
        (6, 'Supported single cassette vs two smaller cassettes stays OPEN. Split loses continuous long-bar fit. Neither is a final mechanism decision.'),
        (7, '88 mm stack + 4 clamp + 6 reserve. Two full + one half = 6.25 kg/module; four = 25 kg, over example 24 kg allowance.'),
        (8, '8 full + 3 half = 23.75 kg nominal example. Actual complete mass, including tray and handle, must be ≤30 kg. No automatic volume limiter.'),
    ], width_chars=58)
    footer(s, 'LAPTOP BAG', 1)
    return s


def big_pack():
    s = Sheet(); s.frame()
    q=G['backpack']; bw,bh,bd=q['body_mm']; cw,ch,cd=q['carrier_outer_mm']
    bx,by=110,230; base=by+bh
    s.rect(bx,by,bw,bh,'of',rx=12)
    receiver_handle(s,bx+bw/2,by)
    for x in (bx+14,bx+bw-14):
        s.line(x,by+10,x,base-10,'al')
    s.line(bx+14,by+10,bx+bw-14,by+10,'al')
    # Both positions shown as alternatives, never an installed adjustment rail.
    x=bx+(bw-cw)/2
    low_top=base-q['low_carrier_bottom_mm']-ch
    mid_top=base-q['midlow_carrier_bottom_mm']-ch
    s.rect(x-6,low_top-6,cw+12,ch+12,'h')
    s.rect(x,low_top,cw,ch,'pe')
    for r in range(3):
        for c in range(3):
            s.rect(x+6+c*99,low_top+6+r*104,97,102,'wt',rx=2)
    s.rect(x,mid_top,cw,ch,'d')
    s.dim_v(mid_top,low_top,bx+bw+30,'30 offset',bx+bw)
    s.dim_h(bx,bx+bw,base+35,str(bw),base)
    s.dim_v(by,base,bx-35,str(bh),bx)
    s.view_label(bx+bw/2,base+72,'FRONT — 1:4 AT A3')
    s.text(bx+bw/2,by+80,'Blue = alternative fixed mid-low', 'sm','middle')

    ax=750
    s.rect(ax,by,bd,bh,'of',rx=8)
    s.rect(ax,by+14,18,bh-28,'pad')
    s.line(ax+16,by+10,ax+16,base-10,'al')
    s.rect(ax+18,low_top-6,78,ch+12,'h')
    s.rect(ax+24,low_top,cd,ch,'pe')
    for r in range(3):
        s.rect(ax+28,low_top+6+r*104,35,102,'wt')
        s.rect(ax+63,low_top+6+r*104,18,102,'wt')
    s.rect(ax+24,mid_top,cd,ch,'d')
    s.rect(ax+96,by+20,4,bh-40,'pe')
    # 12 lateral gap from barrier at100 to sleeve at112.
    sw,sh,sd=q['sleeve_outer_mm']; sy=base-q['sleeve_bottom_mm']-sh
    s.rect(ax+100,sy+30,6,sh-60,'pad')
    s.rect(ax+112,sy,sd,sh,'pad')
    s.rect(ax+122,sy+13,17,356,'lap')
    s.line(ax+113,by+10,ax+113,sy,'t')
    s.rect(ax+112,base-20,sd,6,'pad')
    s.dim_h(ax,ax+bd,base+35,str(bd),base)
    s.view_label(ax+bd/2,base+72,'SECTION — 1:4')
    s.text(ax+bd/2,by-25,'Back at left; laptop portrait', 'sm','middle')
    s.text(ax+140,base-40,'12 free above base pad', 'sm','middle',rotate=-90)

    # Detail: carrier grid fits finished bricks with actual gaps at scale1:4.
    wx,wy=110,850
    s.rect(wx,wy,cw,ch/2,'pe')  # compact projection is explicitly NTS below
    for c in range(3):
        s.rect(wx+6+c*99,wy+6,97,102,'wt')
    s.dim_h(wx,wx+cw,wy-24,str(cw),wy)
    s.text(wx+cw/2,wy+137,'3 × 3 grid; diagram cropped to one row', 'sm','middle')
    s.text(470,860,'Carrier overall 307 W × 322 H × 66 D', 'lbl')
    for i,line in enumerate([
        'Clear cavity 299 × 314 × 58; 53 stack +4 clamp +1 reserve.',
        'Bay 319 × 334 × 78. Side structure/textile 20.5 each.',
        'LOW bottom36 / top358; MID-LOW bottom66 / top388.',
        'Separate fixed layouts, no adjustable slider in POC.',
        '9 × 2.5 =22.5 kg; +1 ×1.25 =23.75 kg, not24.',
        'Heavy top-lift: grounded bag, two grips, rig-test first.',
    ]):
        s.text(470,890+i*25,line,'sm')
    s.notes(1060,70,'BACKPACK — BIG PACK',[
        (None,'30 kg complete mass ceiling; start lighter. Hand carry first; worn mode is secondary, not primary rucking.'),
        (1,'360 W × 500 H × 190 D body. Carrier 307 × 322 × 66. Old 310-wide bag / 300-high zone did not allow finished parts and frame.'),
        (2,'Low vs fixed mid-low is a PROPOSAL comparison, not a selected position. Compare hand tilt and shoulder pressure at equal total mass.'),
        (3,'Back-to-front: 18 pad/frame + 78 bay + 4 barrier + 12 gap + 37 sleeve + 41 main/front =190. Gap includes 6 replaceable pads, 6 free.'),
        (4,'Portrait laptop sleeve clear 260 W × 370 H × 25 D; padded outer 272 × 382 × 37. Bottom32: 14 base +6 pad +12 free gap.'),
        (5,'Suspend sleeve; test lateral and base impact with surrogate. No load transfer from carrier or frame to laptop.'),
        (6,'Stow harness for hand carry. Top-loading carrier path, zipped opening and retention need real-part insertion tests. Two lifting grips stow inside carrier envelope.'),
        (7,'Modular handle receivers and captive-bolt POC swaps. Double variant TBD. Handle location must be checked against actual loaded CoM, not guessed.'),
        (8,'Grid insert removable for compatible flat plates. Finished stack ≤53 incl. coating/separators; check actual SKU. Not every weight source reaches24 kg.'),
    ],width_chars=58)
    footer(s,'BIG PACK',2)
    return s


def weight_system():
    s=Sheet(); s.frame(); k=2
    q=G['laptop']; cl,cd,ch=q['cassette_outer_mm']; il,id_,ih=q['cassette_inner_mm']
    x,y=100,160
    s.rect(x,y,cl*k,cd*k,'pe')
    s.rect(x+8,y+8,il*k,id_*k,'of')
    for c in range(4):
        xx=x+(6+c*99)*k
        s.rect(xx,y+12,97*k,102*k,'wt',rx=3)
        s.text(xx+97,y+105,'97 × 102','sm','middle')
    s.dim_h(x,x+cl*k,y-30,str(cl),y)
    s.dim_v(y,y+cd*k,x-30,str(cd),x)
    s.view_label(x+cl, y+cd*k+45,'LAPTOP CASSETTE TOP — 1:2 AT A3')
    s.text(x+cl,y+cd*k+75,'398 cavity =4×97 +3×2 +2×2; depth106 =102 +2×2','sm','middle')

    # Physical stack at 2x: walls4, weight88, clamp4, reserve6, roof4.
    sx,sy=100,550
    s.rect(sx,sy,228,212,'pe')
    s.rect(sx+8,sy+8,212,196,'of')
    floor=sy+204
    for h in (35,35,18):
        floor-=h*k
        s.rect(sx+12,floor,204,h*k,'wt')
        s.text(sx+114,floor+h,'full ≤35' if h==35 else 'half ≤18','sm','middle')
    s.rect(sx+8,floor-8,212,8,'pe')
    s.dim_v(sy,sy+212,sx-30,'106 outer',sx)
    s.text(sx+114,sy-22,'4 clamp +6 reserve above stack','sm','middle')
    s.view_label(sx+114,sy+250,'END SECTION — 1:2')
    s.text(370,570,'Mass and finished dimensions are separate', 'lbl')
    for i,line in enumerate([
        'Core reference95 ×100 ×33 steel ≈2.461 kg before radii/coating.',
        'Nominal2.5 /1.25 kg targets: measure finished; tune core to suit.',
        'Finished full ≤97 ×102 ×35; half ≤97 ×102 ×18.',
        '4 ×(2.5 +2.5 +1.25) =25 kg, not24.',
        '23.75 kg example: 8 full +3 half; weigh actual whole bag.',
        '88 stack +4 clamp +6 reserve =98 inner height.',
        '7 sleeved bars ×12 =84 fit; 8×12 =96 do NOT fit.',
        'Lower stacks require secured spacers and clamp testing.',
    ]): s.text(370,602+i*27,line,'sm')

    # Handle options are explicitly symbolic, not dimensioned final geometry.
    s.text(100,900,'MODULAR HANDLE CONCEPT — NTS', 'lbl')
    receiver_handle(s,250,1030)
    s.path('M180,980 Q250,915 320,980','h')
    s.text(440,920,'Shared frame receivers: provisional140 centres', 'sm')
    s.text(440,947,'Fabric module (dashed) or standard rigid module', 'sm')
    s.text(440,974,'120 grip length; ≥45 knuckle clearance; trial30/35/40 grip', 'sm')
    s.text(440,1001,'Captive bolts; swap unloaded with tool; fastening details TBD', 'sm')
    s.text(440,1028,'DOUBLE WEIGHT HANDLE: MEANING / GEOMETRY TBD', 'lbl')

    s.notes(1060,70,'WEIGHT INTERFACE — SOURCE LIMITS',[
        (None,'One shared interface goal, two enclosure shapes. No universal-fit or universal24 kg claim. Complete bag ≤30 kg.'),
        (1,'Finished95 ×100 core coating allowance gives ≤97 ×102 footprint. 2 mm edge and intermodule gaps. Source limits in tech pack v0.2.'),
        (2,'Big Pack cavity299 ×314 ×58; 3×97 +2×2 +2×2 =299; 3×102 +2×2 +2×2 =314. 53 stack +4 clamp +1 reserve.'),
        (3,'Raw bar laptop380 ×100 ×10 ≈2.983 kg. Finished sleeve ≤384 ×104 ×12. Seven layers ≈20.88 kg steel; add sleeve tare.'),
        (4,'Big Pack raw285 ×100 ×10 ≈2.237 kg; sleeved ≤289 ×104 ×12. 2 rows ×4 layers =8 pieces, ≈17.90 kg steel. Three rows need320 high with gaps/edges; do not fit. Secure unused space.'),
        (5,'Shot theoretical upper bounds before shell losses: laptop13.7–17.8 kg, Big Pack18.4–23.9 kg at3.7–4.8 kg/L. Real capacity is lower.'),
        (6,'Water/sand much lighter. Long shells must fit cavity and stack including caps; nominal outside shell volume is not fill capacity.'),
        (7,'Ruck plate229 ×292 is a candidate Big Pack footprint, insert removed. Finished stack ≤53; sleeves/clamp included. Not every SKU fits.'),
        (8,'Small gym plates ≤150 diameter are Big Pack candidates only; confirm layout and stack. Laptop cavity depth106 cannot take them.'),
        (9,'Proposed supports, clamps, fasteners and coatings are untested. Low-stack spacers, sealed fillers and two-grip retention need POC validation.'),
    ],width_chars=58)
    footer(s,'WEIGHT SYSTEM',3)
    return s


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=SOURCE)
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,fn in [('1-laptop-bag',laptop_bag),('2-big-pack',big_pack),('3-weight-system',weight_system)]:
        out=args.output_dir/f'{name}.svg'
        out.write_text(fn().svg())
        print('wrote',out)
