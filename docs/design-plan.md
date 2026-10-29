# Product Design Plan

How we go from idea to a manufacturable first product. Phases overlap; the
gate at the end of each phase decides whether we move on.

## 1. Phases at a glance

| # | Phase | Main output | Gate |
| --- | --- | --- | --- |
| 0 | Discovery & research | Research summary, validated load range | Is there real demand? What load is right? |
| 1 | Requirements | Signed-off PRD v1 | Do we agree on what we're building? |
| 2 | Concept exploration | 3–5 weight-system concepts, backpack + laptop bag concepts, scored | Pick 1–2 concepts to prototype |
| 3 | Rough prototypes | Hacked bags + test weights, walk tests | Does the core idea feel good on a real commute? |
| 4 | Engineering prototype | Sewn prototypes on a frame, first weights, durability tests at 30 kg | Passes durability tests; release mechanism works |
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
- **Name check.** Desk research done:
  [`research/name-check.md`](research/name-check.md). The founder keeps
  "Heavy Bag". Next: verify trademarks, domains and handles directly, then
  attorney clearance; fall back to a close alternative if it's blocked.
- **Weight sourcing.** Done (desk research):
  [`research/weights-exploration.md`](research/weights-exploration.md); see
  §3.2.

## 3. Key design problems

### 3.1 Product line: backpack and laptop bag

Two bags at launch, **one shared weight system** — the same weights fit both,
so a customer who owns both bags only buys weights once.

**Laptop bag** (briefcase-style)
- Top handle on a rigid bridge, directly over the weight tray.
- Weight tray in the base, under a rigid false floor; laptop sits above it.
- Detachable shoulder strap for non-training moments.

**Backpack**
- The suitcase carry is still the core exercise: a rigid **top handle**
  built for long one-hand carries, not a thin grab loop.
- Weights sit in a **sleeve along the back panel**, low and between the frame
  stays. The top handle is mounted right above that sleeve, so the bag hangs
  straight in the hand. When worn, the weight is close to the spine, which
  is the comfortable place for it.
- Shoulder straps tuck away behind a zipped panel during the carry, so
  nothing dangles or snags when switching hands. Worn as a backpack, it's a
  rest mode — or a second, rucking-style workout.

**Sizing (starting dimensions, to confirm with mock-ups)**

Both bags must fit a **16" MacBook Pro** (about 35.6 × 24.8 × 1.7 cm,
~2.1 kg) plus weights plus everyday things (charger, notebook, lunch,
jacket layer).

| | Laptop bag | Backpack |
| --- | --- | --- |
| External size (W × H × D) | ~42 × 40 × 13 cm | ~31 × 48 × 16 cm (~24 L) |
| Laptop sleeve (internal) | ~37 × 26 × 2.5 cm, padded, above the false floor | ~37 × 26 × 2.5 cm, padded, in front of the weight sleeve |
| Weight space | Base tray band ~38 × 11 × 9 cm (~3.8 L) | Back-panel sleeve ~28 × 30 cm, up to ~6 cm thick |
| Space for other things | Main compartment ~8 L + front pocket | Main compartment + front pocket |
| Weight sources at full 24 kg | Our steel, local steel bar (~7–8 cm stack) | All sources, incl. ruck plates and shot |
| Weight sources capped | Steel-shot cassettes ~16 kg; gym plates on edge don't fit (they need ~14 cm) | — |

**Why a 9 cm base, not 14 cm:** a 14 cm base makes the laptop bag ~45 cm
tall — closer to a tote, heavier and harder to keep clear of the leg. With
9 cm, the slim dense options (our steel, steel bar) still reach the full
24 kg, shot reaches ~16 kg, and anyone who wants plates or 24 kg of shot
has the backpack. The backpack's layout, from the spine outward: frame
sheet → weight sleeve → laptop sleeve → main compartment.

Check in mock-ups (experiment E7): leg and stair clearance for shorter
users with a 40 cm-tall bag, and whether ~8 L is enough for everyday things.

### 3.2 The weights

The material sets how big the weight compartment must be:

