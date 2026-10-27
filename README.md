# Website Shield

A free Claude skill that checks your small business website before you launch.

- Asks you a few questions first, then audits your site: hidden trackers, leaked keys, missing legal pages, accessibility in light and dark mode, and risky claims.
- Fixes things in safe phases, with your approval at every step. It never deploys or touches your DNS without a clear yes.
- Covers the US (ADA, CIPA, TCPA texting rules, CAN-SPAM, FTC) and the EU (GDPR, cookies, identity pages for Spain, Germany, France and Italy, the EU Accessibility Act), with sources and dates.

**Who it is for:** people building websites with AI (Claude, Cursor, Lovable, Bolt, Webflow, WordPress) who want a solid baseline without hiring an agency first.

## Pick a file

| File | Use it when |
|---|---|
| `website-shield/` (full skill) | You want everything. Loads only the parts your answers need. |
| `website-shield-us.md` | Your business and customers are only in the US. |
| `website-shield-eu.md` | Your business and customers are only in the EU. |

## What works where

- **Claude Code:** full audit (loads every page in a browser, accessibility tests in both themes, header and CSP checks) and fixes the code.
- **Claude app:** reviews code or pages you upload, writes legal pages, rewrites claims. Live browser tests will show as "not measured".
- **Webflow, WordPress, Wix and other site builders:** checks the live site where possible and gives you a step-by-step list of changes to make in your builder. It cannot edit the site for you.

## Install

**Claude Code**
1. Copy the `website-shield` folder to `~/.claude/skills/website-shield/` (on Windows: `C:\Users\<you>\.claude\skills\website-shield\`).
2. For a single-file version, create a folder such as `~/.claude/skills/website-shield-us/` and save the file inside it as `SKILL.md`.
3. Start a new session, or run `/reload-skills`.

Docs: [Claude Code skills](https://code.claude.com/docs/en/skills)

**Claude app (claude.ai or desktop)**
1. Go to **Customize > Skills**, click **+**, then **Upload a skill**.
2. Upload `website-shield.zip`.
3. Switch it on.

For a single-file version: put the file in a folder with the same name (for example `website-shield-us/`), rename the file to `SKILL.md`, zip the folder and upload the zip.

Docs: [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

## Try it

- "Audit my site before launch."
- "Build me a compliant landing page for my plumbing business in Texas."
- "My site is in Germany and sells to the US, check it."

## Not legal advice

This skill applies published rules and good practice, with sources and "as of" dates. Laws change and every business is different. Have a lawyer review your legal pages and client contracts before you rely on them.

Made by AWYX Media. Follow @awyxmediaagency on X for more free Claude skills.
