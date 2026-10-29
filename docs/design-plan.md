# Product Design Plan

How we go from idea to a manufacturable first product. Phases overlap; the
gate at the end of each phase decides whether we move on.

## 1. Phases at a glance

| # | Phase | Main output | Gate |
| --- | --- | --- | --- |
| 0 | Discovery & research | Research summary, validated load range | Is there real demand? What load is right? |
| 1 | Requirements | Signed-off PRD v1 | Do we agree on what we're building? |
| 2 | Concept exploration | 3–5 weight-system concepts, 2–3 bag forms, scored | Pick 1–2 concepts to prototype |
| 3 | Rough prototypes | Hacked bags + test weights, walk tests | Does the core idea feel good on a real commute? |
| 4 | Engineering prototype | Sewn prototype on a frame, first bricks, durability tests at 30 kg | Passes durability tests; release mechanism works |
| 5 | Wear test | 10–20 people, 4 weeks of commuting | People keep using it |
| 6 | Manufacturing prep | Tech pack, supplier quotes, unit cost | Margin works at target price |
| 7 | Launch | Pilot run / pre-order campaign | — |

## 2. Phase 0 — Discovery & research

- **Competitor scan.** Rucking (backpacks + weight plates), weighted vests,
  weighted wrist/ankle gear, structured work bags. Note price points, weight
  formats, and how they secure and release weights.
- **Expert input.** A strength coach and a physiotherapist on: how users
  should build up to 30 kg, the carry-to-fatigue-then-switch protocol
  (about 10 min per side over a 20 min walk), risks (grip, shoulder, elbow,
  lower back), and what guidance to ship with the product.
- **User interviews (10–15).** Commute length and route (stairs, transit,
  crowds), what they carry today, where weights would live during the day,
  what would make them stop using it.
- **Quick survey / landing page** to test interest and price sensitivity.

## 3. Key design problems

### 3.1 The weights ("bricks")

The material sets how big the weight compartment must be:

| Material | Density (g/cm³) | Volume for 10 kg | Notes |
| --- | --- | --- | --- |
| Steel (coated) | ~7.9 | ~1.3 L | Compact; needs rubber/TPU coating to stop noise and damage |
| Cast iron (coated) | ~7.2 | ~1.4 L | Cheap to cast; same coating needs |
| Concrete / clay brick | ~1.8–2.4 | ~4.5 L | Cheap, available anywhere; dusty, abrasive, crumbles |
| Sand (sealed bag) | ~1.6 | ~6 L | Soft and quiet; bulky |
| Water (bladder/bottles) | 1.0 | 10 L | Can be poured out at the destination; very bulky |

**Takeaway:** 10 kg of steel fits in a tray about 38 × 12 × 3 cm — it
disappears into the bottom of a briefcase. 10 kg of real clay bricks fills
most of the bag. So the core product should use **dense, coated, standard
bricks**, with "bring your own weight" (real bricks, water bottles) as a
possible budget option to explore, not the default.

### 3.2 Where the weight goes

- **Bottom tray** — lowest centre of mass, most stable, easy to centre under
  the handle. Raises the bag floor a little. _Leading candidate._
- **Side panel** — keeps the bottom free; risks tilting the bag unless the
  handle is offset to match. Worth testing as a variant.
- Either way: centred front-to-back and side-to-side under the handle.

### 3.3 Quick drop and replace — concept directions

| Concept | How it works | Strengths | Risks |
| --- | --- | --- | --- |
| A. Drawer / cassette | All bricks sit in a rigid tray that slides out of an end hatch | One-motion drop; tray doubles as a carry/storage unit | Hatch and rails add cost and weight |
| B. Bottom flap | Zipped or buckled bottom panel opens to release a brick pouch | Simple, soft-goods only | Dropping weights by accident; zip under heavy load |
| C. Rail / clip-in bricks | Each brick clips into a rail on the bag floor or side | Fine-grained adjustment, no rattle | Many small mechanisms; slower full drop |
| D. Pocketed sleeve | Fabric sleeve with brick-sized pockets, pulls out by a handle | Cheap, light, easy to sew | Less rigid; bricks can shift |
| E. Bring your own | Lined, washable compartment that fits standard bricks/bottles | No weights to sell; low price | Bulky, dirty, inconsistent weight |

Concepts will be scored (Pugh matrix) against: drop speed, safety
(accidental release), rattle, compartment volume, cost, durability, looks.

### 3.4 Handle and carry ergonomics

The recommended carry is one hand until fatigue, switch, repeat — up to
30 kg total. So **grip is the limiting factor**, and the handle is the most
important part of the bag to get right.

- Rigid handle directly over the centre of mass, so the bag hangs straight
  in either hand.
- Fully symmetric: same balance and feel left or right, either face against
  the leg. Switching hands mid-stride should take a second.
- Test grip diameters (about 25–35 mm), shapes and wraps at 30 kg: a thicker
  handle spreads pressure but tires the grip faster.
