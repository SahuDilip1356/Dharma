---
name: uiux-react-patterns
description: |
  React and Next.js component patterns for high-quality, performant, accessible UI.
  Powered by Vercel's 70-rule React best practices guide. Triggers when:
  - Writing or reviewing React/Next.js components
  - Performance, rendering, or bundle size is a concern
  - Component API design feels off or props are getting complex
  - uiux-designer master skill reaches the implementation step for React/Next.js

  Covers: eliminating waterfalls, bundle optimization, server vs client boundaries,
  re-render optimization, form patterns, data fetching, and advanced React patterns.

license: MIT
metadata:
  author: Dilip Sahu
  source: Vercel react-best-practices (70 rules, 8 categories)
  version: "1.0.0"
---

# UI/UX React Patterns (Vercel Best Practices)

**Source:** Vercel Engineering — 70 rules across 8 categories for React and Next.js.

---

## Category 1: Eliminating Waterfalls (CRITICAL)

Waterfalls = sequential awaits when parallel is possible. This is the #1 performance killer in React/Next.js apps.

**Rule:** Never `await` sequentially when requests are independent.

```tsx
// ❌ Waterfall — each waits for the previous
const user = await fetchUser(id)
const posts = await fetchPosts(id)
const comments = await fetchComments(id)

// ✅ Parallel — all fire simultaneously
const [user, posts, comments] = await Promise.all([
  fetchUser(id),
  fetchPosts(id),
  fetchComments(id),
])
```

**In React Server Components:** Use `Promise.all` at the top of the component, not inside sequential `await` chains.

**In layouts:** Fetch data in parallel across layout + page — don't chain parent → child sequential fetches.

---

## Category 2: Bundle Size (CRITICAL)

Every KB of JS delays time-to-interactive.

```tsx
// ❌ Imports entire library
import { format } from 'date-fns'

// ✅ Direct import — only the function
import format from 'date-fns/format'

// ❌ Heavy library for one icon
import { FiSearch } from 'react-icons/fi'

// ✅ SVG inline or specific import
import SearchIcon from '@/icons/search.svg'
```

**Dynamic imports for heavy components:**
```tsx
import dynamic from 'next/dynamic'

// ✅ Only loads when component is rendered
const HeavyChart = dynamic(() => import('./Chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false, // only if not needed server-side
})
```

**Rules:**
- Never `import *` from a large library
- Tree-shake lodash: use `lodash-es` or individual function imports
- Dynamic import for: map libraries, rich text editors, chart libraries, PDF viewers
- Monitor bundle with `@next/bundle-analyzer`

---

## Category 3: Server vs Client Boundary

**Default: Server Component.** Only add `"use client"` when you need:
- `useState` / `useReducer`
- `useEffect` / browser APIs
- Event handlers (`onClick`, `onChange`)
- Third-party client-only libraries

```tsx
// ✅ Server Component — no "use client" needed
export default async function ProductPage({ id }) {
  const product = await getProduct(id)  // direct DB/API call
  return <ProductView product={product} />
}

// ProductView stays server unless it needs interactivity
// Push "use client" to the leaf — the smallest interactive piece
```

**Pattern: Client Island**
```tsx
// server/ProductPage.tsx (Server Component)
import { AddToCartButton } from './AddToCartButton'  // "use client"

export default async function ProductPage() {
  const product = await getProduct()
  return (
    <div>
      <ProductDetails product={product} />   {/* stays server */}
      <AddToCartButton productId={product.id} />  {/* only this is client */}
    </div>
  )
}
```

---

## Category 4: Re-render Optimization

**Rule:** Don't optimize prematurely. Profile first with React DevTools Profiler.

```tsx
// ❌ Inline function — new reference every render
<Button onClick={() => handleClick(id)} />

// ✅ useCallback — stable reference
const handleClick = useCallback(() => {
  // ...
}, [id])
<Button onClick={handleClick} />

// ❌ Object created every render
<Component style={{ padding: 16 }} />

// ✅ Stable reference
const style = useMemo(() => ({ padding: 16 }), [])
<Component style={style} />
```

**When to memoize:**
- `useMemo`: expensive calculations (>1ms), or object passed to child that triggers re-renders
- `useCallback`: function passed to child component wrapped in `React.memo`
- `React.memo`: component that re-renders often with same props

**When NOT to memoize:** Everything else. Memoization has a cost — only apply where profiling shows a problem.

---

## Category 5: Component API Design

**Props rules:**

