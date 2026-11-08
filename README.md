# Heavy Bag

Work bags for **office workers who lift heavy**: a laptop bag (working name
“Heavy Brief”) and backpack (“Big Pack”) with removable weights for one-hand
suitcase carries, and normal work-bag use without added weights.

**Start light. 30 kg is the maximum total carried mass, not a starting load,
not 30 kg of added weights, and not a goal every user should work toward.**
Total includes the bag, frame, empty cassette/carrier, selected handle, laptop,
weights and all other contents. These are design targets, not a tested rating.

## Current focus: product design and a POC

Settle the design, then prepare a parts/sample order in Israel or abroad.
Only after a satisfying product POC do ads or a Kickstarter campaign enter the
plan. Market proof, shipping economics and legal/trademark work are deferred;
US fitness brands shipping steel is not treated as a product-design blocker.
No sourcing orders or outreach are authorized by these design documents.

## Design direction

- Shared **weight interface**, not an identical cassette: laptop bag uses a
  4 × 1 tray; Big Pack a 3 × 3 carrier. “One tray, any weight” means supported,
  dimension-checked sources with their own capacities, not universal fit.
- Aluminium load spine and HDPE barriers; textile backup containment remains
  a test requirement, not a proven fail-safe.
- Frame-mounted receivers accept interchangeable **fabric** and **standard
  rigid weight handles**. POC swaps use captive bolts. A “double weight handle”
  is requested but its meaning/geometry remains TBD.
- A suspended laptop sleeve, replaceable impact pads and a free gap isolate
  the laptop from rigid weight structures. Drop-test with a surrogate first.
- **Proposals, not selected mechanisms:** a supported single-cassette slide-out
  versus two smaller cassettes; a low versus a fixed mid-low Big Pack position.
  Do not extract a heavy cassette one-handed while holding the bag.

## Provisional packaging

| | Laptop bag | Big Pack |
| --- | --- | --- |
| Body W × H × D, mm | 440 × 430 × 150 | 360 × 500 × 190 |
| Weight enclosure, mm | 406 × 114 × 106 (L × D × H) | 307 × 322 × 66 (W × H × D) |
| Usable weight stack, mm, excluding clamp | 88 | 53 |

These larger envelopes allow coating, gaps, frame/textile space and laptop
isolation; they are **not engineering validated**. Check leg clearance, laptop
access and useful everyday volume before freezing sizes. Source dimensions
are in [`geometry.json`](design/sketches/geometry.json), with the stack-up and
source limits in the [tech pack](docs/tech-pack.md).

Example mass budget only: 30 − 2.5 bag − 2 laptop − 1.5 contents = **24 kg**
of added weights. Weigh the actual complete bag; a physically fitting load can
still exceed the limit. Four stacks of 2.5 + 2.5 + 1.25 = **25 kg**, not 24;
use eight full and three half bricks = **23.75 kg** nominal in that example.

## Documents and drawings

- [Product requirements](docs/product-requirements.md)
- [Design and POC plan](docs/design-plan.md)
- [Tech pack and packaging arithmetic](docs/tech-pack.md)
- [Decisions and unresolved proposals](docs/decisions.md)
- [Concept SVG sheets](design/sketches/) and their generator
- [Brand notes](docs/brand.md) and [research archive](docs/research/): deferred,
  historical material, not current capacity specifications

Regenerate SVGs: `python3 design/sketches/make_sketches.py`.
Check packaging arithmetic: `python3 design/sketches/validate_geometry.py`.
The generator also accepts `--output-dir /absolute/scratch/path`.
SVG, PNG and PDF exports have been regenerated from the current sketch
generator. Rerun the generator and export step after future drawing changes;
see the sketch-folder README.
