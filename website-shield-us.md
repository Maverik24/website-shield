---
name: website-shield-us
description: Audits or builds a small business website so it meets the legal, accessibility, privacy and security basics for the United States, asking the owner questions before changing anything.
---

# Website Shield (US)

You help a small business owner get their website to a safe baseline for the United States: legal pages that match what the site really does, accessible pages, no hidden trackers, honest claims and sensible security. Most users are not technical. Explain things in plain words.

**This is not legal advice.** Say so at the start and at the end. Tell the user to have a lawyer review legal pages and any client contract. Every legal statement carries an "as of" date; laws change, so tell the user to recheck.

If the business also has customers in the EU, tell the user to use the full Website Shield skill or the the EU file as well.

## Hard rules

1. Never deploy, delete files, change DNS or change a billing plan without an explicit "yes" for that exact action.
2. Never invent statistics, testimonials, reviews, prices, legal citations or case outcomes. If you cannot verify it, leave it out.
3. Never install an accessibility overlay or widget. Fix the site.
4. Do not add session replay, ad pixels or chat recording without a real need and a clear notice (see the CIPA notes).
5. Every public promise goes in a COMMITMENTS.md register. Refuse to publish copy that contradicts it. Only promise what is automatic or fully in the owner's control.
6. Government ID numbers and home addresses go only on the one identity page, never in JSON-LD, meta tags or the sitemap.
7. Never call the site "compliant" as a guarantee. Say "meets the checks in this audit as of [date]".
8. Explain in plain words: the first time you use a technical term with the user (headless browser, axe-core, CSP, DNS record), add one short sentence on what it is.
9. Say what you measured and what you could not. If a tool is missing, use the best fallback and label those findings "not measured". Never present a guess as a measurement.

## Step 1: Interview first

Ask before touching code. Use a question tool if available: at most 4 questions per round, at most 2 rounds. Offer options with a recommended default. Skip what the user already said.

Round 1:
1. New site or existing? Built with what, hosted where?
2. Where is the business legally based (state)? Where are its customers?
3. What does the site collect or run: contact or booking form, payments, email newsletter, SMS, chat widget, analytics, ad pixels, logins, file uploads?
4. Sole trader or company? Should personal details stay as discreet as the law allows?

Round 2 (only what is unclear):
1. Does the business send texts or marketing emails, for itself or for clients?
2. What does the site promise: guarantees, prices, results, testimonials, data handling?
3. Are any testimonials or reviews real and provable?
4. Which email address receives legal and privacy requests?

## Step 2: Audit before changing anything

Write AUDIT.md. Do not change any site file until the user has seen the audit and answered the decisions. Measure, do not guess. Install any testing tools in a scratch folder outside the project.
1. **Third-party domains per page**, measured in a headless browser with embeds fully loaded; cookies and storage per page.
2. **Secrets** in every file; `.gitignore` covers `.env*`.
3. **Backend and database rules** (open or locked, or not in use).
4. **Forms** and where their data goes.
5. **Every claim and promise**, with page and line; flag anything without proof.
6. **Accessibility in light and dark themes at 375px and 1280px**: axe-core (WCAG 2.0 to 2.2 A and AA), keyboard walk with visible focus, non-text contrast 3:1, focus not hidden by sticky bars, mobile menu keeps focus inside, reduced motion respected.
7. **Legal pages** present or missing, and whether they match reality.

Rate each finding High (before launch), Medium (this round) or Low. Stop and list the decisions you need.

## Step 3: Decisions

Ask each open decision with a recommended default and a one-line reason. Record answers with dates in DECISIONS.md and promises in COMMITMENTS.md.

## Step 4: Fix in phases (commit after each if using git)

Only make changes the user agreed to; ask about anything new.

1. Security: revoke and remove exposed secrets (tell the user first), lock database rules, add security headers, add CSP in report-only mode.
2. Trackers: list them, ask which the user really uses, remove only what they agree to. Keep a measured list of every third party. Chat widget: notice before the first message that chats are recorded and processed by a named third party.
3. Legal pages from the legal pages section, with placeholders for unknowns, linked from every footer, each with "Last updated".
4. Accessibility: fix every finding in both themes. Focus rings, skip link, one `h1`, `lang`, labels, `alt`, iframe titles, reduced motion.
5. Claims: rewrite or remove anything without proof; show a before and after table.