```tsx
// ❌ Boolean prop explosion
<Button primary large rounded fullWidth disabled loading />

// ✅ Variant + size system
<Button variant="primary" size="lg" loading />

// ❌ Overloaded children
<Modal title="..." footer={<div>...</div>} content={<div>...</div>} />

// ✅ Composition pattern
<Modal>
  <Modal.Header>...</Modal.Header>
  <Modal.Body>...</Modal.Body>
  <Modal.Footer>...</Modal.Footer>
</Modal>

// ❌ Prop drilling 3+ levels
<A prop={x}><B prop={x}><C prop={x} /></B></A>

// ✅ Context for deeply shared state
const ThemeContext = createContext()
```

**Composable component rules:**
- One component, one responsibility
- Props should be the minimum needed — no passing through props you don't use
- Prefer `children` composition over render props for simple cases
- Use `forwardRef` when consumers need DOM access (input, button, modal trigger)

---

## Category 6: Forms

```tsx
// ✅ Server Actions (Next.js App Router)
async function submitForm(formData: FormData) {
  'use server'
  const email = formData.get('email')
  await saveEmail(email)
}

<form action={submitForm}>
  <input
    type="email"
    name="email"
    autoComplete="email"
    inputMode="email"
    spellCheck={false}
    required
  />
  <SubmitButton />
</form>

// ✅ SubmitButton with pending state
function SubmitButton() {
  const { pending } = useFormStatus()
  return (
    <button type="submit" disabled={pending} aria-busy={pending}>
      {pending ? 'Saving…' : 'Save'}
    </button>
  )
}
```

**Form rules:**
- Use `name` attribute on all inputs — required for FormData
- `autoComplete` on all inputs (browsers use this for autofill)
- Correct `type` and `inputMode` for mobile keyboards
- `spellCheck={false}` on email, username, code inputs
- Never `preventDefault` on paste
- Inline error messages with `aria-describedby`
- Focus first error field on failed submit

---

## Category 7: Data Fetching Patterns

```tsx
// ✅ Fetch in Server Component, pass as props
export default async function Page() {
  const data = await getData()  // cached by Next.js automatically
  return <ClientComponent initialData={data} />
}

// ✅ Parallel data fetching
export default async function Dashboard() {
  const [metrics, users, events] = await Promise.all([
    getMetrics(),
    getUsers(),
    getRecentEvents(),
  ])
  return <DashboardView metrics={metrics} users={users} events={events} />
}

// ✅ Streaming with Suspense
export default function Page() {
  return (
    <>
      <CriticalContent />  {/* renders immediately */}
      <Suspense fallback={<MetricsSkeleton />}>
        <SlowMetrics />    {/* streams in when ready */}
      </Suspense>
    </>
  )
}
```

**Rules:**
- Fetch as close to use as possible (colocated in the Server Component that renders it)
- Use `cache()` from React for request deduplication across components
- `revalidate` or `revalidatePath` for cache invalidation after mutations
- Skeleton screens > spinners for content areas > 300ms

---

## Category 8: Accessibility Patterns in React

```tsx
// ✅ Icon button
<button
  onClick={handleClose}
  aria-label="Close dialog"
  className="focus-visible:ring-2 focus-visible:ring-offset-2"
>
  <XIcon aria-hidden="true" />
</button>

// ✅ Form field with error
<div>
  <label htmlFor="email">Email</label>
  <input
    id="email"
    type="email"
    aria-describedby={error ? 'email-error' : undefined}
    aria-invalid={!!error}
  />
  {error && (
    <p id="email-error" role="alert">
      {error}
    </p>
  )}
</div>

// ✅ Loading state announced to screen readers
<div aria-live="polite" aria-busy={isLoading}>
  {isLoading ? 'Loading…' : content}
</div>

// ✅ Dialog/Modal with focus trap
<dialog
  ref={dialogRef}
  onKeyDown={e => e.key === 'Escape' && close()}
>
  {/* focus trapped inside while open */}
</dialog>
```

---

## Quick Reference: Red Flags in Code Review

| Seen In Code | Problem | Fix |
|-------------|---------|-----|
| Sequential `await` chains | Waterfall | `Promise.all` |
| `import { x } from 'huge-lib'` | Bundle bloat | Direct import or dynamic |
| `"use client"` on page/layout | Too high in tree | Push to leaf component |
| Inline `() =>` in JSX to child | Re-render risk | `useCallback` |
| 5+ boolean props on component | API explosion | `variant` system |
| No `autoComplete` on inputs | Poor UX | Add `autocomplete` attribute |
| `outline: none` anywhere | Focus lost | `focus-visible` replacement |
| Large list `.map()` without virtualization | Performance | `virtua` or `content-visibility` |
| `useState` for server-fetchable data | Unnecessary | Fetch in Server Component |
