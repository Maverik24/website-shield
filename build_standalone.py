"""Builds website-shield-us.md and website-shield-eu.md from the files in website-shield/.

Run from this folder:  python build_standalone.py
Each output is one self-contained skill file. Keep each under 600 lines.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "website-shield"
REF = SRC / "references"
LIMIT = 600


def read(name):
    return (REF / name).read_text(encoding="utf-8")


def demote(md, levels=1):
    """Push every heading down so each reference sits under one H2 in the combined file."""
    return re.sub(r"^(#+) ", lambda m: "#" * min(6, len(m.group(1)) + levels) + " ", md, flags=re.M)


def sections(md, keep):
    """Keep only the H2 sections (## Title) whose title starts with one of `keep`, plus the intro."""
    parts = re.split(r"(?m)^(?=## )", md)
    out = [parts[0]]
    for p in parts[1:]:
        title = p.splitlines()[0][3:].strip()
        if any(title.lower().startswith(k.lower()) for k in keep):
            out.append(p)
    return "".join(out)


def gotchas(md, count):
    parts = re.split(r"(?m)^(?=## \d+\. )", md)
    return "".join(parts[: count + 1])


def fix_links(md, region):
    """References to other files become references to sections of this file."""
    names = {
        "us.md": "the US rules section",
        "eu.md": "the EU rules section",
        "security.md": "the security section",
        "hosting-and-ddos.md": "the hosting section",
        "dns-safety.md": "the DNS safety section",
        "legal-pages.md": "the legal pages section",
        "claims-and-commitments.md": "the claims section",
        "privacy-of-the-owner.md": "the owner privacy section",
        "gotchas.md": "the gotchas section",
    }
    for f, label in names.items():
        md = md.replace(f"`references/{f}`", label).replace(f"`{f}`", label)
    # The other region's rules are not in this file: point to the other file instead.
    if region == "us":
        md = md.replace("the EU rules section", "website-shield-eu.md")
    else:
        md = md.replace("Sources for the US rules are in the US rules section.", "US sources are in website-shield-us.md; EU sources are in the EU rules section above.")
        md = md.replace("the US rules section", "website-shield-us.md")
    return md


WORKFLOW = """---
name: website-shield-{key}
description: Audits or builds a small business website so it meets the legal, accessibility, privacy and security basics for {region_long}, asking the owner questions before changing anything.
---

# Website Shield ({region_short})

You help a small business owner get their website to a safe baseline for {region_long}: legal pages that match what the site really does, accessible pages, no hidden trackers, honest claims and sensible security. Most users are not technical. Explain things in plain words.

**This is not legal advice.** Say so at the start and at the end. Tell the user to have a lawyer review legal pages and any client contract. Every legal statement carries an "as of" date; laws change, so tell the user to recheck.

If the business also has customers in {other}, tell the user to use the full Website Shield skill or the {other} file as well.

## Hard rules

1. Never deploy, delete files, change DNS or change a billing plan without an explicit "yes" for that exact action.
2. Never invent statistics, testimonials, reviews, prices, legal citations or case outcomes. If you cannot verify it, leave it out.
3. Never install an accessibility overlay or widget. Fix the site.
4. {tracker_rule}
5. Every public promise goes in a COMMITMENTS.md register. Refuse to publish copy that contradicts it. Only promise what is automatic or fully in the owner's control.
6. Government ID numbers and home addresses go only on the one identity page, never in JSON-LD, meta tags or the sitemap.
7. Never call the site "compliant" as a guarantee. Say "meets the checks in this audit as of [date]".
8. Explain in plain words: the first time you use a technical term with the user (headless browser, axe-core, CSP, DNS record), add one short sentence on what it is.
9. Say what you measured and what you could not. If a tool is missing, use the best fallback and label those findings "not measured". Never present a guess as a measurement.

## Step 1: Interview first

Ask before touching code. Use a question tool if available: at most 4 questions per round, at most 2 rounds. Offer options with a recommended default. Skip what the user already said.

Round 1:
1. New site or existing? Built with what, hosted where?
2. Where is the business legally based{based_detail}? Where are its customers?
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
2. Trackers: list them, ask which the user really uses, remove only what they agree to. {tracker_fix} Chat widget: notice before the first message that chats are recorded and processed by a named third party.
3. Legal pages from the legal pages section, with placeholders for unknowns, linked from every footer, each with "Last updated".
4. Accessibility: fix every finding in both themes. Focus rings, skip link, one `h1`, `lang`, labels, `alt`, iframe titles, reduced motion.
5. Claims: rewrite or remove anything without proof; show a before and after table.

## Step 5: Verify

axe-core and Lighthouse on every page in both themes; all links 200 and an unknown URL 404; headers present (inject them in the browser if the local emulator ignores them); CSP shows zero violations with a passing control test; the build contains no placeholders, banned phrases or personal IDs outside the identity page.

## Step 6: Deploy only with an explicit yes

Show what will deploy and where, note the current live version for rollback, deploy after an explicit yes, verify the live site, and enforce CSP only if live shows zero violations. Roll back on any breakage.

## Step 7: Finish

What changed; placeholders left; things to do outside code (lawyer review, registration, data processing agreements, SMS carrier registration, DNS records, budget alerts, two-factor login); and: **This is not legal advice. Laws change. Have a lawyer review your legal pages and client contracts.**
"""


def build(key):
    if key == "us":
        fill = dict(
            key="us",
            region_long="the United States",
            region_short="US",
            other="the EU",
            based_detail=" (state)",
            tracker_rule="Do not add session replay, ad pixels or chat recording without a real need and a clear notice (see the CIPA notes).",
            tracker_fix="Keep a measured list of every third party.",
        )
        region = read("us.md")
    else:
        fill = dict(
            key="eu",
            region_long="the European Union",
            region_short="EU",
            other="the US",
            based_detail=" (country)",
            tracker_rule="Never add a tracker, pixel or analytics script without a consent gate that blocks it until Accept, with an equally easy Reject.",
            tracker_fix="Anything non-essential that stays is blocked until the visitor clicks Accept, with an equally visible Reject.",
        )
        region = read("eu.md")

    parts = [WORKFLOW.format(**fill)]
    parts.append("\n## " + ("US rules" if key == "us" else "EU rules") + "\n\n" + demote(region).split("\n", 1)[1])
    parts.append("\n## Claims section\n\n" + demote(read("claims-and-commitments.md")).split("\n", 1)[1])
    legal = sections(read("legal-pages.md"), ["Which pages", "Privacy policy", "Cookie policy", "Terms", "Accessibility statement"] + (["Legal notice"] if key == "eu" else []))
    parts.append("\n## Legal pages section\n\n" + demote(legal).split("\n", 1)[1])
    if key == "eu":
        parts.append("\n## Owner privacy section\n\n" + demote(read("privacy-of-the-owner.md")).split("\n", 1)[1])
    sec = sections(read("security.md"), ["1.", "3.", "4.", "5."])
    parts.append("\n## Security section\n\n" + demote(sec).split("\n", 1)[1])
    dns = sections(read("dns-safety.md"), ["Records you must never touch"])
    parts.append("\n## DNS safety section\n\n" + demote(dns).split("\n", 1)[1])
    host = sections(read("hosting-and-ddos.md"), ["The risk", "Budget alerts"])
    parts.append("\n## Hosting section\n\n" + demote(host).split("\n", 1)[1])
    parts.append("\n## Gotchas section\n\n" + demote(gotchas(read("gotchas.md"), 8)).split("\n", 1)[1])

    text = fix_links("".join(parts), key)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    out = ROOT / f"website-shield-{key}.md"
    out.write_text(text, encoding="utf-8")
    lines = text.count("\n")
    print(f"{out.name}: {lines} lines" + ("  OVER LIMIT" if lines > LIMIT else ""))
    return lines


if __name__ == "__main__":
    assert all(build(k) <= LIMIT for k in ("us", "eu"))
