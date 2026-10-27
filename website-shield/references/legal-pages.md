# Legal pages: what each must contain

**As of 2026-10-27. Not legal advice. These are starting templates. A lawyer must review them before the business relies on them.**

The legal requirement behind each item, with its source link, is in `us.md` (CalOPPA, FTC, CCPA) and `eu.md` (GDPR Art. 13, ePrivacy, e-Commerce Art. 5, national identity rules, EAA).

Rules for every legal page:
- Visible "Last updated [date]" at the top.
- Linked from the **footer of every page**, one click away.
- Written in plain language. Short sentences.
- Placeholders in square brackets for anything you do not know: `[FULL LEGAL NAME]`, `[TAX ID]`, `[CONTACT ADDRESS]`, `[EMAIL PROVIDER]`, `[RETENTION PERIOD]`, `[NOTICE PERIOD]`, `[GUARANTEE TERMS]`. Never guess these.
- Must match what the site really does. If the audit found no trackers, say so. If a booking embed sets a cookie, say which.
- Keep a source-only note at the top of each source file (for example `<!-- REVIEW BY LAWYER BEFORE FIRST CLIENT -->`) and strip it from the published HTML in the build step.

## Which pages each region needs

| Page | US | EU |
|---|---|---|
| Privacy policy | Yes (CalOPPA, see `us.md`) | Yes (GDPR Art. 13, see `eu.md`) |
| Cookie policy | Recommended | Yes, if anything is stored on the device |
| Legal notice / identity page | Optional | Yes (e-Commerce Art. 5 and national rules) |
| Terms of service | Yes if you sell services or products | Yes if you sell services or products |
| Accessibility statement | Recommended | Recommended (see the EAA notes in `eu.md`) |
| Data and compliance page | Recommended if you handle client or customer lists | Recommended |

## Privacy policy template outline

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

## Cookie policy template outline

1. The short version: what kinds of storage the site uses, and whether there is a banner and why.
2. A table: name, set by, purpose, how long, type (strictly necessary, preference requested by the user, analytics, marketing). One row per real item found in the audit, including those set by embeds.
3. Third-party embeds: what they load and what they may set when used.
4. Why there is (or is not) a banner.
5. How to delete or block them.

On phones, make tables stack into labelled rows instead of scrolling sideways.

## Legal notice / identity page template outline (EU)

1. Owner: `[FULL LEGAL NAME]`, trading as `[TRADING NAME]`.
2. Tax ID: `[TAX ID]` (country-specific label: NIF/NIE, USt-IdNr, partita IVA, SIREN).
3. Address: `[CONTACT ADDRESS]` (see `privacy-of-the-owner.md`).
4. Email and other direct contact.
5. Register details, licences, professional body, if any.
6. Hosting provider details (required in France).
7. Purpose of the site and conditions of use.
8. Intellectual property and links to other sites.
9. Governing law and courts.
10. A version in the local language if the business is based in a non-English-speaking country (mark the section with the right `lang` attribute).

## Terms of service template outline

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

## Accessibility statement template outline

1. Goal: WCAG 2.2 AA, in light and dark mode.
2. What has been done (keyboard access, focus rings, skip link, contrast, labels, reduced motion, no overlay).
3. How and when it was tested (tools and date).
4. Known limitations (for example a third-party embed) and an alternative way to get the service.
5. How to report a barrier (email) and what happens next.

## Data and compliance page outline (for businesses that handle lists)

1. What the list is used for, and never used for.
2. Where it is stored and who can access it (name the software).
3. Retention and deletion.
4. Texting rules (consent, opt-out, sending window, carrier registration).
5. Email rules (unsubscribe, postal address).
6. What the client controls (approval, pause, deletion).
7. A muted note: the client owns the list and consent records; this is not legal advice.

Every promise on this page must also be in `COMMITMENTS.md`.
