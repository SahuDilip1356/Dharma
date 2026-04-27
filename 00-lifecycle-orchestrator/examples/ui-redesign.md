# Example: UI Redesign

**Request:** "The clinic dashboard looks dated and doctors say it's hard to scan — redesign it."

---

## Classification
```
Work type:    ui-ux-design
Surface area: frontend
User impact:  user-facing (primary daily-use screen for doctors and receptionists)
Risk level:   medium (no data model changes; visual + layout only)
Reversibility:easy (CSS/component changes, feature flag possible)
Route:        D (UI/UX Design or Redesign)
```

---

## Phase Sequence

**Phase 1 — UX Gate** → `uiux-designer` + `uiux-design-intelligence`

```
User flow:
  Doctor opens dashboard → sees today's appointments → clicks patient → opens chart
  Receptionist opens dashboard → sees check-in queue → marks patient arrived

Primary action: scan appointment list at a glance (doctors); mark arrivals (receptionists)

Hierarchy:
  1. Today's schedule (time + patient name + status)
  2. Quick action (check in / open chart)
  3. Summary stats (appointments today, completed, pending)
  4. Secondary: upcoming tomorrow

States:
  Empty: "No appointments scheduled today" + schedule link
  Loading: skeleton rows (not spinner — users need to scan on arrival)
  Error: "Unable to load schedule — [retry]" with last-known data if cached
  Success: live appointment list

Accessibility:
  - Status badges must use icon + text + color (not color alone)
  - Keyboard: Tab through appointments, Enter to open patient
  - Screen reader: appointment rows must announce time + name + status

Responsive:
  - 375px: single column, time + name + tap-to-expand
  - 768px: two columns, status badge visible
  - 1280px: full table with all columns + side panel

Visual direction: Corporate Clean (dark navy sidebar, white content, blue accent)
  Primary:    #1B2B4B (navy)
  Accent:     #0066CC (blue)
  Background: #F8FAFC
  Surface:    #FFFFFF
  Font:       Inter 400/500/600
```

**Phase 2 — Planning Gate** → `uiux-frontend-design-system`

```
Design system:
  - Spacing: 4px base scale
  - Radius: 6px cards, 4px badges
  - Shadow: sm only (dashboard = data, not decoration)
  - Status colors: green (checked-in), amber (waiting), gray (scheduled)
    Each uses: color + icon + text label (never color alone)

Files affected:
  - components/Dashboard/AppointmentList.tsx
  - components/Dashboard/StatsSummary.tsx
  - components/Dashboard/StatusBadge.tsx (new)
  - app/dashboard/page.tsx
  - styles/tokens.css (update color tokens)
```

**Phase 3 — Build** → `uiux-react-patterns` + `surgical-changes`
- Server Component for appointment data fetch
- `StatusBadge` as a new isolated component (not modifying existing badge)
- Skeleton loading via `AppointmentSkeleton` component
- No changes to data fetching logic, API, or patient record components

**Phase 4 — Verification** → `uiux-accessibility-review` + `uiux-responsive-review` + `uiux-design-qa`

```
Accessibility:
  - Color contrast: navy #1B2B4B on white = 12.4:1 ✅
  - Status badges: icon + text + color ✅
  - Keyboard: Tab cycles appointments, Enter opens patient ✅
  - Screen reader: "9:00 AM — Priya Sharma — Waiting" announced ✅

Responsive:
  - 375px: single column, time stacked above name ✅
  - 768px: two columns visible ✅
  - 1280px: full table with side panel ✅

States:
  - Empty: "No appointments today" with CTA ✅
  - Loading: skeleton rows visible for 200ms ✅
  - Error: retry message with cached data shown ✅

Screenshots: attached at 375 / 768 / 1280px
```

**Phase 5 — Finish**
```
Summary: Dashboard redesigned — Corporate Clean style, improved scan hierarchy, accessible status badges
Verified: a11y ✅, responsive ✅, all states ✅, screenshots reviewed
Remaining risks: none — visual change only, no data model affected
Next: PR → design review with one doctor before merge
```