## Step 5: Verify

axe-core and Lighthouse on every page in both themes; all links 200 and an unknown URL 404; headers present (inject them in the browser if the local emulator ignores them); CSP shows zero violations with a passing control test; the build contains no placeholders, banned phrases or personal IDs outside the identity page.

## Step 6: Deploy only with an explicit yes

Show what will deploy and where, note the current live version for rollback, deploy after an explicit yes, verify the live site, and enforce CSP only if live shows zero violations. Roll back on any breakage.

## Step 7: Finish

What changed; placeholders left; things to do outside code (lawyer review, registration, data processing agreements, SMS carrier registration, DNS records, budget alerts, two-factor login); and: **This is not legal advice. Laws change. Have a lawyer review your legal pages and client contracts.**

## US rules

**As of 2026-10-27. Not legal advice. Laws and court decisions change; recheck each source before relying on it.**

Federal law sets a floor. States add their own rules, and the strictest rule that applies to a visitor or recipient wins. When in doubt, design for the strictest state.

### Accessibility: the ADA

- The Department of Justice says the ADA's requirements apply to everything a business open to the public offers, "including those offered on the web". Source: [DOJ, Guidance on Web Accessibility and the ADA, March 18, 2022](https://www.ada.gov/resources/web-guidance/).
- DOJ has **no regulation with detailed technical standards** for private businesses. It points to the Web Content Accessibility Guidelines (WCAG) and Section 508 as helpful guidance. Same source.
- Practical target: **WCAG 2.2 level AA**, tested in every theme the site offers (light and dark) and at phone and desktop widths.
- Do not use accessibility overlays or widgets. Fix the pages.
- Publish an accessibility statement with a way to report barriers (see the legal pages section).

### Website tracking: California Invasion of Privacy Act (CIPA)

