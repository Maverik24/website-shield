# United States: website rules for small businesses

**As of 2026-10-27. Not legal advice. Laws and court decisions change; recheck each source before relying on it.**

Federal law sets a floor. States add their own rules, and the strictest rule that applies to a visitor or recipient wins. When in doubt, design for the strictest state.

## Accessibility: the ADA

- The Department of Justice says the ADA's requirements apply to everything a business open to the public offers, "including those offered on the web". Source: [DOJ, Guidance on Web Accessibility and the ADA, March 18, 2022](https://www.ada.gov/resources/web-guidance/).
- DOJ has **no regulation with detailed technical standards** for private businesses. It points to the Web Content Accessibility Guidelines (WCAG) and Section 508 as helpful guidance. Same source.
- Practical target: **WCAG 2.2 level AA**, tested in every theme the site offers (light and dark) and at phone and desktop widths.
- Do not use accessibility overlays or widgets. Fix the pages.
- Publish an accessibility statement with a way to report barriers (see `legal-pages.md`).

## Website tracking: California Invasion of Privacy Act (CIPA)

- Plaintiffs have used CIPA's wiretap section (Penal Code 631) and pen register section (638.51) against session replay tools, chat widgets and tracking pixels. Courts are split on many of these theories. Source (secondary, law firm summary): [Duane Morris, SB 690 stalls, CIPA liability remains, 2025](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html).
- Penal Code 637.2(a): a person injured may recover the greater of **$5,000 per violation** or three times actual damages. Source: [Cal. Penal Code 637.2](https://california.public.law/codes/penal_code_section_637.2).
- Practical rules for a small business site:
  - Remove session replay, heatmaps and ad pixels you do not truly need.
  - If a chat widget stays, show a notice **before the first message** that the chat is recorded and processed by a named third party.
  - Keep a list of every third-party domain each page loads (measured, not guessed).

## Texting: the TCPA and state rules

### Federal

- **Quiet hours:** no telephone solicitations to a residential subscriber "before the hour of 8 a.m. or after 9 p.m." in the recipient's local time. Source: [47 CFR 64.1200(c)(1)](https://www.law.cornell.edu/cfr/text/47/64.1200).
- **Consent for marketing:** autodialed or prerecorded marketing calls to wireless numbers need the called party's **prior express written consent**. Source: [47 CFR 64.1200(a)(2)](https://www.law.cornell.edu/cfr/text/47/64.1200). This skill treats every marketing text as covered by these rules, which is the cautious reading.
- **Damages:** $500 per violation, and a court may award up to three times that for willful or knowing violations. Source: [47 U.S.C. 227(b)(3) and (c)(5)](https://www.law.cornell.edu/uscode/text/47/227).
- **Carrier registration:** US carriers expect business texting from standard 10-digit numbers to be registered (A2P 10DLC) through the texting provider. Check the provider's documentation for current steps and timing, and do not promise a go-live date for texts until registration is approved.

### States with stricter hours (verified against the statute or enrolled bill)

| State | Allowed window (recipient local time) | Covers texts? | Source |
|---|---|---|---|
| Federal floor | 8 a.m. to 9 p.m. | Yes | [47 CFR 64.1200(c)(1)](https://www.law.cornell.edu/cfr/text/47/64.1200) |
| Florida | 8 a.m. to 8 p.m. | Yes (Florida's definition of a telephonic sales call includes text messages) | [Fla. Stat. 501.616(6)(a)](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.616.html), [Fla. Stat. 501.059(1)(j)](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.059.html) |
| Washington | 8 a.m. to 8 p.m. | Check with counsel | [RCW 80.36.390(8)](https://app.leg.wa.gov/rcw/default.aspx?cite=80.36.390) |
| Texas | Weekdays and Saturday 9 a.m. to 9 p.m.; Sunday noon to 9 p.m. | Yes, since SB 140 (effective September 1, 2025) | [Tex. Bus. & Com. Code 301.051(b)(2)](https://texas.public.law/statutes/tex._bus._&_com._code_section_301.051); SB 140: [Senate Research Center analysis](https://capitol.texas.gov/tlodocs/89R/analysis/doc/SB00140F.docx), [Morgan Lewis, 2025](https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages) |
| Maryland | 8 a.m. to 8 p.m. | Practitioners say yes | [Stop the Spam Calls Act, 2023 Ch. 413 (enrolled SB 90)](https://mgaleg.maryland.gov/2023RS/chapters_noln/Ch_413_sb0090E.pdf); effective January 1, 2024 |
| Oklahoma | 8 a.m. to 8 p.m. | Practitioners say likely; confirm with counsel | [HB 3168 (2022), enrolled](https://oklegislature.gov/cf_pdf/2021-22%20ENR/hB/HB3168%20ENR.PDF); Oklahoma Telephone Solicitation Act, 15 O.S. 775C.1 et seq. |

**Not verified against primary text, so not in the table:** Louisiana and several other states are reported by compliance vendors and law firms to ban marketing calls on Sundays and legal holidays. One source: [ALFA International / Leake Andersson, Louisiana compendium](https://www.alfainternational.com/wp-content/uploads/LA-Compendium-EDITED.pdf). The safe window below avoids those days anyway.

### Recommended default: the safe universal window

**Send marketing texts only on weekdays, 10 a.m. to 6 p.m. in the recipient's local time, never on Sundays or public holidays.** This sits inside every window in the table above and avoids the reported Sunday and holiday bans. It is a business choice, not a legal minimum, and it is the default this skill recommends.

Also:
- Only text people whose records show **prior express written consent** for marketing texts. Everyone else gets email only.
- Every text includes a way to opt out (for example "Reply STOP to opt out"), and STOP is honored immediately and permanently.
- Some states also cap how often you can contact the same person. Maryland's enrolled act limits solicitations to three per 24 hours on the same subject ([2023 Ch. 413](https://mgaleg.maryland.gov/2023RS/chapters_noln/Ch_413_sb0090E.pdf)); practitioners report similar caps in other states. Keep campaigns short and spaced out.

## Email: CAN-SPAM

From the [FTC CAN-SPAM Act compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business):
- Accurate "From", "To", "Reply-To" and routing information.
- No misleading subject lines.
- Identify the message as an ad.
- Include a valid physical postal address.
- Tell recipients how to opt out, and honor opt-outs within **10 business days**.
- You stay responsible for email sent on your behalf by a vendor.
- Penalty: up to **$53,088 per separate email** in violation (figure on the FTC page as of 2026-10-27).

## Claims, reviews and pricing: the FTC

- **Consumer Reviews and Testimonials Rule** (16 CFR Part 465), effective **October 21, 2024**. It prohibits, among other things: fake or false reviews and testimonials, buying reviews that must express a particular sentiment, undisclosed insider reviews, company-controlled "independent" review sites, review suppression, and fake social media influence indicators. Courts can impose civil penalties for knowing violations. Source: [FTC Q&A on the rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers).
- **Former price comparisons** (16 CFR 233.1): a "was" price is deceptive if it is fictitious, meaning it was not openly offered for a reasonably substantial period. This is why "founding rate" or "launch price" claims need a real, higher regular price behind them. Source: [16 CFR 233.1](https://www.law.cornell.edu/cfr/text/16/233.1).
- **Guarantee advertising** (16 CFR Part 239): ads that mention a guarantee should tell people where they can see the complete terms. Source: [16 CFR 239.2](https://www.law.cornell.edu/cfr/text/16/239.2).
- See `claims-and-commitments.md` for the wording rules this skill applies.

## Privacy policies: CalOPPA

[Cal. Bus. & Prof. Code 22575](https://california.public.law/codes/business_and_professions_code_section_22575) applies to commercial websites that collect personally identifiable information from California residents. The policy must:
1. List the categories of personal information collected and the categories of third parties it may be shared with.
2. Describe how visitors can review and request changes, if that is offered.
3. Say how visitors will be told about material changes.
4. Give an effective date.
5. Say how the site responds to browser "Do Not Track" signals.
6. Say whether other parties may collect information about the visitor's activity across sites.

## State comprehensive privacy laws (CCPA and others)

- The California Consumer Privacy Act applies to a for-profit business that meets **any one** of these:
  - annual gross revenue above **$26,625,000** (CPI-adjusted figure effective January 1, 2025; the statute's base figure is $25,000,000). Source: [CPPA CPI adjustment](https://cppa.ca.gov/regulations/cpi_adjustment.html).
  - buys, sells or shares the personal information of **100,000 or more** consumers or households a year.
  - earns **50% or more** of annual revenue from selling or sharing personal information.
  Source: [Cal. Civ. Code 1798.140(d)(1)](https://california.public.law/codes/civil_code_section_1798.140).
- Many other states have their own comprehensive privacy laws with different thresholds. Check the [IAPP US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/) for the current list.
- Many very small businesses are below these thresholds, but a clear privacy policy is still required by CalOPPA (above) and is good practice. Say "we do not sell or share personal information" only if it is true, including for any pixels and embeds.

## US checklist

- [ ] Accessibility: WCAG 2.2 AA in both themes, accessibility statement published.
- [ ] No session replay or pixels without a real need; chat notice before first message.
- [ ] Privacy policy with all six CalOPPA items and an effective date.
- [ ] Texts: prior express written consent, safe universal window, STOP honored, A2P 10DLC registered.
- [ ] Emails: postal address, opt-out honored within 10 business days, honest subject lines.
- [ ] No fake reviews, no fictitious "was" prices, guarantee terms one click away.
