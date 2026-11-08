# Tech pack — provisional packaging revision v0.2

**Product-design / POC only. Not engineering validated, not fabrication-ready.**
All dimensions mm. Coordinate order is explicit below. No purchase or supplier
outreach is authorized by this document. Current SVG, PNG and PDF
exports have been regenerated from the current sketch generator. Central envelope values:
[`geometry.json`](../design/sketches/geometry.json).

## 1. Intent and mass budget

Laptop bag and Big Pack for **office workers who lift heavy**. Start light;
**30 kg maximum complete mass**, not a training destination or added-weight
rating. Complete mass includes frame, empty enclosure, handle module, clamps,
liners, laptop and all contents. ≤2.5 kg empty is an unproven stretch target.

Example: 30 − 2.5 empty bag − 2 laptop − 1.5 other contents = **24 kg** added
weight allowance. Weigh actual assemblies; a 2.1 kg laptop or heavier handle
reduces this allowance. Physical fit does not prevent overload.

## 2. Weight and enclosure envelope arithmetic

### Own bricks: core is not finished size or guaranteed mass

- Initial steel core reference 95 × 100 × 33. At 7,850 kg/m³ this is
  **2.461 kg** before edge radii, machining and coating, not guaranteed 2.5 kg.
- Nominal targets: 2.5 kg full, 1.25 kg half, **measured finished**. Agree mass
  tolerance with the maker. A sharp, uncoated rectangular core needs about
  33.52 mm thickness for 2.5 kg before radius/coating effects; tune cores only
  while staying inside the finished envelope. If that cannot be achieved,
  revise envelope or mass target, not the label.
- Finished maximum including coating and tolerances: full **97 × 102 × 35**;
  half **97 × 102 × 18**. This provisionally reserves up to 1 mm per face on
  the footprint; coating thickness and process still need specification.
- Grid allocation: 2 mm edge clearance each side and 2 mm between modules.
  These are provisional insertion allowances, not machining tolerances.

| Assembly | Outer | Clear cavity | Stack / clamp allowance |
| --- | --- | --- | --- |
| Laptop 4 × 1 cassette, L × D × H | 406 × 114 × 106 | 398 × 106 × 98 | 88 stack + 4 clamp + 6 compression/hardware reserve |
| Big Pack 3 × 3 carrier, W × H × D | 307 × 322 × 66 | 299 × 314 × 58 | 53 stack + 4 clamp + 1 compression reserve |

Walls/floor/lid allowance = 4 mm per face for packaging, not specified
structural thickness. Clamp fittings/straps and folded grips must stay within
outer envelopes. Low stacks use secured spacers: do not imply the plate has
88 mm of unsupported clamping travel. Test contact pressure and retention.
The Big Pack's 1 mm reserve is tight; increase enclosure depth if real hardware
cannot fit, rather than cutting the brick or coating allowance silently.

- Laptop length: **4×97 + 3×2 + 2×2 = 398**; depth 102 + 2×2 = 106.
- Big Pack width: **3×97 + 2×2 + 2×2 = 299**; height
  **3×102 + 2×2 + 2×2 = 314**. Add 8 total wall allowance → 307 × 322.
- A 380 mm cavity for 4×95 or 285 mm cavity for 3×95 had **zero** nominal
  clearance even before coating. Those v0.1 cavity dimensions are superseded.
- Two full and one half finished brick: 35+35+18 = **88** high, inside laptop
  stack space, but 2.5+2.5+1.25 = **6.25 kg per module**, ×4 = **25 kg**.
  That fits spatially but exceeds the illustrative 24 kg allowance.
- Illustrative allowed laptop loading: eight full + three half = **23.75 kg**
  nominal, one module has no half. Restrain the asymmetric partial load.
- Big Pack: nine full = **22.5 kg**; add one half = **23.75**, not 24. Maximum
  local stack is 35+18 = 53. More halves may fit physically and overload the
  bag. Label and weigh the entire bag, including the carrier and all adapters.

## 3. Bodies, insertion bays and laptop protection

| | Laptop bag | Big Pack |
| --- | --- | --- |
| External body W × H × D | 440 × 430 × 150 | 360 × 500 × 190 |
| Clear enclosure bay | 414 L × 122 D × 110 H | 319 W × 334 H × 78 D |
| Insertion clearance | 4 at each L/D face, 2 at top/bottom | 6 each face |
| Laptop clear sleeve W × H × D | 370 × 260 × 25 | **260 × 370 × 25**, portrait |
| Padded sleeve outer W × H × D | 382 × 272 × 37 | 272 × 382 × 37 |