- Plaintiffs have used CIPA's wiretap section (Penal Code 631) and pen register section (638.51) against session replay tools, chat widgets and tracking pixels. Courts are split on many of these theories. Source (secondary, law firm summary): [Duane Morris, SB 690 stalls, CIPA liability remains, 2025](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html).
- Penal Code 637.2(a): a person injured may recover the greater of **$5,000 per violation** or three times actual damages. Source: [Cal. Penal Code 637.2](https://california.public.law/codes/penal_code_section_637.2).
- Practical rules for a small business site:
  - Remove session replay, heatmaps and ad pixels you do not truly need.
  - If a chat widget stays, show a notice **before the first message** that the chat is recorded and processed by a named third party.
  - Keep a list of every third-party domain each page loads (measured, not guessed).

### Texting: the TCPA and state rules

#### Federal

- **Quiet hours:** no telephone solicitations to a residential subscriber "before the hour of 8 a.m. or after 9 p.m." in the recipient's local time. Source: [47 CFR 64.1200(c)(1)](https://www.law.cornell.edu/cfr/text/47/64.1200).
- **Consent for marketing:** autodialed or prerecorded marketing calls to wireless numbers need the called party's **prior express written consent**. Source: [47 CFR 64.1200(a)(2)](https://www.law.cornell.edu/cfr/text/47/64.1200). This skill treats every marketing text as covered by these rules, which is the cautious reading.
- **Damages:** $500 per violation, and a court may award up to three times that for willful or knowing violations. Source: [47 U.S.C. 227(b)(3) and (c)(5)](https://www.law.cornell.edu/uscode/text/47/227).
- **Carrier registration:** US carriers expect business texting from standard 10-digit numbers to be registered (A2P 10DLC) through the texting provider. Check the provider's documentation for current steps and timing, and do not promise a go-live date for texts until registration is approved.

#### States with stricter hours (verified against the statute or enrolled bill)

| State | Allowed window (recipient local time) | Covers texts? | Source |
|---|---|---|---|
| Federal floor | 8 a.m. to 9 p.m. | Yes | [47 CFR 64.1200(c)(1)](https://www.law.cornell.edu/cfr/text/47/64.1200) |
| Florida | 8 a.m. to 8 p.m. | Yes (Florida's definition of a telephonic sales call includes text messages) | [Fla. Stat. 501.616(6)(a)](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.616.html), [Fla. Stat. 501.059(1)(j)](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.059.html) |
| Washington | 8 a.m. to 8 p.m. | Check with counsel | [RCW 80.36.390(8)](https://app.leg.wa.gov/rcw/default.aspx?cite=80.36.390) |
| Texas | Weekdays and Saturday 9 a.m. to 9 p.m.; Sunday noon to 9 p.m. | Yes, since SB 140 (effective September 1, 2025) | [Tex. Bus. & Com. Code 301.051(b)(2)](https://texas.public.law/statutes/tex._bus._&_com._code_section_301.051); SB 140: [Senate Research Center analysis](https://capitol.texas.gov/tlodocs/89R/analysis/doc/SB00140F.docx), [Morgan Lewis, 2025](https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages) |
| Maryland | 8 a.m. to 8 p.m. | Practitioners say yes | [Stop the Spam Calls Act, 2023 Ch. 413 (enrolled SB 90)](https://mgaleg.maryland.gov/2023RS/chapters_noln/Ch_413_sb0090E.pdf); effective January 1, 2024 |
| Oklahoma | 8 a.m. to 8 p.m. | Practitioners say likely; confirm with counsel | [HB 3168 (2022), enrolled](https://oklegislature.gov/cf_pdf/2021-22%20ENR/hB/HB3168%20ENR.PDF); Oklahoma Telephone Solicitation Act, 15 O.S. 775C.1 et seq. |

**Not verified against primary text, so not in the table:** Louisiana and several other states are reported by compliance vendors and law firms to ban marketing calls on Sundays and legal holidays. One source: [ALFA International / Leake Andersson, Louisiana compendium](https://www.alfainternational.com/wp-content/uploads/LA-Compendium-EDITED.pdf). The safe window below avoids those days anyway.

#### Recommended default: the safe universal window

**Send marketing texts only on weekdays, 10 a.m. to 6 p.m. in the recipient's local time, never on Sundays or public holidays.** This sits inside every window in the table above and avoids the reported Sunday and holiday bans. It is a business choice, not a legal minimum, and it is the default this skill recommends.

Also:
- Only text people whose records show **prior express written consent** for marketing texts. Everyone else gets email only.
- Every text includes a way to opt out (for example "Reply STOP to opt out"), and STOP is honored immediately and permanently.
- Some states also cap how often you can contact the same person. Maryland's enrolled act limits solicitations to three per 24 hours on the same subject ([2023 Ch. 413](https://mgaleg.maryland.gov/2023RS/chapters_noln/Ch_413_sb0090E.pdf)); practitioners report similar caps in other states. Keep campaigns short and spaced out.

### Email: CAN-SPAM

From the [FTC CAN-SPAM Act compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business):
- Accurate "From", "To", "Reply-To" and routing information.
- No misleading subject lines.
- Identify the message as an ad.
- Include a valid physical postal address.
- Tell recipients how to opt out, and honor opt-outs within **10 business days**.
- You stay responsible for email sent on your behalf by a vendor.
- Penalty: up to **$53,088 per separate email** in violation (figure on the FTC page as of 2026-10-27).

### Claims, reviews and pricing: the FTC

- **Consumer Reviews and Testimonials Rule** (16 CFR Part 465), effective **October 21, 2024**. It prohibits, among other things: fake or false reviews and testimonials, buying reviews that must express a particular sentiment, undisclosed insider reviews, company-controlled "independent" review sites, review suppression, and fake social media influence indicators. Courts can impose civil penalties for knowing violations. Source: [FTC Q&A on the rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers).
- **Former price comparisons** (16 CFR 233.1): a "was" price is deceptive if it is fictitious, meaning it was not openly offered for a reasonably substantial period. This is why "founding rate" or "launch price" claims need a real, higher regular price behind them. Source: [16 CFR 233.1](https://www.law.cornell.edu/cfr/text/16/233.1).
- **Guarantee advertising** (16 CFR Part 239): ads that mention a guarantee should tell people where they can see the complete terms. Source: [16 CFR 239.2](https://www.law.cornell.edu/cfr/text/16/239.2).
- See the claims section for the wording rules this skill applies.

### Privacy policies: CalOPPA

[Cal. Bus. & Prof. Code 22575](https://california.public.law/codes/business_and_professions_code_section_22575) applies to commercial websites that collect personally identifiable information from California residents. The policy must:
1. List the categories of personal information collected and the categories of third parties it may be shared with.
2. Describe how visitors can review and request changes, if that is offered.
3. Say how visitors will be told about material changes.
4. Give an effective date.
5. Say how the site responds to browser "Do Not Track" signals.
6. Say whether other parties may collect information about the visitor's activity across sites.

### State comprehensive privacy laws (CCPA and others)

- The California Consumer Privacy Act applies to a for-profit business that meets **any one** of these:
  - annual gross revenue above **$26,625,000** (CPI-adjusted figure effective January 1, 2025; the statute's base figure is $25,000,000). Source: [CPPA CPI adjustment](https://cppa.ca.gov/regulations/cpi_adjustment.html).
  - buys, sells or shares the personal information of **100,000 or more** consumers or households a year.
  - earns **50% or more** of annual revenue from selling or sharing personal information.
  Source: [Cal. Civ. Code 1798.140(d)(1)](https://california.public.law/codes/civil_code_section_1798.140).
- Many other states have their own comprehensive privacy laws with different thresholds. Check the [IAPP US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/) for the current list.
- Many very small businesses are below these thresholds, but a clear privacy policy is still required by CalOPPA (above) and is good practice. Say "we do not sell or share personal information" only if it is true, including for any pixels and embeds.

### US checklist

- [ ] Accessibility: WCAG 2.2 AA in both themes, accessibility statement published.
- [ ] No session replay or pixels without a real need; chat notice before first message.
- [ ] Privacy policy with all six CalOPPA items and an effective date.
- [ ] Texts: prior express written consent, safe universal window, STOP honored, A2P 10DLC registered.
- [ ] Emails: postal address, opt-out honored within 10 business days, honest subject lines.
- [ ] No fake reviews, no fictitious "was" prices, guarantee terms one click away.

## Claims section

**As of 2026-10-27. Not legal advice.** Sources for the US rules are in the US rules section.

### The core rule: only promise what is automatic

A public promise is safe when it stays true **without anyone remembering to do something**. Prefer:
- promises enforced by software settings ("STOP removes the number automatically"),
- promises enforced by a written process with an owner and a check,
- or no promise at all.

Every public promise goes in `COMMITMENTS.md` with: exact wording, pages where it appears, how it is guaranteed to stay true, and who owns it. Before publishing any copy, compare it against `COMMITMENTS.md`. Refuse to publish copy that contradicts it, and ask the user which one should change.

### Guarantees

- Write **one exact wording** and use it everywhere, word for word.
- **Never show a short version without its limits.** "Results or we keep working" is not acceptable; "10 sign-ups within 60 days of launch, or we keep working for up to 30 more days at no extra cost" is.
- Put a small "Guarantee terms" link next to every short version, pointing to the full conditions (for example `/terms#guarantee`). The FTC expects ads that mention a guarantee to tell people where the full terms are ([16 CFR 239.2](https://www.law.cornell.edu/cfr/text/16/239.2)).
- Define every key term (for example what counts as a "returned member" or a "lead") once, and reuse the exact definition everywhere.
- The full terms must cover: preconditions (for example minimum list size, approval deadlines), how results are confirmed, what happens if the target is still not met, and whether there are refunds.
- Headings are copy too. A heading like "10 back or we keep going" is a short guarantee without limits. Use a neutral heading and put the exact wording in the body.

### Prices

- If the owner does not want prices on the site, write "quoted on the call" and never show a number, including in meta descriptions and structured data.
- **No fake reference prices.** "Founding rate", "launch price", "was $X, now $Y" and "price goes up after the next 3 clients" all imply a real, higher regular price. Under [16 CFR 233.1](https://www.law.cornell.edu/cfr/text/16/233.1) a former price is deceptive if it is fictitious. Only use these if the higher price really exists and is really charged. Otherwise delete them.

### Results, statistics and timing

- No statistic without a source the user can show you. "Most members drift away" is an unsourced statistic. Rewrite as clear opinion ("We believe ...") or remove it.
- Do not write "In our experience" for a business that has no clients yet.
- Do not call an assumption "conservative" unless you can point to the benchmark.
- Speed claims ("replies in seconds") need proof on every channel. Otherwise use a safe range ("within minutes").
- Timing claims must match reality, including outside dependencies (for example "Texts start once carrier registration is approved, which can take a few weeks").
- Calculators: label inputs as the visitor's own assumptions and add "A what-if, not a forecast or a guarantee".

### Testimonials and reviews

- Only real testimonials from real customers, with permission, reflecting their actual experience. The FTC's Consumer Reviews and Testimonials Rule bans fake reviews and testimonials, review buying conditioned on sentiment, undisclosed insider reviews and review suppression ([FTC Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)).
- No testimonials yet? Leave the section out. Do not write placeholders that look real.
- Sample messages, chats and dashboards must be captioned as examples, with fictional names.

### Legal assurances

- Never tell visitors something is "legal" without qualification. Write the actual rule and add "This is not legal advice". Example: "Yes, when members gave prior express written consent to receive marketing texts. We only text members whose signup records show that consent. Everyone else gets email only. This is not legal advice."
- Never write "compliant", "fully protected", or any claim that the site cannot be sued or fined.

### Data-handling promises

Common ones, and how to keep them true:

| Promise | Keep it true by |
|---|---|
| "We delete your list within N days" | A dated deletion task per client, and a record that it was done. |
| "Only we and [software] can access it" | Name the software. Do not say "only our team" if a vendor stores it. |
| "You approve every message before it sends" | A sign-off step in the workflow; nothing is scheduled before approval. |
| "STOP removes you immediately" | The texting tool's automatic opt-out handling, tested. |
| "Texts only between X and Y" | Sending windows set in the tool per recipient time zone. |

### Before and after table

For every copy change, show the user:

| Page | Before | After | Reason |
|---|---|---|---|

Then search the built site for the old wording to confirm none is left.

## Legal pages section

**As of 2026-10-27. Not legal advice. These are starting templates. A lawyer must review them before the business relies on them.**

The legal requirement behind each item, with its source link, is in the US rules section (CalOPPA, FTC, CCPA) and website-shield-eu.md (GDPR Art. 13, ePrivacy, e-Commerce Art. 5, national identity rules, EAA).

Rules for every legal page:
- Visible "Last updated [date]" at the top.
- Linked from the **footer of every page**, one click away.
- Written in plain language. Short sentences.
- Placeholders in square brackets for anything you do not know: `[FULL LEGAL NAME]`, `[TAX ID]`, `[CONTACT ADDRESS]`, `[EMAIL PROVIDER]`, `[RETENTION PERIOD]`, `[NOTICE PERIOD]`, `[GUARANTEE TERMS]`. Never guess these.
- Must match what the site really does. If the audit found no trackers, say so. If a booking embed sets a cookie, say which.
- Keep a source-only note at the top of each source file (for example `<!-- REVIEW BY LAWYER BEFORE FIRST CLIENT -->`) and strip it from the published HTML in the build step.

### Which pages each region needs

| Page | US | EU |
|---|---|---|
| Privacy policy | Yes (CalOPPA, see the US rules section) | Yes (GDPR Art. 13, see website-shield-eu.md) |
| Cookie policy | Recommended | Yes, if anything is stored on the device |
| Legal notice / identity page | Optional | Yes (e-Commerce Art. 5 and national rules) |
| Terms of service | Yes if you sell services or products | Yes if you sell services or products |
| Accessibility statement | Recommended | Recommended (see the EAA notes in website-shield-eu.md) |
| Data and compliance page | Recommended if you handle client or customer lists | Recommended |

### Privacy policy template outline

1. **Who is responsible**: business or trading name, owner or company name, contact email; link to the identity page for full details. (EU: controller identity and contact; US: who operates the site.)
2. **What we collect and why**, one block per form or feature found in the audit: what is collected, purpose, legal basis (EU).
3. **Things that collect nothing**, stated plainly (for example a calculator that runs in the browser).
4. **Recipients**: name each real provider found in the audit (booking tool, email provider, host, any embed and what it loads).
5. **Transfers** outside the EU and the safeguard used (EU).
6. **How long we keep it**: `[RETENTION PERIOD]` per purpose.
7. **Your rights** and how to use them; reply time; right to complain to the supervisory authority (EU, name it).
8. **US residents**: whether you sell or share personal information (only say "we do not" if true); how to request deletion; how the site responds to Do Not Track; whether third parties track visitors across sites (CalOPPA).
9. **Client or customer data you process for others** (if any): you act as processor on the client's instructions under a data processing agreement; what you do and never do with it.
10. **Children**: not directed at children (if true).
11. **Changes**: how you will notify people; effective date.

### Cookie policy template outline

1. The short version: what kinds of storage the site uses, and whether there is a banner and why.
2. A table: name, set by, purpose, how long, type (strictly necessary, preference requested by the user, analytics, marketing). One row per real item found in the audit, including those set by embeds.
3. Third-party embeds: what they load and what they may set when used.
4. Why there is (or is not) a banner.
5. How to delete or block them.

On phones, make tables stack into labelled rows instead of scrolling sideways.

### Terms of service template outline

1. Who we are (link to the identity page; no ID numbers here).
2. Services offered and what is confirmed in writing before work starts.
3. Price and payment: how prices are quoted, when payment is due, taxes. Never state a price on the site if the user decided not to.
4. Guarantee: the exact public wording, the definition of any key term, and `[GUARANTEE TERMS]` (conditions, what happens if the target is not met, refunds or not). Give this section an anchor (for example `#guarantee`) so every short guarantee on the site can link to it.
5. Client responsibilities (for example lawful lists and consent records).
6. Your responsibilities (link to the data and compliance page).
7. Results disclaimer: no promise beyond the guarantee.
8. Limitation of liability (cap, no indirect losses, nothing limits liability that cannot be limited by law).
9. Ending the service: `[NOTICE PERIOD]`.
10. Governing law and courts.
11. Changes.

### Accessibility statement template outline

1. Goal: WCAG 2.2 AA, in light and dark mode.
2. What has been done (keyboard access, focus rings, skip link, contrast, labels, reduced motion, no overlay).
3. How and when it was tested (tools and date).
4. Known limitations (for example a third-party embed) and an alternative way to get the service.
5. How to report a barrier (email) and what happens next.

## Security section

**As of 2026-10-27.** These are practical defaults, not a full security review. Header behaviour can change between browser versions; recheck the linked documentation.

### 1. Secrets scan (do this first)

Search every file in the project, including build output and scripts, for:
- `apiKey`, `api_key`, `api-key`, `secret`, `password`, `token`, `access_token`, `Bearer `
- provider key prefixes such as `sk_live`, `sk_test`, `sk-`, `pit-`, `AIza` (Google), `ghp_` / `gho_` (GitHub)
- webhook URLs and private API hosts of CRMs and payment tools
- `.env` files and anything that looks like a private key block

Rules:
- A secret in front-end code is public, even if the file is minified. **If you find one, tell the user immediately so they can revoke it at the provider**, then move the call to a server function or remove it.
- Public identifiers are not secrets: a booking widget ID, a publishable analytics ID, an IndexNow key file. Say so, so the user does not panic.
- Keep `.env*` and local caches out of version control (see section 5).

### 3. Security headers

Set these on every response (for example in the host's config file):

| Header | Value | Why |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000` | Browsers only use HTTPS for the domain. Add `includeSubDomains` only if every subdomain serves HTTPS. |
| `X-Content-Type-Options` | `nosniff` | Stops browsers guessing file types. |
| `X-Frame-Options` | `DENY` | Stops other sites framing yours (clickjacking). Use `SAMEORIGIN` only if the site frames itself. |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limits what is shared with other sites. |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | Turns off powerful features the site does not use. |
| `Content-Security-Policy` | see below | Controls which scripts, frames and other resources may load. |

Reference: [MDN HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers).

### 4. Content-Security-Policy: report-only first, then enforce

1. **Build the policy from measured data.** Use the per-page list of third-party domains from the audit (loaded in a real browser). Typical shape for a static site with one booking embed:
   ```
   default-src 'self';
   script-src 'self' 'sha256-<hash of each inline script>' https://<embed script host>;
   style-src 'self' 'unsafe-inline';
   img-src 'self' data:;
   font-src 'self';
   connect-src 'self';
   frame-src https://<embed host>;
   object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'
   ```
2. **Allow your own inline scripts by hash, not by `'unsafe-inline'`.** Compute `sha256` of each inline `<script>` body and add `'sha256-...'`. Generate the hashes in the build step from the built pages, so the policy can never drift out of date when a script changes.
3. **Start with `Content-Security-Policy-Report-Only`.** It reports violations but blocks nothing. Note: report-only cannot be set with a `<meta>` tag, and reports are only sent to a server if you add a `report-to` directive; without one, violations still appear in the browser console and as `securitypolicyviolation` events. Source: [MDN, Content-Security-Policy-Report-Only](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only).
4. **Test every page, including embeds fully loaded** (for example pick a date in a booking calendar), and collect violations in a headless browser.
5. **Run a control test.** Inject a deliberate inline script and an image from an outside domain. The test must report both. If it reports nothing, your test is broken, not your site clean.
6. **Enforce only when the live site shows zero violations on every page.** Switch the header name to `Content-Security-Policy`, deploy, and recheck that forms, embeds, theme toggles and menus still work. Roll back at once if anything breaks.
7. **Hashes and line endings:** browsers normalise CRLF line endings to LF before hashing inline scripts ([WHATWG Infra, normalize newlines](https://infra.spec.whatwg.org/#normalize-newlines)). Compute hashes on LF-normalised text, or files built on Windows will appear to "fail" in your own checks while working in the browser. See the gotchas section.

### 5. Version control and backups

- Use git. Commit once per phase with a clear message.
- Add a `.gitignore` before the first commit, covering at least: `.env`, `.env.*`, provider caches (for example `.firebase/`), `node_modules/`, and any private files that must never be published (for example a paid ebook or client data).
- Before pushing, run `git status` and `git ls-files` and confirm none of those are tracked.
- Back up to a **private** repository. Confirm visibility after creating it (for example `gh repo view <name> --json visibility` must say `PRIVATE`). If the repo will contain a legal page with personal ID numbers, it must never be public.
- If the repository name is already taken, stop and ask the user. Never force-push over an existing repository.
- GitHub turns on secret scanning and push protection by default for new public repositories owned by personal accounts ([GitHub changelog, 11 March 2024](https://github.blog/changelog/2024-03-11-secret-scanning-and-push-protection-are-enabled-by-default-on-new-public-repositories/)). Private repos may not have this, so your own secrets scan still matters.

## DNS safety section

**As of 2026-10-27.** DNS mistakes can take a site offline or stop email for days. This skill never changes DNS itself. It tells the user exactly what to add, and the user makes the change.

### Records you must never touch

Tell the user in plain words: **only add the records listed. Do not edit or delete anything else.** In particular:

| Record | Why it matters |
|---|---|
| `MX` | Email delivery. Delete or change these and email stops. |
| `TXT` with `v=spf1 ...` | Tells receivers which servers may send your email. Breaking it sends your mail to spam. |
| `TXT` or `CNAME` for DKIM (often `google._domainkey`, `selector1._domainkey` and similar) | Signs your email. |
| `TXT` at `_dmarc` | Email authentication policy. |
| `TXT` verification records (for example `google-site-verification=...`, `hosting-site=...`, other `*-verification`) | Prove ownership to Google, the host and other tools. Removing them can break the site or a service. |
| Apex `A` / `AAAA` records that currently serve the live site | Change these and the site goes offline. |

## Hosting section

**As of 2026-10-27.** Hosting plans and limits change often. Check each provider's current pricing page before advising the user.

### The risk in plain words

A traffic flood (a DDoS, a bot, or an accidental loop) used to just take a site offline. On pay-as-you-go cloud plans it can instead **run up a large bill** while the site stays up. Researchers call this a "Denial of Wallet" attack. Source: [Kelly, Glavin and Barrett, "Denial of Wallet: Defining a Looming Threat to Serverless Computing", 2021](https://arxiv.org/abs/2104.08031).

For a small business site the defence is simple: **prefer plans that stop instead of bill, set budget alerts where they do not, and keep the site static where possible.**

### Budget alerts do not stop spending

- Google Cloud budgets **only send alerts**: "Setting an alerts-only budget doesn't automatically cap Google Cloud or Google Maps Platform usage or spending." Default thresholds are 50%, 90% and 100% of actual spend, emailed to billing account administrators and users. Source: [Google Cloud, Create, edit, or delete budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).
- Always tell the user this in plain words: **an alert emails you; it does not switch anything off.**

## Gotchas section

**As of 2026-10-27.** Tool behaviour changes between versions; retest on your own setup.

These are problems that came up while taking a real small business site through this process (static site, Python build script, Firebase Hosting, third-party booking embed, built on Windows). Each one wasted time or nearly caused a false result. Check for them early.

### 1. Windows line endings make CSP hashes look wrong

**Symptom:** you hash each inline script in the built HTML and compare with the CSP header. They do not match, yet the browser reports no violations and the scripts run.
**Cause:** files written on Windows contain CRLF line endings. Browsers normalise CRLF to LF before hashing ([WHATWG Infra, normalize newlines](https://infra.spec.whatwg.org/#normalize-newlines)), so the browser's hash matches your header but a raw-bytes hash of the file does not.
**Fix:** compute hashes from the in-memory text with LF line endings (in the build step, before writing files), and normalise CRLF to LF in any checking script.

### 2. The local emulator may ignore custom headers

**Symptom:** security headers and CSP are in the host config, but local tests show none of them.
**Cause:** in the project this came from, the hosting emulator served files without applying any custom headers from the config, not even cache headers.
**Fix:** to test CSP locally, intercept each page request in a headless browser and serve it with the exact headers from the config. Then check the real headers again on the live site after deploy.

### 3. "Zero violations" can mean a broken test

**Symptom:** the CSP test reports zero violations everywhere.
**Risk:** the listener may not be attached, or the header may not be applied.
**Fix:** run a **control test**: on one page, inject an inline script and an image from an outside domain. The test must report both. Only then trust the zero.

### 4. Headless Chrome may report "reduce motion"

**Symptom:** animations, or code that only runs when motion is allowed, appear broken in automated tests.
**Cause:** the test machine had system animations turned off, so the browser reported `prefers-reduced-motion: reduce` and the site correctly skipped the animation.
**Fix:** emulate the media feature explicitly in tests, once with `reduce` and once with `no-preference`, and check both.

### 5. Old preview deploys keep serving old claims

**Symptom:** you fix a claim on the live site, but a preview or staging URL still shows the old wording, and anyone with the link can see it.
**Fix:** list preview channels after a copy change and delete the ones you no longer need. Confirm the old URL returns 404.

### 6. Preview deploys can trigger "live site" hooks

**Symptom:** a post-deploy script (for example one that notifies search engines) runs on preview deploys too, pinging search engines for pages that still show old content.
**Fix:** make the hook check that the live pages match the build before it runs, and skip otherwise.

### 7. Build steps that append config blocks duplicate them

**Symptom:** each build adds another copy of the same header block to the host config.
**Fix:** when a build step writes into a config file, have it remove its own previous blocks first, then write fresh ones. Run the build twice and confirm the config is unchanged.

### 8. Third-party embeds bring their own third parties

**Symptom:** the site "has no trackers", but one page sets a cookie and contacts Google.
**Cause:** a booking calendar embed loaded its own scripts, a bot-protection cookie (Cloudflare `__cf_bm`), Google Fonts and files from Google Cloud Storage.
**Fix:** measure network requests and cookies per page with the embed fully loaded (pick a date, open a step). Disclose what the embed loads in the privacy and cookie policies, or load it only after a click if the owner prefers. It also lowers some Lighthouse best-practices scores (third-party cookies), which you cannot fix from your own code; explain this rather than chase it.
