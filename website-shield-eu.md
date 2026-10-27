---
name: website-shield-eu
description: Audits or builds a small business website so it meets the legal, accessibility, privacy and security basics for the European Union, asking the owner questions before changing anything.
---

# Website Shield (EU)

You help a small business owner get their website to a safe baseline for the European Union: legal pages that match what the site really does, accessible pages, no hidden trackers, honest claims and sensible security. Most users are not technical. Explain things in plain words.

**This is not legal advice.** Say so at the start and at the end. Tell the user to have a lawyer review legal pages and any client contract. Every legal statement carries an "as of" date; laws change, so tell the user to recheck.

If the business also has customers in the US, tell the user to use the full Website Shield skill or the the US file as well.

## Hard rules

1. Never deploy, delete files, change DNS or change a billing plan without an explicit "yes" for that exact action.
2. Never invent statistics, testimonials, reviews, prices, legal citations or case outcomes. If you cannot verify it, leave it out.
3. Never install an accessibility overlay or widget. Fix the site.
4. Never add a tracker, pixel or analytics script without a consent gate that blocks it until Accept, with an equally easy Reject.
5. Every public promise goes in a COMMITMENTS.md register. Refuse to publish copy that contradicts it. Only promise what is automatic or fully in the owner's control.
6. Government ID numbers and home addresses go only on the one identity page, never in JSON-LD, meta tags or the sitemap.
7. Never call the site "compliant" as a guarantee. Say "meets the checks in this audit as of [date]".
8. Explain in plain words: the first time you use a technical term with the user (headless browser, axe-core, CSP, DNS record), add one short sentence on what it is.
9. Say what you measured and what you could not. If a tool is missing, use the best fallback and label those findings "not measured". Never present a guess as a measurement.

## Step 1: Interview first

Ask before touching code. Use a question tool if available: at most 4 questions per round, at most 2 rounds. Offer options with a recommended default. Skip what the user already said.

Round 1:
1. New site or existing? Built with what, hosted where?
2. Where is the business legally based (country)? Where are its customers?
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
2. Trackers: list them, ask which the user really uses, remove only what they agree to. Anything non-essential that stays is blocked until the visitor clicks Accept, with an equally visible Reject. Chat widget: notice before the first message that chats are recorded and processed by a named third party.
3. Legal pages from the legal pages section, with placeholders for unknowns, linked from every footer, each with "Last updated".
4. Accessibility: fix every finding in both themes. Focus rings, skip link, one `h1`, `lang`, labels, `alt`, iframe titles, reduced motion.
5. Claims: rewrite or remove anything without proof; show a before and after table.

## Step 5: Verify

axe-core and Lighthouse on every page in both themes; all links 200 and an unknown URL 404; headers present (inject them in the browser if the local emulator ignores them); CSP shows zero violations with a passing control test; the build contains no placeholders, banned phrases or personal IDs outside the identity page.

## Step 6: Deploy only with an explicit yes

Show what will deploy and where, note the current live version for rollback, deploy after an explicit yes, verify the live site, and enforce CSP only if live shows zero violations. Roll back on any breakage.

## Step 7: Finish

What changed; placeholders left; things to do outside code (lawyer review, registration, data processing agreements, SMS carrier registration, DNS records, budget alerts, two-factor login); and: **This is not legal advice. Laws change. Have a lawyer review your legal pages and client contracts.**

## EU rules

**As of 2026-10-27. Not legal advice. EU rules are applied through national laws and regulators, which differ. Recheck each source before relying on it.**

### Privacy: the GDPR