Laptop bag width stack: 406 cassette + 8 insertion + 26 combined end-frame /
textile allowance = 440. Reserve 13 each end (candidate stay 5 thick + 8 textile /
seam); depth 114 + 8 insertion + 28 front/back allowance = 150. **Clear hatch
opening 118 D × 110 H minimum**, measured after zip/lining intrusion: leaves
2 per face around 114 × 106 cassette. End stays/bridge must route around the
hatch; no cross-member through the extraction path. Reinforce and test the
load detour. Body height from base upward:

1. Base/cradle allowance 10; cassette top 116.
2. 4 head clearance (bay starts 8, ends 118; 2 more to barrier) → barrier
   underside 120; 4 HDPE barrier → top 124.
3. Replaceable impact pads 6 → top 130.
4. **12 free gap above the pads** → suspended sleeve bottom 142.
5. Sleeve outer height 272 → top 414; 16 top/access allowance → body 430.

Attach suspension straps at reinforced upper structure with no weight load
through sleeve. The free gap must survive suspension stretch and impacts;
pads catch overtravel without a hard strike. This stack-up is only unloaded
packaging. Test with a 356 × 248 × 17 surrogate before a real laptop.

Big Pack width: 307 carrier + 12 insertion + **41 side structure/textile** =
360 (20.5 each side: reserve 12 for stay packaging + 8.5 textile/seams). Bay
height 334 exceeds carrier 322 by 12, unlike the old 300 mm zone. Proposed
carrier bottom **36 above base (low)** or **66 (mid-low)**, top respectively
358 / 388; surrounding bay 30–364 or 60–394. Both fit within the 500 body.
These are separate fixed-mount POC layouts, not a sliding adjustment mechanism.

Big Pack depth from back: **18 padding/frame + 78 carrier bay + 4 rigid
barrier + 12 lateral isolation space + 37 padded laptop sleeve + 41 main/front
allowance = 190**. Pads replaceable on barrier within that lateral gap;
6 mm pads leave 6 free lateral space. Portrait sleeve bottom 32 above base;
base stop top 14 + 6 impact pad + 12 free vertical gap = 32. Sleeve top 414,
leaving 86 for access/suspension. Test lateral and base impacts; frame must
not bypass isolation. Everyday-volume and access claims await mock-ups.

## 4. Source-specific capacity — never “24 kg from any source”

All examples include no sleeve/container mass unless stated; weigh that mass
as well. Bulk density, shell wall thickness and closures reduce capacities.
Two bags share the interface goal, not the same cassette geometry.

| Source | Laptop bag | Big Pack |
| --- | --- | --- |
| Own nominal steel bricks | 20 kg: 8 full in two layers; 23.75 kg: 8 full + 3 half example | 22.5 kg: 9 full; 23.75: 9 full + 1 half example |
| 100 × 10 raw steel bar, 7,850 kg/m³ | 380 length ≈2.983 kg each; sleeved ≤384 × 104 × 12; **7 layers =84 mm, ≈20.88 kg steel**; 8 layers =96 fails 88 stack | 285 length ≈2.237 kg each; sleeved ≤289 × 104 × 12; **2 rows × 4 depth layers =8 pieces ≈17.90 kg steel** (214 row span incl. 2 gap +4 edges, 48 depth); 3 rows need 320 height with 2 mm gaps/edges and do not fit; secure unused space |
| Shot-filled sealed shells | Absolute cavity bounding volume at 88 stack: 3.713 L; loose shot 3.7–4.8 kg/L gives **13.7–17.8 kg theoretical fill**, less after walls, gaps, closures | At 53 stack: 4.976 L; same density → **18.4–23.9 kg theoretical fill**, less after shells/closures; no promised 24 kg |
| Sand / water shells | Same 3.713 L geometric upper bound: ~5.9 kg sand at 1.6 kg/L or ~3.7 kg water, before shell losses | 4.976 L: ~8.0 kg sand / ~5.0 kg water before losses |
| Ruck plates | Not supported in this narrow cavity | Candidate 229 × 292 footprint inside 299 × 314 after grid insert removal; **finished thickness incl. sleeves ≤53**, clamped; inspect actual plate, no universal standard fit |
| Small gym plates | Not supported (106 clear depth) | Candidate ≤150 diameter flat in empty cavity; maximum finished stack 53 incl. separators; layout and rating per actual SKU, not automatic 24 kg |

