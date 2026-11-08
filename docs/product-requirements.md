# Product requirements — product-design / POC revision

Status: provisional design targets; no engineering validation or certified
load rating. Dimensions and source-specific examples: [tech pack](tech-pack.md).

## 1. Audience and use

Primary audience: **office workers who are heavy lifters**, already training
and wanting an optional suitcase carry during the commute. Start with less
weight (including zero added weight); adjust to individual ability and the
route. **30 kg total is a ceiling, not a mandatory progression destination.**
Switch hands as appropriate and set down before losing control; walking to
exhaustion is not a POC test instruction. No fixed per-side time is required.

## 2. Product line

- **R-P1** Laptop bag (Heavy Brief, working name) and backpack (Big Pack).
- **R-P2** Shared finished-weight interface; different 4 × 1 and 3 × 3 carriers.
- **R-P3** Backpack has frame-mounted handle receivers; straps stow for hand carry.
- **R-P4** Laptop bag has the same handle-module concept and a detachable strap.
- **R-P5** One structural system for future fabric choices; Core nylon for POC.
- **R-P6** Both fit a 356 × 248 × 17 mm laptop plus weights and daily contents.
  Big Pack carries the laptop vertically; do not specify a 370 mm-wide sleeve
  inside a 360 mm-wide body.

## 3. Use cases

| ID | Use case |
| --- | --- |
| UC-1 | Carry a self-selected load; switch hands and set down when needed. |
| UC-2 | Set the bag on stable support, deliberately release and remove weights for storage at work. |
| UC-3 | Refit secured weights, or leave them out for a lighter return. |
| UC-4 | Change individual weights with the bag set down. |
| UC-5 | Stop and set down if load is unsuitable; unload safely, never dump weights onto the route. |
| UC-6 | Use as a normal work bag with no added weights. |

## 4. Functional requirements

### Weight system

- **R-W1** Dedicated retained compartment, separated from laptop and contents.
- **R-W2** Nominal 1.25 / 2.5 kg own-brick steps; other sources have measured steps.
- **R-W3** Maximum **30 kg complete bag**, including empty tray/carrier, chosen
  handle and any inserts. 24 kg added allowance is only the 2.5 + 2 + 1.5 kg
  example, not a universal capacity.
- **R-W10** Prevent accidental overload through marked source/load charts and
  weighing the complete assembly. Volume alone cannot enforce 30 kg; dense
  weights may fit while exceeding it. Do not claim mechanical overload limiting.
- **R-W4** Removal is controlled with the bag supported. Single supported
  cassette versus two smaller cassettes remains an open proposal. Record time
  and effort; the former one-motion / under-10-second promise is withdrawn
  until a safe method is selected and tested.
- **R-W5** Individual weights adjustable without dumping the remaining load.
- **R-W6** Deliberate retention release independent of the textile hatch; no
  accidental exit. Supported-slide proposal includes a travel stop and final
  release only with external support in place.
- **R-W7** No shifting or harmful rattle at empty, partial or maximum load; use
  clamp, liners and low-stack spacers appropriate to each source.
- **R-W8** Laptop weights in base. Big Pack weights against back frame;
  **low vs fixed mid-low is unresolved**, with 30 mm offset trial proposed.
- **R-W9** Enclosures have two lifting grips, retained clear of their insertion
  envelope; lifting strength and storage stability require testing.
- **R-W11** “One tray, any weight” is an interface goal. Sources must fit the
  finished envelope with coating/sleeves and retention hardware; no bare steel.
- **R-W12** No universal 24 kg claim. See tech-pack capacity table. Shells,
  water, sand, shot, bars and plates have distinct volume and mass limits.

### Bag, laptop and handles

- **R-B1** Common receivers mechanically attached to frame bridge, not sewn
  only: interchangeable fabric module and standard rigid weight handle module.
  POC uses captive bolts; no untested quick release. “Double weight handle”
  module reserved as **TBD**, no inferred shape, interface extension or rating.
- **R-B2** Bag hangs acceptably vertical and clears the leg at the tested loads.
- **R-B9** Left/right handling and switches work without dangling harness parts.
- **R-B3** Handle → receivers → bridge/stays → cradle → retained weights.
- **R-B4** Proposed static proof target 90 kg equivalent (3 × 30); engineer to
  confirm protocol, fasteners and acceptance before testing. Not an achieved rating.
- **R-B5** Suspended padded laptop sleeve above a rigid barrier, with replaceable
  impact pads and an unloaded free gap. No bottom-out against frame/weights
  under agreed drop tests with a laptop surrogate; gap dimensions alone do not
  establish protection. Big Pack also needs lateral separation from its carrier.
- **R-B6** Professional work-bag appearance.
- **R-B7** Detachable shoulder strap / stowable backpack harness for non-training use.
- **R-B8** ≤2.5 kg empty incl. frame, empty cassette, selected handle and all
  required inserts is a stretch hypothesis. Measure each configuration and
  reduce permitted ballast if it is heavier.

### Durability and own weights

- **R-D1** 6061-T6 spine plus HDPE panels; profiles/joints unvalidated.
- **R-D2** Daily-use structural target up to 30 kg; verify statics/fatigue/creep.
- **R-D3** Textile backup containment to be tested with primary frame disconnected.
- **R-D4** Future fabric options must pass the same structural tests.
- **R-D5** Reinforced seams and metal load-path hardware; inspect bolt retention.
- **R-D6** Replaceable abrasion-resistant weight lining and runners.
- **R-D7** Five-year life / 10,000 lift-cycle target is a hypothesis, not proof.
- **R-D8** Replaceable wraps, pads, feet, runners and handle modules.
- **R-K1** Nominal steel core footprint 95 × 100 mm, finished full envelope
  ≤97 × 102 × 35 mm, half ≤97 × 102 × 18 mm. All adapters fit their stated cavity.
- **R-K2** Encased/coated, quiet, no exposed sharp metal; sample impact testing required.
- **R-K3** Mark measured finished mass. 2.5 / 1.25 kg are targets, not exact mass
  guaranteed by dimensions. Tolerance to be agreed before fabrication.
- **R-K4** Dense sources support slim compartments; low-density fillers need less mass.
- **R-K5** No lead; assess materials and containment before handling trials.

## 5. Scope and POC gates

Product design only now: resolve packaging, extraction, laptop isolation,
handle module ergonomics and backpack position, then prepare sample/parts
orders in Israel or abroad. Rucking is not the primary v1 exercise. Legal,
market validation, shipping economics, ads and Kickstarter are deferred until
a satisfying product POC; none is a gate to the current design iteration.

POC evidence: fit gauges for finished coated parts; empty/partial-load rattle
checks; supported removal; mass record; grip and balance comparison at
comfortable submaximal loads; controlled rig tests before heavy human carries;
surrogate-laptop drop tests with no bottom-out. Record failures and revise.
No live laptop or improvised cardboard structure in a 30 kg walk test.
