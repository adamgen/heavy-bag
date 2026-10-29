# Product Requirements (v0 — draft)

Status: **draft**. Numbers marked _(hypothesis)_ are starting points to be
validated in research and prototyping, not commitments.

## 1. Target users

- **Primary — the walking commuter.** Office worker who walks 10–30 minutes
  each way (or walks to/from transit), wants to get stronger, and is short on
  time.
- **Secondary — the fitness-minded professional.** Already trains, knows what
  a suitcase carry or ruck is, and wants to add volume through the day.

## 2. Product line

- **R-P1** Two bags at launch: a **backpack** and a **laptop bag**.
- **R-P2** Both share one weight system: the same weights fit both bags.
- **R-P3** Backpack: rigid top handle for the suitcase carry, mounted above
  the weight sleeve; shoulder straps stow away during the carry.
- **R-P4** Laptop bag: rigid top handle above the weight tray, plus a
  detachable shoulder strap.
- **R-P5** Each bag is offered in several outer fabrics on one shared
  internal structure (see design plan §3.7).

## 3. Recommended carry

- Total carried load: **up to 30 kg**, including the bag, laptop, contents
  and weights. Users build up to this over time.
- Carry in one hand until the grip or core fatigues, then switch hands, and
  keep alternating.
- A typical 20-minute walk is about 10 minutes per side, split into several
  bouts.

## 4. Use cases

| ID | Use case |
| --- | --- |
| UC-1 | Walk to work carrying the loaded bag in one hand until it fatigues, then switch hands; alternate for the whole walk. |
| UC-2 | Arrive at work, pull the weights out in one motion, leave them under the desk or in a locker, and use the bag normally during the day. |
| UC-3 | Before going home, put the weights back in (or don't — light day). |
| UC-4 | Add or remove one brick to change the load (progression, tired day, injury). |
| UC-5 | Mid-walk, decide the load is too much and drop weights quickly. |
| UC-6 | Use the bag as a normal work bag with no weights at all. |

## 5. Functional requirements

### Weight system
- **R-W1** Holds added weight in a dedicated compartment, physically separated
  from the main (laptop) compartment.
- **R-W2** Adjustable in increments of 1–2.5 kg _(hypothesis)_.
- **R-W3** Designed to be carried at up to 30 kg in total: bag, laptop,
  contents and weights together. With a 2.5 kg bag, ~2 kg laptop and ~1.5 kg
  of other contents, that leaves room for **up to ~24 kg of bricks**.
- **R-W10** The weight compartment holds no more bricks than fit within the
  30 kg total with typical contents, so it's hard to overload by accident.
- **R-W4** All weights can be removed together in one motion, in under
  10 seconds, without tools _(hypothesis)_.
- **R-W5** A single brick can be added or removed without removing the others.
- **R-W6** Weights cannot fall out by accident: release needs a deliberate
  action (for example, a two-step release).
- **R-W7** Weights don't shift, slide or rattle while walking.
- **R-W8** Weight compartment sits low and centred under the handle: a
  base tray in the laptop bag, a back-panel sleeve in the backpack.
- **R-W9** The removed weights are easy to carry and store as a unit (for
  example, a tray or pouch with its own grip).

### Bag & carry
- **R-B1** A top handle designed for one-handed suitcase carry: rigid, sits
  over the centre of mass, comfortable diameter for a long hold.
- **R-B2** The loaded bag hangs vertically and stays clear of the leg while
  walking.
- **R-B9** Symmetric carry: the bag balances and feels the same in either
  hand, and switching hands is quick and natural mid-walk (no strap to
  untangle, no "right way round").
- **R-B3** Load path runs from the handle through the frame to the weights —
  not through decorative fabric panels.
- **R-B4** Handle and attachment points rated to at least 3× maximum loaded
  weight, i.e. ≥ 90 kg static _(hypothesis; set the final factor with the
  manufacturer)_.
- **R-B5** Protected laptop sleeve (fits 14"–16" laptop _(hypothesis)_).
- **R-B6** Professional look, suitable for an office.
- **R-B7** A way to carry the bag without training: shoulder strap on the
  laptop bag, stowable shoulder straps on the backpack.
- **R-B8** Empty bag weight ≤ 2.5 kg including the frame _(hypothesis; the
  frame makes the original 2 kg target tight)_.

### Durability (critical)
- **R-D1** Internal frame carries the load from handle to weight
  compartment: an aluminium (6061-T6) load spine with HDPE panels for shape
  (see design plan §3.6).
- **R-D2** Bag carries 30 kg in daily use without tearing, seam failure,
  permanent sagging or frame deformation.
- **R-D3** The fabric alone (without the frame) can hold 30 kg without
  failing, so a frame fault doesn't drop the weights.
- **R-D4** Every outer fabric option is highly abrasion- and tear-resistant
  and water-resistant, and passes the same 30 kg durability tests.
- **R-D5** All load-bearing seams use heavy bonded thread with bar-tacks or
  box-X stitching; load-bearing hardware is metal, not plastic.
- **R-D6** Weight compartment base and lining resist abrasion from the
  bricks being slid in and out every day.
- **R-D7** Design life of at least 5 years of daily commuting (about 2,300
  loaded trips, each with several hand switches — roughly 10,000 lifts)
  _(hypothesis)_.
- **R-D8** Wear parts (handle wrap, base feet, tray runners) can be replaced.

### Weights ("bricks")
- **R-K1** Standard size and shape; every brick fits every slot.
- **R-K2** Coated or encased (no bare metal, no dust, no sharp edges),
  quiet, and safe to handle and drop.
- **R-K3** Weight clearly marked on each brick.
- **R-K4** Dense enough to keep the compartment slim (see design plan §3).
- **R-K5** Non-toxic materials (no lead).

## 6. Non-goals (v1)

- Rucking as the main exercise. The backpack can be worn, but both bags are
  designed first for the one-hand suitcase carry.
- Electronic features (sensors, step tracking, app).
- Luggage / travel suitcase sizes.

## 7. Success metrics (v1)

- Testers keep using it: ≥ 60% of wear-testers still carry weights after
  4 weeks _(hypothesis)_.
- Weight drop (UC-2) takes < 10 s and is rated "easy" by ≥ 90% of testers.
- No injuries, no load-path failures and no accidental weight releases in
  testing.
- Passes all lab durability tests at 30 kg (design plan §4) with no
  structural damage.