| Material | Density (g/cm³) | Volume for 10 kg | Notes |
| --- | --- | --- | --- |
| Steel (coated) | ~7.9 | ~1.3 L | Compact; needs rubber/TPU coating to stop noise and damage |
| Cast iron (coated) | ~7.2 | ~1.4 L | Cheap to cast; same coating needs |
| Concrete / clay brick | ~1.8–2.4 | ~4.5 L | Cheap, available anywhere; dusty, abrasive, crumbles |
| Sand (sealed bag) | ~1.6 | ~6 L | Soft and quiet; bulky |
| Water (bladder/bottles) | 1.0 | 10 L | Can be poured out at the destination; very bulky |

10 kg of steel fits in a tray about 38 × 12 × 3 cm and disappears into the
bag; 10 kg of clay bricks fills most of it. Bricks top out at about 24 kg
(30 kg total minus bag, laptop and contents) — about 3 L in steel.

**Shipping problem.** Dense metal weights are the most compact, but
shipping a full 24 kg set costs an estimated $25–60 at scale, and more at
small-shipper rates. It also needs two or three parcels to stay under the
common 25 kg parcel limit. 25 options were explored in
[`research/weights-exploration.md`](research/weights-exploration.md). Main
findings:

- **Only metal, or metal-loaded fillers, fit 24 kg in a slim bag.**
  Concrete, bricks, sand and water top out around 8–12 kg — fine for
  beginners, not for the full range.
- **Users build up over time.** Nobody needs 24 kg on day one, so we can
  ship a little metal now and more later, or start on local filler.
- **Moulds rank lower than expected:** concrete is too light for more than
  ~10 kg, and casting is dusty and fiddly. Possible hobbyist accessory only.

**Decision: "One tray, any weight."** The bag sells a standard weight *interface*, not the weights. One
rigid, clamping tray (concept A below) takes many weight sources:

| Source | How it fits | Steps |
| --- | --- | --- |
| Fill-your-own cassettes (ship empty with the bag) | Identical sealed shells, filled locally with steel shot (~5 kg each), sand or water | ~1–5 kg |
| Local steel flat bar | Customer buys 100 × 10 mm (or × 5 mm) bar cut to 380 mm; we ship a quiet TPU sleeve | 3 / 1.5 kg |
| Standard 1" gym plates | "Toast-rack" tray insert holds plates on edge | 1.25 / 2.5 kg |
| Ruck plates (backpack) | Back sleeve sized to the common 22.9 × 29.2 cm ruck plate | 4.5 / 9 / 13.6 kg |
| Our own coated steel bricks (premium) | Native fit, marked, silent; sold in small "level-up" packs as users progress | 1.25 / 2.5 / 5 kg |
| Bricks or water ("budget mode") | Strapped into the open tray; lower maximum | 1–3.5 kg |

This cuts the default shipment from ~27 kg to ~3–8 kg per customer. One
clamping tray handles rattle, quick release and overload limits for every
source. The research doc lists nine validation experiments (shipping
quotes, rattle test, local-sourcing mystery shop, preference test, and
more).

Laptop-bag base height: set at ~9 cm (see §3.1 sizing). Full 24 kg with our
steel or steel bar; shot capped at ~16 kg; gym plates in the backpack only.

### 3.3 Where the weight goes

- **Laptop bag: bottom tray** — lowest centre of mass, most stable, easy to
  centre under the handle.
- **Backpack: back-panel sleeve** — low, between the frame stays, with the
  top handle mounted directly above it.
- Either way: centred under the handle, so the bag hangs vertically in either
  hand.

### 3.4 Quick drop and replace — concept directions

| Concept | How it works | Strengths | Risks |
| --- | --- | --- | --- |
| A. Drawer / cassette | All weights sit in a rigid tray that slides out of an end hatch | One-motion drop; tray doubles as a carry/storage unit | Hatch and rails add cost and weight |
| B. Bottom flap | Zipped or buckled bottom panel opens to release a weight pouch | Simple, soft-goods only | Dropping weights by accident; zip under heavy load |
| C. Rail / clip-in bricks | Each brick clips into a rail on the bag floor or side | Fine-grained adjustment, no rattle | Many small mechanisms; slower full drop |
| D. Pocketed sleeve | Fabric sleeve with brick-sized pockets, pulls out by a handle | Cheap, light, easy to sew | Less rigid; bricks can shift |
| E. Bring your own | Lined, washable compartment that fits standard bricks/bottles | No weights to sell; low price | Bulky, dirty, inconsistent weight |

