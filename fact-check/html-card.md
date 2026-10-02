# HTML Fact-Check Card (Mode 1 output)

Single self-contained `.html` file, inline CSS, no external deps. Sections:
header (title in user's language, date, mode badge) · content summary ·
overall verdict + MFS gauge with CFS/MTS/SCD breakdown · confidence factors ·
per-claim breakdown (classification + verdict badge + mini reasoning + tiered
sources) · counterfactual (if applicable) · red flags (category icon + severity
dot) · origin trace (if applicable) · sources with evaluation (tier badge, site
rating, author, evidence quality, lateral finding, collapsible "how we
evaluated") · educational section (10a–10f) · share-safe summary · disclaimer.

**Design:** verdict palette only —
`--green:#16a34a · --lime:#65a30d · --yellow:#ca8a04 · --orange:#ea580c ·
--red-orange:#dc2626 · --dark-red:#991b1b`. No purple/indigo/violet. 8px
spacing scale, max-width 800px centered, `<details>/<summary>` for collapsibles,
mobile responsive (320px+), `prefers-color-scheme` dark/light, `@media print`,
system font stack, ≤3 font weights, WCAG AA contrast.