- Handle stays put (doesn't flop or rotate), so the free hand can grab it
  during the switch.
- Slim bag profile so it clears the leg.
- Shoulder strap for non-training moments.

### 3.5 Durability: frame and fabric (critical goal)

The bag is rated for **30 kg**. Two layers of protection:

1. **The frame carries the load.** Handle → frame → weight compartment. The
   fabric is a skin over the frame, not the structure.
2. **The fabric could carry it anyway.** If the frame cracks or a joint
   loosens, the fabric and seams alone still hold 30 kg, so weights never
   drop.

**Frame options:**

| Option | Strengths | Weaknesses | Best for |
| --- | --- | --- | --- |
| Aluminium (6061-T6 tube or bent sheet) | Strong and stiff for its weight; easy to make in small numbers, no tooling | Can dent or bend permanently; joints need care; conducts cold | Prototypes and first production run |
| Glass-filled nylon (moulded, e.g. PA6-GF30) | Tough, doesn't dent, complex shapes in one part, cheap per unit | Expensive mould tooling; can creep under constant load | Volume production |
| HDPE / polypropylene frame sheet | Cheap, light, used in backpacks, survives impact | Flexible — needs ribs or a metal stay to stop sagging at 30 kg | Side and back panels, combined with metal stays |
| Carbon fibre | Lightest and stiffest | Costly; brittle on sharp impact | Premium edition later, if ever |

Working plan: prototype with an **aluminium frame + HDPE panels**, then
decide whether moulded glass-filled nylon pays off at production volume.

**Fabric and construction options:**

| Element | Candidates |
| --- | --- |
| Outer shell | 1000D–1680D high-tenacity / ballistic nylon; Cordura-class fabrics; laminated sailcloth (X-Pac class); full-grain leather for a premium line |
| Weight compartment lining | Heavy coated nylon or TPU-coated fabric; replaceable slide plate under the tray |
| Thread and stitching | Heavy bonded nylon or polyester thread; bar-tacks and box-X stitching at every load point |
| Webbing and handle core | Nylon or polyester webbing anchored to the frame; handle bolted or riveted to the frame, not just sewn |
| Hardware | Metal (aluminium or steel) buckles, D-rings and fasteners on the load path |
| Base | Reinforced base panel with protective feet |

**Brick volume:** 30 kg is the total, including bag, laptop and contents,
so the bricks top out at about 24 kg. In steel that's about 3 L — a tray of
roughly 38 × 12 × 7 cm. The frame and compartment need to fit this without
making the bag bulky.

### 3.6 Safety

- Rigid divider between weights and laptop.
- Ship with clear carry guidance: start light and build up toward 30 kg
  over weeks; carry to fatigue, then switch hands; keep alternating; stand
  tall and don't lean away from the bag.
- Have a strength coach / physio review the guidance and the build-up plan.

## 4. Prototyping and testing

**Phase 3 — rough prototypes (cheap and fast):**
- Take 2–3 existing briefcases/totes. Add weights (sandbags, steel plates,
  bottles) at the bottom vs. side. Walk the real commute.
- Follow the recommended carry (one hand to fatigue, switch, repeat) at
  several loads up to 30 kg.
- Measure: how much the bag swings, time per hand before switching, number
  of switches per walk, how easy the switch is, comfort rating, how the bag
  looks and sounds.
- Mock up concepts A–E in cardboard/foam to time the weight drop.

**Phase 4 — engineering prototype:**
- Sewn prototype with the chosen weight system.
- First brick samples (3D-printed shell + steel shot, then real coated steel).
- Durability tests at the 30 kg rating:
  - **Static pull:** handle and every load-bearing attachment held at
    3× load (90 kg) — no failure.
  - **Fatigue:** lift-and-carry cycling at 30 kg, at least 10,000 cycles
    (about 5 years of commutes, counting hand switches) — no seam, frame or
    handle damage.
  - **Fabric-only test:** frame removed or disconnected, 30 kg load —
    fabric and seams hold.
  - **Drop test:** loaded bag dropped onto concrete from desk height and
    on its corners — frame, base and weight tray intact.
  - **Fabric lab tests:** abrasion (Martindale), tear and tensile strength,
    water resistance.
  - **Creep:** 30 kg hung for days (and warm conditions) — no lasting sag,
    especially for plastic frames.
  - **Tray wear:** brick tray slid in and out thousands of times — lining
    and runners still work.

**Phase 5 — wear test:**
- 10–20 commuters, 4 weeks, weekly short survey + exit interview.
- Track: days carried with weights, total load used and how it builds over
  the weeks, time per hand and switches per walk, drop/replace friction,
  failures, any pain or injury.

## 5. Risks

| Risk | Mitigation |
| --- | --- |
| Injury from too much load or poor form | Expert-set load range, start-light guidance, small increments |
| Weights fall out or damage the laptop | Two-step release, rigid divider, testing |
| Bag looks or sounds "gym", not "office" | Design early with the look in mind; coated, rattle-free bricks |
| Heavy shipping cost for weights | Sell bricks separately or ship from a regional warehouse; explore BYO option |
| Handle, stitching or frame fails under 30 kg over time | Frame load path, fabric able to hold the load alone, 3× safety factor, fatigue and creep testing |
| Frame makes the bag heavy or bulky | Light alloys or glass-filled nylon; tune frame against the empty-weight target |
| Name "Heavy Bag" collides with boxing heavy bags (search, trademark) | Brand/name check in Phase 0 |

## 6. Immediate next steps

1. Answer the open questions in [`decisions.md`](decisions.md).
2. Competitor scan and expert interviews (Phase 0).
3. Build the first rough prototype from an existing bag and walk it to work
   for a week.