Long shells must stay inside 398 × 106 × 88 (laptop) or 299 × 314 × 53
(Big Pack); a nominal 380 × 100 shell body is not usable fill volume.
Sealed fillers need leak and rattle tests; no loose sand/water in the tray.

## 5. Structure, modular handles and construction

- 6061-T6 frame bridge, stays and cradle; HDPE barriers/shape panels; profiles,
  joint design, fasteners and thicknesses selected after structural review.
- Shared frame receivers, provisional **140 mm centres**, for fabric or standard
  rigid handle. Rigid POC has 120 usable grip length, 30/35/40 grip trials and
  ≥45 clear knuckle space. Receiver pitch is an initial fixture dimension,
  not a claim that commercial off-the-shelf handles fit it.
- Fabric grip still bolts through structural end fittings to the same
  receivers; not sewn-only. Each complete module must pass the same tests.
- Captive bolts for POC: final diameter, edge distance, thread engagement,
  torque, anti-loosening and inspection marks TBD. Swap only unloaded using
  a tool. No quick-release or permanently riveted replaceable modules.
- **Double weight handle: requested variant, meaning and geometry TBD**. Do
  not assume two-hand, two grips, a thicker grip or any load multiplier.
- Heavy Core nylon, lighter lining, reinforced seams, backup load webbing,
  metal load hardware, protective feet, abrasion liner and replaceable runners.
- Stowable backpack harness; detachable laptop-bag shoulder strap. Keep all
  straps clear of receivers, knuckles, hatch and extraction support.

## 6. Extraction and backpack placement — proposals only

**A. Supported single cassette (recommended for comparison, not decided):**
set bag on stable level support at hatch height; slide onto an adjacent stable
surface/platform, never pull the suspended heavy tray one-handed. Two stowable
lifting grips, positive travel stop before loss of runner support, and a
separate deliberate final release only after support is established. Check
pinch zones, tipping, rail friction, zip opening and reseating/lock indication.
Budget ≥450 clear support length for the 406 tray plus finger space; determine
support strength and geometry in the POC. No unsupported cantilever at full load.

**B. Two smaller cassettes:** compare lower lift mass against extra walls,
clamps, releases and loading errors; breaks continuous long-bar compatibility
unless redesigned. No frozen split dimensions or automatic approval.

Big Pack remains top-loading. Do not lift a 23.75 kg carrier by an untested
pull loop: two grips, grounded bag, progressive supported rig tests; if human
removal is not controlled, revise the enclosure/handling method before freezing.

**Placement comparison:** low vs fixed mid-low, both close to the back. Check
hand-carry tilt, back/shoulder pressure, harness stow and laptop/main access
with equal total mass. Do not assert low is best for worn comfort.

## 7. POC tests before supplier-ready drawings

Use fit gauges including finished coating, runners, folded grips, zip intrusion
and worst-case tolerances. Record empty assembly mass with each handle.
Start unloaded/submaximal; heavy proof tests on an engineered rig, not a person.

| Test | Proposed target / evidence; not an achieved result |
| --- | --- |
| Handle modules / joints | Engineer-reviewed 90 kg-equivalent static proof and 10,000 lift cycles up to 30 kg; all supported modules; no pull-out, loosening or permanent set |
| Backup textiles | Controlled frame-disconnected containment at 30 kg |
| Retention / extraction | Empty, partial, highest permitted load; travel stop, deliberate release and reseat; no unintended exit, tip or pinch; record time rather than impose 10 s |
| Wear / creep | 2,000 removal cycles; 72 h hang up to 30 kg after rig review; no unsafe wear or lasting sag |
| Laptop isolation | Instrumented surrogate, agreed desk-height / corner drops; no hard bottom-out, intrusion or release; define acceptable acceleration before testing |
| Balance / comfort | Both hands; each handle; low/mid-low Big Pack layouts; comfortable human loads only after structural screening |
| Fill / coating | Seal leakage, abrasion, low-stack rattle, actual mass, closure clearance |

After design choices settle, prepare a parts and sample order (Israel or
abroad). Marketing, ads/Kickstarter, market proof, legal and shipping studies
remain deferred. No manufacturing release until unresolved fits, structure,
handle fasteners and test protocols are reviewed with the sample maker.
