# Hosting costs, traffic floods and "denial of wallet"

**As of 2026-10-27.** Hosting plans and limits change often. Check each provider's current pricing page before advising the user.

## The risk in plain words

A traffic flood (a DDoS, a bot, or an accidental loop) used to just take a site offline. On pay-as-you-go cloud plans it can instead **run up a large bill** while the site stays up. Researchers call this a "Denial of Wallet" attack. Source: [Kelly, Glavin and Barrett, "Denial of Wallet: Defining a Looming Threat to Serverless Computing", 2021](https://arxiv.org/abs/2104.08031).

For a small business site the defence is simple: **prefer plans that stop instead of bill, set budget alerts where they do not, and keep the site static where possible.**

## Free plan vs paid plan

| Situation | What it means |
|---|---|
| Free plan with hard limits | Worst case: the site slows down or stops until the next cycle. No surprise bill. |
| Paid pay-as-you-go plan | Worst case: the bill grows with traffic until you notice. Needs alerts and, where offered, a hard cap. |

Before advising a plan change, check whether billing is enabled at all. On Google Cloud and Firebase you can read it with the Cloud Billing API (`billingInfo.billingEnabled`). If billing is off, tell the user "free plan, no budget needed" and stop.

## Budget alerts do not stop spending

- Google Cloud budgets **only send alerts**: "Setting an alerts-only budget doesn't automatically cap Google Cloud or Google Maps Platform usage or spending." Default thresholds are 50%, 90% and 100% of actual spend, emailed to billing account administrators and users. Source: [Google Cloud, Create, edit, or delete budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).
- Always tell the user this in plain words: **an alert emails you; it does not switch anything off.**

## Per host

**Firebase Hosting (Google)**
- Spark (no-cost) plan Hosting includes 10 GB storage and 360 MB/day data transfer. The Blaze plan bills beyond the no-cost amounts. Source: [Firebase pricing](https://firebase.google.com/pricing).
- On Blaze, create a Google Cloud budget with email alerts (see above). It will not cap spend.

**Vercel**
- Spend Management is available on Pro and Enterprise (Flexible Commitment). Setting a spend amount does not stop usage on its own; you must also enable **Pause Production Deployments** to stop serving when the amount is reached. Checks run every few minutes, so usage can continue briefly after the limit. Notifications at 50%, 75% and 100%. Source: [Vercel Spend Management docs](https://vercel.com/docs/spend-management).

**Netlify**
- Credit-based plans: the Free plan has 300 credits a month with a hard limit, no auto recharge, and "You'll never be charged for the Free plan". Paid plans can auto-recharge credit packs. Source: [Netlify, credit-based pricing plans](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), [Netlify pricing](https://www.netlify.com/pricing/).

**Cloudflare Pages**
- Requests to static assets are free and unlimited; requests that run Pages Functions count against the Workers plan quota. Source: [Cloudflare Pages Functions pricing](https://developers.cloudflare.com/pages/functions/pricing/).
- Free plan limits include 500 builds a month and 20,000 files per site. Source: [Cloudflare Pages limits](https://developers.cloudflare.com/pages/platform/limits/).

## Putting Cloudflare in front of another host

Routing a domain through Cloudflare's proxy can absorb floods before they reach a metered host. It is a bigger change than it looks:
- It changes DNS (nameservers or proxied records). Follow `dns-safety.md` and get explicit approval.
- Some hosts issue their own HTTPS certificates and may not like a proxy in front. Check the host's docs first.
- Do not do this as part of a routine compliance pass. Offer it as a separate, optional project.

## Checklist

- [ ] Know whether billing is enabled, and on which plan.
- [ ] Free plan with hard limits where possible.
- [ ] On paid plans: budget alerts at 50/90/100% and, where the host offers it, a pause or hard cap.
- [ ] Static pages wherever possible; avoid server functions that anyone can call in a loop.
- [ ] Tell the user plainly that alerts do not stop spending.