The cassette (A), with a compression clamp, is the favourite: it is the
"one tray, any weight" interface from §3.2, and one tray shape could slide
into the laptop bag's base and the backpack's back sleeve. Bring-your-own
(E) folds into it as the budget mode. Concepts will be scored (Pugh matrix) against: drop
speed, safety (accidental release), rattle, volume, cost, durability, looks,
and fit in both bags.

### 3.5 Handle and carry ergonomics

The recommended carry is one hand until fatigue, switch, repeat — up to
30 kg total. So **grip is the limiting factor**, and the handle is the most
important part of both bags.

- Rigid handle directly over the centre of mass, so the bag hangs straight
  in either hand.
- Fully symmetric: same balance and feel left or right, either face against
  the leg. Switching hands mid-stride should take a second.
- Test grip diameters (about 25–35 mm), shapes and wraps at 30 kg: a thicker
  handle spreads pressure but tires the grip faster.
- Handle stays put (doesn't flop or rotate), so the free hand can grab it
  during the switch.
- Slim profile so the bag clears the leg.

### 3.6 Frame (decision: hybrid aluminium + HDPE)

The bag is rated for **30 kg**, with two layers of protection:

1. **The frame carries the load.** Handle → frame → weight compartment. The
   fabric is a skin over the frame, not the structure.
2. **The fabric could carry it anyway.** If the frame cracks or a joint
   loosens, the fabric and seams alone still hold 30 kg, so weights never
   drop.

**Options considered:**

| Option | Strengths | Weaknesses | Role |
| --- | --- | --- | --- |
| Aluminium 6061-T6 (tube, flat bar, bent sheet) | Strong and stiff for its weight; easy to bend and make in small numbers, no tooling | Can dent or bend permanently; joints need care | **Load-carrying spine** |
| HDPE frame sheet | Cheap, light, proven in backpacks, survives impact | Flexible; sags at 30 kg without metal support | **Shape and protection panels** |
| Glass-filled nylon (moulded, e.g. PA6-GF30) | Tough, complex shapes in one part, cheap per unit | Expensive moulds; creeps under constant load | **Later:** handle mounts, tray, joints at volume |
| 7075 aluminium | Stronger than 6061, so thinner stays | Pricier, harder to bend | Fallback if 6061 is too heavy |
| Carbon fibre | Lightest and stiffest | Costly; brittle on sharp impact | Not planned |

**Decision.** A **6061-T6 aluminium spine carries the load**, and **HDPE
sheets give shape and protect the contents**:

- **Laptop bag:** an aluminium U-frame — the handle bridge on top, a stay
  down each end panel, joined by the weight-tray cradle at the bottom. HDPE
  sheets stiffen the front and back walls; a rigid false floor separates the
  laptop from the weights.
- **Backpack:** two aluminium stays in the back panel (standard backpack
  construction), joined at the top by the handle bridge and at the bottom by
  the weight cradle. An HDPE frame sheet sits between them, and the weight
  sleeve rests against it.
- **Handle:** bolted or riveted to the aluminium bridge, never just sewn.

Why not all-plastic now: plastic creeps under a constant 30 kg, and moulds
are a big up-front cost before the design is settled. Once the design is
stable, moulded glass-filled nylon parts (handle mounts, cradle, joints) can
cut weight and cost at volume.

### 3.7 Fabric and construction (decision: several fabric options, one structure)

**Every bag has the same hidden structure** — frame, load webbing, heavy
stitching, metal hardware, abrasion-resistant weight-compartment lining.
The outer fabric is a choice of look and feel. Every option must pass the
same 30 kg durability tests.

**Outer fabric options:**

| Line | Outer fabric | Character | Trade-offs |
| --- | --- | --- | --- |
| **Core** (launch) | 1680D ballistic nylon, or 1000D Cordura-class nylon | Classic, extremely tough, office-appropriate | Heavier than modern laminates; best durability per cost |
| **Tech** | Laminated sailcloth (X-Pac class) or UHMWPE / Dyneema-blend fabric | Modern, lighter, highly water-resistant | Higher cost; UHMWPE fabrics are the priciest |
| **Heritage** (premium) | Full-grain leather, or waxed canvas with leather trim | Premium, ages well | Heavier; needs care; leather relies fully on the internal structure |

Recommendation: launch with **Core** in two or three colours, test **Tech**
and **Heritage** as samples in the wear test, and add lines after launch.

**Shared construction:**

| Element | Spec |
| --- | --- |
| Weight-compartment lining | Heavy TPU-coated nylon; replaceable slide plate under the tray |
| Thread and stitching | Heavy bonded nylon or polyester thread; bar-tacks and box-X stitching at every load point |
| Load webbing | Nylon or polyester webbing anchored to the frame, as the fabric-only backup load path |
| Hardware | Metal (aluminium or steel) buckles, D-rings and fasteners on the load path |
| Base | Reinforced base panel with protective feet |

### 3.8 Safety

- Rigid divider between weights and laptop.
- Ship with clear carry guidance: start light and build up toward 30 kg
  over weeks; carry to fatigue, then switch hands; keep alternating; stand
  tall and don't lean away from the bag.
- Have a strength coach / physio review the guidance and the build-up plan.

## 4. Prototyping and testing

**Phase 3 — rough prototypes (cheap and fast):**
- Take an existing laptop bag and backpack. Add weights (sandbags, steel
  plates, bottles) in the base vs. the back panel. Walk the real commute.
- Follow the recommended carry (one hand to fatigue, switch, repeat) at
  several loads up to 30 kg.
- Measure: how much the bag swings, time per hand before switching, number
  of switches per walk, how easy the switch is, comfort rating, how the bag
  looks and sounds.
- Mock up concepts A–E in cardboard/foam to time the weight drop.

**Phase 4 — engineering prototype:**
- Sewn prototypes of both bags on the aluminium + HDPE frame, with the chosen
  weight system.
- First weight samples (3D-printed shell + steel shot, then the chosen
  production approach).
- Durability tests at the 30 kg rating, for every fabric option:
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
  - **Creep:** 30 kg hung for days (and warm conditions) — no lasting sag.
  - **Tray wear:** weight tray slid in and out thousands of times — lining
    and runners still work.

**Phase 5 — wear test:**
- 10–20 commuters, 4 weeks, weekly short survey + exit interview.
- Track: days carried with weights, total load used and how it builds over
  the weeks, time per hand and switches per walk, drop/replace friction,
  failures, any pain or injury, and which fabric and bag style people prefer.

## 5. Risks

| Risk | Mitigation |
| --- | --- |
| Injury from too much load or poor form | Expert-set build-up plan, start-light guidance, small increments |
| Weights fall out or damage the laptop | Two-step release, rigid divider, testing |
| Bag looks or sounds "gym", not "office" | Brand look set early (see [`brand.md`](brand.md)); coated, rattle-free weights |
| Heavy shipping cost for weights | "One tray, any weight": ship empty cassettes and sleeves, support local steel and gym plates, sell our steel in small packs (§3.2) |
| Handle, stitching or frame fails under 30 kg over time | Aluminium load spine, fabric able to hold the load alone, 3× safety factor, fatigue and creep testing |
| Frame makes the bag heavy or bulky | 7075 fallback, moulded parts at volume; tune against the empty-weight target |
| Backpack straps get in the way of the hand carry | Stowable straps; test hand switches with the backpack |
| Name "Heavy Bag" is weak to protect and buried by boxing search results | Register a distinctive logo mark; own a clear domain; lead SEO with "commute" / "weighted work bag" terms; close alternatives ready (see name check) |

## 6. Immediate next steps

1. Verify "Heavy Bag" trademarks, domains and handles directly (needs
   registry access or a manual check), then attorney clearance.
2. Competitor scan and expert interviews (Phase 0).
3. Build the first rough prototypes from an existing laptop bag and
   backpack and walk them to work for a week — include a first clamping
   tray and test it with steel bar, shot cassettes and gym plates.
4. Cardboard mock-ups of both bags at the §3.1 sizes, with a 16" MacBook Pro
   inside.
