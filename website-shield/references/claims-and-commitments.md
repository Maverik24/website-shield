# Claims and commitments

**As of 2026-10-27. Not legal advice.** Sources for the US rules are in `us.md`.

## The core rule: only promise what is automatic

A public promise is safe when it stays true **without anyone remembering to do something**. Prefer:
- promises enforced by software settings ("STOP removes the number automatically"),
- promises enforced by a written process with an owner and a check,
- or no promise at all.

Every public promise goes in `COMMITMENTS.md` with: exact wording, pages where it appears, how it is guaranteed to stay true, and who owns it. Before publishing any copy, compare it against `COMMITMENTS.md`. Refuse to publish copy that contradicts it, and ask the user which one should change.

## Guarantees

- Write **one exact wording** and use it everywhere, word for word.
- **Never show a short version without its limits.** "Results or we keep working" is not acceptable; "10 sign-ups within 60 days of launch, or we keep working for up to 30 more days at no extra cost" is.
- Put a small "Guarantee terms" link next to every short version, pointing to the full conditions (for example `/terms#guarantee`). The FTC expects ads that mention a guarantee to tell people where the full terms are ([16 CFR 239.2](https://www.law.cornell.edu/cfr/text/16/239.2)).
- Define every key term (for example what counts as a "returned member" or a "lead") once, and reuse the exact definition everywhere.
- The full terms must cover: preconditions (for example minimum list size, approval deadlines), how results are confirmed, what happens if the target is still not met, and whether there are refunds.
- Headings are copy too. A heading like "10 back or we keep going" is a short guarantee without limits. Use a neutral heading and put the exact wording in the body.

## Prices

- If the owner does not want prices on the site, write "quoted on the call" and never show a number, including in meta descriptions and structured data.
- **No fake reference prices.** "Founding rate", "launch price", "was $X, now $Y" and "price goes up after the next 3 clients" all imply a real, higher regular price. Under [16 CFR 233.1](https://www.law.cornell.edu/cfr/text/16/233.1) a former price is deceptive if it is fictitious. Only use these if the higher price really exists and is really charged. Otherwise delete them.

## Results, statistics and timing

- No statistic without a source the user can show you. "Most members drift away" is an unsourced statistic. Rewrite as clear opinion ("We believe ...") or remove it.
- Do not write "In our experience" for a business that has no clients yet.
- Do not call an assumption "conservative" unless you can point to the benchmark.
- Speed claims ("replies in seconds") need proof on every channel. Otherwise use a safe range ("within minutes").
- Timing claims must match reality, including outside dependencies (for example "Texts start once carrier registration is approved, which can take a few weeks").
- Calculators: label inputs as the visitor's own assumptions and add "A what-if, not a forecast or a guarantee".

## Testimonials and reviews

- Only real testimonials from real customers, with permission, reflecting their actual experience. The FTC's Consumer Reviews and Testimonials Rule bans fake reviews and testimonials, review buying conditioned on sentiment, undisclosed insider reviews and review suppression ([FTC Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)).
- No testimonials yet? Leave the section out. Do not write placeholders that look real.
- Sample messages, chats and dashboards must be captioned as examples, with fictional names.

## Legal assurances

- Never tell visitors something is "legal" without qualification. Write the actual rule and add "This is not legal advice". Example: "Yes, when members gave prior express written consent to receive marketing texts. We only text members whose signup records show that consent. Everyone else gets email only. This is not legal advice."
- Never write "compliant", "fully protected", or any claim that the site cannot be sued or fined.

## Data-handling promises

Common ones, and how to keep them true:

| Promise | Keep it true by |
|---|---|
| "We delete your list within N days" | A dated deletion task per client, and a record that it was done. |
| "Only we and [software] can access it" | Name the software. Do not say "only our team" if a vendor stores it. |
| "You approve every message before it sends" | A sign-off step in the workflow; nothing is scheduled before approval. |
| "STOP removes you immediately" | The texting tool's automatic opt-out handling, tested. |
| "Texts only between X and Y" | Sending windows set in the tool per recipient time zone. |

## Before and after table

For every copy change, show the user:

| Page | Before | After | Reason |
|---|---|---|---|

Then search the built site for the old wording to confirm none is left.
