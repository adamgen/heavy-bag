# Product Requirements (v0 — draft)

Status: **draft**. Numbers marked _(hypothesis)_ are starting points to be
validated in research and prototyping, not commitments.

## 1. Target users

- **Primary — the walking commuter.** Office worker who walks 10–30 minutes
  each way (or walks to/from transit), wants to get stronger, and is short on
  time.
- **Secondary — the fitness-minded professional.** Already trains, knows what
  a suitcase carry or ruck is, and wants to add volume through the day.

## 2. Use cases

| ID | Use case |
| --- | --- |
| UC-1 | Walk to work carrying the loaded bag in one hand, switching hands as needed. |
| UC-2 | Arrive at work, pull the weights out in one motion, leave them under the desk or in a locker, and use the bag normally during the day. |
| UC-3 | Before going home, put the weights back in (or don't — light day). |
| UC-4 | Add or remove one brick to change the load (progression, tired day, injury). |
| UC-5 | Mid-walk, decide the load is too much and drop weights quickly. |
| UC-6 | Use the bag as a normal work bag with no weights at all. |

## 3. Functional requirements

### Weight system
- **R-W1** Holds added weight in a dedicated compartment, physically separated
  from the main (laptop) compartment.
- **R-W2** Adjustable in increments of 1–2.5 kg _(hypothesis)_.
- **R-W3** Added load range 0–15 kg _(hypothesis; validate with users and a
  strength coach / physio)_.
- **R-W4** All weights can be removed together in one motion, in under
  10 seconds, without tools _(hypothesis)_.
- **R-W5** A single brick can be added or removed without removing the others.
- **R-W6** Weights cannot fall out by accident: release needs a deliberate
  action (for example, a two-step release).
- **R-W7** Weights don't shift, slide or rattle while walking.
- **R-W8** Weight compartment sits low in the bag (bottom, or lower side),
  centred under the handle.
- **R-W9** The removed weights are easy to carry and store as a unit (for
  example, a tray or pouch with its own grip).

### Bag & carry
- **R-B1** A top handle designed for one-handed suitcase carry: rigid, sits
  over the centre of mass, comfortable diameter for a long hold.
- **R-B2** The loaded bag hangs vertically and stays clear of the leg while
  walking.
- **R-B3** Load path runs from the handle through internal structure (frame
  or webbing) to the weights — not through decorative fabric panels.
- **R-B4** Handle and attachment points rated to at least 3× maximum loaded
  weight _(hypothesis; set the final factor with the manufacturer)_.
- **R-B5** Protected laptop sleeve (fits 14"–16" laptop _(hypothesis)_).
- **R-B6** Professional look, suitable for an office.
- **R-B7** Optional shoulder strap for days or moments you don't want to
  train.
- **R-B8** Empty bag weight ≤ 2 kg _(hypothesis)_.

### Weights ("bricks")
- **R-K1** Standard size and shape; every brick fits every slot.
- **R-K2** Coated or encased (no bare metal, no dust, no sharp edges),
  quiet, and safe to handle and drop.
- **R-K3** Weight clearly marked on each brick.
- **R-K4** Dense enough to keep the compartment slim (see design plan §3).
- **R-K5** Non-toxic materials (no lead).

## 4. Non-goals (v1)

- Backpack carry as the main mode (that's rucking, a different product).
- Electronic features (sensors, step tracking, app).
- Luggage / travel suitcase sizes.

## 5. Success metrics (v1)

- Testers keep using it: ≥ 60% of wear-testers still carry weights after
  4 weeks _(hypothesis)_.
- Weight drop (UC-2) takes < 10 s and is rated "easy" by ≥ 90% of testers.
- No injuries, no load-path failures and no accidental weight releases in
  testing.
