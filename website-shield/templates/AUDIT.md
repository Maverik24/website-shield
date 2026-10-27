# Website audit: [SITE URL]

Date: [YYYY-MM-DD]. Audit only: no site files changed.
Regions: [US / EU / both]. Stack and host: [ ].
**Not legal advice.** Findings reflect the checks below as of the date above.

Severity: **High** = fix before launch or before taking clients. **Medium** = fix in this round. **Low** = nice to have or confirm only.

## Summary

| Area | Result | Severity |
|---|---|---|
| Secrets in code | [ ] | [ ] |
| Databases, storage, server functions | [ ] | [ ] |
| Third-party loads | [ ] | [ ] |
| Trackers, pixels, analytics, session replay, chat | [ ] | [ ] |
| Cookies and browser storage | [ ] | [ ] |
| Forms and data destinations | [ ] | [ ] |
| Legal pages | [ ] | [ ] |
| Accessibility (light and dark, phone and desktop) | [ ] | [ ] |
| Claims and promises | [ ] | [ ] |
| Security headers | [ ] | [ ] |

## 1. Third-party domains per page (measured in a headless browser)

| Page | Domain | Resource type | Loaded by | Cookies set |
|---|---|---|---|---|
| [ ] | [ ] | [script, iframe, font, image, fetch] | [ ] | [ ] |

## 2. Secrets and committed files

- Patterns searched: [ ]
- Findings: [none / list with file and line]
- `.gitignore` covers `.env*`: [yes / no / no git]

## 3. Backend services and rules

| Service | Status | Rules |
|---|---|---|
| [ ] | [in use / disabled / not found] | [open / locked / n/a] |

## 4. Forms and where data goes

| Page | Element | Collects | Destination |
|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] |

## 5. Claims, promises and guarantees

| # | Page and line | Text | Issue | Severity |
|---|---|---|---|---|
| C1 | [ ] | [ ] | [no source / vague guarantee / legal assurance / fake reference price] | [ ] |

Commitments to confirm with the owner: [list, then copy confirmed ones to COMMITMENTS.md]

## 6. Accessibility

Automated: axe-core runs: [N] ([pages] x light/dark x 375px/1280px). Violations: [N].

| # | Page / theme / width | Issue | WCAG | Severity |
|---|---|---|---|---|
| A1 | [ ] | [ ] | [ ] | [ ] |

Manual checks:
- [ ] Keyboard walk: visible focus ring at every stop, both themes
- [ ] Non-text contrast at least 3:1 (input borders, meaningful icons)
- [ ] Sticky bars never cover the focused element
- [ ] Mobile menu: focus moves in and stays in while open; Escape closes it
- [ ] Reduced motion respected
- [ ] One `h1` per page, no skipped heading levels, `lang` set
- [ ] Every input labelled, every iframe titled, decorative images `alt=""`

## 7. Legal pages

| Page | Status | Missing items |
|---|---|---|
| Privacy policy | [present / missing] | [ ] |
| Cookie policy | [ ] | [ ] |
| Legal notice / identity | [ ] | [ ] |
| Terms | [ ] | [ ] |
| Accessibility statement | [ ] | [ ] |

## 8. Security headers (live)

| Header | Present | Value |
|---|---|---|
| Strict-Transport-Security | [ ] | [ ] |
| X-Content-Type-Options | [ ] | [ ] |
| X-Frame-Options | [ ] | [ ] |
| Referrer-Policy | [ ] | [ ] |
| Permissions-Policy | [ ] | [ ] |
| Content-Security-Policy (or Report-Only) | [ ] | [ ] |

## Decisions needed from the owner

- D1: [question, recommended default, one-line reason]
- D2: [ ]

## Verification (filled in after fixes)

| Check | Result |
|---|---|
| axe-core, all pages, both themes, both widths | [ ] |
| Lighthouse accessibility and best practices | [ ] |
| All pages 200, unknown URL 404, footer links work | [ ] |
| CSP violations (with control test passing) | [ ] |
| No placeholders, banned phrases or personal IDs outside the identity page | [ ] |