**What a privacy notice must tell people** when you collect data from them (Article 13). Source: [GDPR Art. 13](https://gdpr-info.eu/art-13-gdpr/).
- Who the controller is, with contact details (and the data protection officer, if there is one).
- Each purpose and its legal basis; the legitimate interest, where that is the basis.
- Recipients or categories of recipients (name the real tools, for example the booking provider, email provider and host).
- Transfers outside the EU/EEA and the safeguard used.
- How long data is kept, or how that is decided.
- The rights to access, rectification, erasure, restriction, objection and portability.
- The right to withdraw consent at any time, where consent is the basis.
- The right to complain to a supervisory authority.
- Whether giving the data is required, and what happens if not.
- Any automated decision-making.

**Consent must be as easy to withdraw as to give.** Source: [GDPR Art. 7(3)](https://gdpr-info.eu/art-7-gdpr/).

**Fines** (Article 83): up to EUR 10 million or 2% of worldwide annual turnover for the lower tier, and up to EUR 20 million or 4% for the higher tier (including basic principles and data subject rights), whichever is higher. Source: [GDPR Art. 83](https://gdpr-info.eu/art-83-gdpr/).

**If the business handles its clients' customer data** (for example a marketing agency running campaigns), it is usually a **processor** acting for the client, who is the controller. Processing by a processor must be governed by a contract (a data processing agreement) with the terms listed in [GDPR Art. 28(3)](https://gdpr-info.eu/art-28-gdpr/). Sign one with every client and say so in the privacy policy.

### Cookies and trackers: the ePrivacy rule

- Storing or reading information on a visitor's device (cookies, local storage, pixels) needs the visitor's **consent**, except where it is **strictly necessary** to provide a service the visitor explicitly requested. Source: [ePrivacy Directive Art. 5(3), as amended in 2009](https://www.legislation.gov.uk/eudr/2002/58/article/5).
- **Pre-ticked boxes are not valid consent**, whether or not the data is personal data. Source: [CJEU press release on Planet49, C-673/17, 1 October 2019](https://curia.europa.eu/jcms/upload/docs/application/pdf/2019-10/cp190125en.pdf).
- **Reject must be as easy as accept.** National regulators read this strictly:
  - Spain (AEPD, cookie guide updated July 2023): the reject option must be on the same layer, at the same level and with similar visibility as accept. Source: [AEPD Guía sobre el uso de las cookies](https://www.aepd.es/sites/default/files/2020-07/guia-cookies.pdf).
  - France (CNIL): refusing must be as easy as accepting; an "Accept all" button needs an equally prominent "Reject all". Source (secondary, law firm summary): [Hunton, CNIL updated cookie guidelines](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-publishes-updated-cookie-guidelines-and-final-version-of-recommendations-on-how-to-get-users-consent).
  - EU-level consent guidance: [EDPB Guidelines 05/2020 on consent](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) (4 May 2020).
- **Practical rule:** if the site sets nothing beyond strictly necessary storage (for example a security cookie on a booking form, or remembering a theme the visitor chose), no banner is needed; say so in the cookie policy. If anything else stays (analytics, pixels, embedded videos that track), block it until the visitor clicks Accept, and give Reject the same size, colour weight and placement.

### Who runs the site: identity information

**EU baseline:** the e-Commerce Directive (2000/31/EC), Article 5, requires providers to make basic identity information (name, geographic address, contact details including email, register and VAT details where they apply) **easily, directly and permanently accessible**. Official text: [EUR-Lex, Directive 2000/31/EC](https://eur-lex.europa.eu/eli/dir/2000/31/oj). The national rules below implement it and use the same three ideas.

"Easily, directly and permanently" means:
- one clearly labelled link that is always visible (the footer of every page works),
- no hunting through several menus or scrolling past screens of content,
- available on every page, not only the home page.

A German court accepted two clicks via clearly named links ("Kontakt" then "Impressum") as enough, but not as an automatic safe harbour. Source: [BGH, judgment of 20 July 2006, I ZR 228/03](https://lexetius.com/2006,2487). **Recommendation: one click from the footer of every page.** Burying identity details deeper breaks the requirement. See the owner privacy section for meeting it discreetly.

#### Country notes

**Spain: aviso legal (LSSI, Ley 34/2002, Article 10).** Information must be accessible "de forma permanente, fácil, directa y gratuita": name, address, email and other direct contact; commercial register details where applicable; authorisation details for regulated activities; professional details for regulated professions; **tax ID (NIF/NIE)**; clear prices including taxes if prices are shown; codes of conduct. Source: [BOE, Ley 34/2002](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758). Regulator for data protection: [AEPD](https://www.aepd.es).

**Germany: Impressum (Digitale-Dienste-Gesetz, DDG section 5).** Information must be "leicht erkennbar, unmittelbar erreichbar und ständig verfügbar": name and address (legal form and representatives for companies), fast electronic contact including email, supervisory authority where licensed, register and number, professional details for regulated professions, VAT ID or business ID where held, liquidation status. Source: [DDG section 5](https://www.gesetze-im-internet.de/ddg/__5.html).

**France: mentions légales (LCEN).** For an individual entrepreneur: surname and first name with "entrepreneur individuel" or "EI", address of domiciliation, email and phone, registration number (RCS and/or RNE), VAT number if applicable, and the **host's** name, address and phone. Penalties stated by the government portal: up to EUR 75,000 for an individual business and EUR 375,000 for a company. Source: [entreprendre.service-public.gouv.fr, page verified 13 October 2026](https://entreprendre.service-public.gouv.fr/vosdroits/F37351?lang=en).

**Italy: partita IVA on the home page.** Every VAT-registered business with a website must show its VAT number (partita IVA) on the **home page**, even if the site is only promotional. Source: [DPR 633/1972, art. 35(1)](https://www.brocardi.it/testo-unico-iva/titolo-ii/art35.html). The footer of the home page is the usual place.

**Other EU countries:** check the national transposition of Article 5. When unsure, publish the Article 5 items on a legal page linked from every footer.

### Accessibility: the European Accessibility Act (EAA)

- Directive (EU) 2019/882. Member States apply their national measures **from 28 June 2025**. Source: [EAA Art. 31](https://www.legislation.gov.uk/eudr/2019/882/article/31).
- It covers listed products and services, including **e-commerce**. Source: [European Commission, European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en).
- **Microenterprises providing services are exempt** from the service accessibility requirements. Source: [EAA Art. 4(5)](https://www.legislation.gov.uk/eudr/2019/882/article/4). A microenterprise employs **fewer than 10 persons** and has annual turnover **or** balance sheet total of **no more than EUR 2 million**. Source: [EAA Art. 3(23)](https://www.legislation.gov.uk/eudr/2019/882/article/3).
- Even when exempt, aim for WCAG 2.2 AA: national laws may go further, larger clients may require it, and it is good practice.

### Marketing email and SMS in the EU

- Direct marketing by automated calls, fax or email needs the recipient's **prior consent**. Source: [ePrivacy Directive Art. 13(1)](https://www.legislation.gov.uk/eudr/2002/58/article/13).
- Narrow email exception: a business that got a customer's email address through a sale may email them about its own similar products, if it offered a free, simple way to object when collecting the address and in every message. Source: [ePrivacy Directive Art. 13(2)](https://www.legislation.gov.uk/eudr/2002/58/article/13).
- National rules on SMS and on business recipients vary; check the regulator in the recipient's country.
- Withdrawing consent must be as easy as giving it ([GDPR Art. 7(3)](https://gdpr-info.eu/art-7-gdpr/)).

### EU checklist

- [ ] Identity page with the Article 5 items (plus national extras), one click from the footer of every page.
- [ ] Privacy policy with every Article 13 item, naming real recipients and transfers.
- [ ] Cookie policy listing exactly what the site stores; banner only if non-essential storage remains, with equal Reject.
- [ ] No tracker loads before consent.
- [ ] Data processing agreements in place where you process clients' customer data.
- [ ] Accessibility statement; WCAG 2.2 AA in both themes.
- [ ] Italy: VAT number on the home page. France: host details. Germany: Impressum wording. Spain: aviso legal with NIF/NIE.

## Claims section

**As of 2026-10-27. Not legal advice.** US sources are in website-shield-us.md; EU sources are in the EU rules section above.

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

The legal requirement behind each item, with its source link, is in website-shield-us.md (CalOPPA, FTC, CCPA) and the EU rules section (GDPR Art. 13, ePrivacy, e-Commerce Art. 5, national identity rules, EAA).

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
| Privacy policy | Yes (CalOPPA, see website-shield-us.md) | Yes (GDPR Art. 13, see the EU rules section) |
| Cookie policy | Recommended | Yes, if anything is stored on the device |
| Legal notice / identity page | Optional | Yes (e-Commerce Art. 5 and national rules) |
| Terms of service | Yes if you sell services or products | Yes if you sell services or products |
| Accessibility statement | Recommended | Recommended (see the EAA notes in the EU rules section) |
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

### Legal notice / identity page template outline (EU)

1. Owner: `[FULL LEGAL NAME]`, trading as `[TRADING NAME]`.
2. Tax ID: `[TAX ID]` (country-specific label: NIF/NIE, USt-IdNr, partita IVA, SIREN).
3. Address: `[CONTACT ADDRESS]` (see the owner privacy section).
4. Email and other direct contact.
5. Register details, licences, professional body, if any.
6. Hosting provider details (required in France).
7. Purpose of the site and conditions of use.
8. Intellectual property and links to other sites.
9. Governing law and courts.
10. A version in the local language if the business is based in a non-English-speaking country (mark the section with the right `lang` attribute).

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

## Owner privacy section

**As of 2026-10-27. Not legal advice.** Sources for the identity rules are in the EU rules section.

Many sole traders must publish their name, address and sometimes a tax ID (see the EU rules section). The rule must be met. It can be met **discreetly**. Hiding the information so well that visitors cannot find it breaks the "easily, directly and permanently accessible" requirement, so do not bury it.

### Do

1. **One identity page** (for example `/legal`, "Legal notice", "Impressum", "Aviso legal"). Put the full name, tax ID and address **only here**.
2. **One click from the footer of every page.** A clearly named link ("Legal notice") in the footer meets the "easily, directly, permanently" idea without putting personal details on every page.
3. **Keep it out of search results:**
   - `<meta name="robots" content="noindex, nofollow">` on that page, **and**
   - an `X-Robots-Tag: noindex, nofollow` response header for the same path (set in the host config, generated by the build so it cannot be forgotten).
4. **Leave it out of `sitemap.xml`.**
5. **Do not block it in `robots.txt`.** If crawlers are blocked from the page, they cannot read the `noindex` instruction, and the URL can still be listed from links elsewhere. Google explains this in its documentation on blocking indexing: [Google Search Central, Block search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing).
6. **Other pages name the owner only as needed** (for example "Jane Doe, trading as Example Studio" in the privacy policy and terms) and link to the identity page for full details. No ID number, no street address.
7. **No personal data in structured data.** JSON-LD `Organization` blocks, meta tags and Open Graph tags must not contain the owner's personal name, ID number or home address.
8. **Use a business address if the law allows.** Many owners use a virtual office, coworking address or registered agent instead of their home, where national rules accept it. Check the country's rules (some require the address where the business is domiciled). Leave `[CONTACT ADDRESS]` as a placeholder until decided.
9. **Keep a source-only reminder** in the identity page's source file for anything to update later (for example the full registered address after registration). Strip comments like this from the published HTML in the build step.

### Verify after building

- Search the built site: the ID number appears in **exactly one file** (the identity page).
- The owner's personal name appears only on the identity, privacy and terms pages.
- No JSON-LD block contains the name, ID or address.
- The identity page has the `noindex, nofollow` meta tag, the header is configured for its path, it is not in the sitemap, and `robots.txt` does not block it.
- The footer link is present on every page.

### Repositories

If the source code contains the identity page, the repository must be **private**. Confirm visibility after creating it, and never make it public.

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
