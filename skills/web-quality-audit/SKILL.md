---
name: web-quality-audit
description: Audit and improve web quality across accessibility, performance, UX, privacy, and browser security. Use for frontend audits, client audits, redesigns, landing pages, production-readiness passes, Core Web Vitals, keyboard navigation, privacy reviews, CSP/cookie/header checks, and responsive UI verification.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Web Quality Audit

Run a compact cross-functional quality pass. Treat accessibility, performance, UX, privacy, and security as connected product risks.

Use `authorized-security-router` first when the request moves from passive web quality review into security testing, target enumeration, request replay, or any live target with unclear authorization.

## Audit Tracks

### Accessibility

- Semantic headings, landmarks, labels, alt text, and form errors.
- Keyboard navigation, focus order, visible focus, and modal/menu focus management.
- ARIA only when native HTML does not cover the interaction.
- Color contrast, reduced motion, and responsive text fit.

### Performance

- LCP candidate image priority, dimensions, compression, and lazy loading.
- Render-blocking CSS/JS, unnecessary third-party scripts, and asset cache busting.
- Expensive render loops, hydration weight, excessive network waterfalls, and unbounded lists.
- Core Web Vitals or local browser measurements when available.

### UX

- First-screen clarity, task orientation, control affordance, empty/loading/error states.
- Mobile layout, tap targets, horizontal overflow, text clipping, and predictable navigation.
- Copy that matches the surface: utility copy for tools, sharper copy for landing pages.

### Privacy

- Data minimization, consent clarity, third-party scripts, tracking pixels, embeds, and analytics.
- Cookies, local storage, referrer policy, permissions policy, and logout cleanup.
- Avoid logging private data in client telemetry and violation reports.

### Security

- Dangerous DOM sinks, unsafe inline scripts, postMessage validation, frame embedding rules.
- Cookie flags, HTTPS/HSTS, CSP rollout state, Trusted Types readiness, CORS/Fetch Metadata where relevant.
- Report-only policies before strict enforcement on existing apps.

## Workflow

1. Identify the app type, target users, critical paths, and deployment constraints.
2. Run static checks first: HTML structure, image dimensions, obvious headers, bundle/assets, dependency scripts.
3. Run browser checks: desktop/mobile, console errors, network failures, keyboard path, overflow, and key interactions.
4. Rank findings by user impact, likelihood, and implementation risk.
5. Fix low-risk issues immediately when the user asked to improve the site.
6. Gate risky policy changes, tracking changes, auth/payment changes, or destructive migrations behind explicit confirmation.

## Report Format

For each finding:

- severity;
- evidence;
- affected file/page;
- recommended fix;
- verification.

Final response should separate implemented fixes from deferred risks.
