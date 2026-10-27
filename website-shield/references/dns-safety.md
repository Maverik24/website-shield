# DNS safety

**As of 2026-10-27.** DNS mistakes can take a site offline or stop email for days. This skill never changes DNS itself. It tells the user exactly what to add, and the user makes the change.

## Before anything: take a snapshot

1. Ask the user to screenshot or export every record in their DNS panel **before** any change. Save it with the date.
2. Read current public DNS yourself (read-only), for example with a DNS-over-HTTPS lookup (`https://dns.google/resolve?name=<host>&type=<TYPE>`) for the apex, `www`, `MX`, `TXT` and `_dmarc`. Note the nameservers too.
3. Compare: if what you read does not match what the user sees in their panel, stop and ask. They may be editing the wrong provider.

## Records you must never touch

Tell the user in plain words: **only add the records listed. Do not edit or delete anything else.** In particular:

| Record | Why it matters |
|---|---|
| `MX` | Email delivery. Delete or change these and email stops. |
| `TXT` with `v=spf1 ...` | Tells receivers which servers may send your email. Breaking it sends your mail to spam. |
| `TXT` or `CNAME` for DKIM (often `google._domainkey`, `selector1._domainkey` and similar) | Signs your email. |
| `TXT` at `_dmarc` | Email authentication policy. |
| `TXT` verification records (for example `google-site-verification=...`, `hosting-site=...`, other `*-verification`) | Prove ownership to Google, the host and other tools. Removing them can break the site or a service. |
| Apex `A` / `AAAA` records that currently serve the live site | Change these and the site goes offline. |

## Adding a www redirect (example: Firebase Hosting)

1. Add `www.example.com` as a custom domain on the **same hosting site** that serves the apex domain, configured to redirect to the apex. Firebase supports redirecting a custom domain to another domain. Source: [Firebase, Connect a custom domain](https://firebase.google.com/docs/hosting/custom-domain).
2. The host then lists the records it needs. For a subdomain this is typically:
   - a `CNAME` for `www` pointing to the site's default host name, and
   - optionally a `TXT` at `_acme-challenge.www` for faster certificate issuance.
3. Give the user these records in a copy-ready table (type, host, value, TTL default) and remind them of the never-touch list above.
4. If `www` already has a record (some registrars add a default `www` CNAME), the user must **replace** that one record, not add a second. Check before you tell them.

## Waiting for the certificate

- DNS changes and HTTPS certificates are not instant. Firebase says certificate provisioning can take up to 24 hours. Source: [Firebase, Connect a custom domain](https://firebase.google.com/docs/hosting/custom-domain).
- Until the certificate is issued, `https://www.` fails with a certificate name error, while `http://www.` may already redirect. That is normal.
- Give the user a small check script that confirms: the DNS record resolves to the right target, the host shows the domain as active with a certificate, and `https://www.` answers `301` to the apex. Have them run it later instead of checking by hand.

## Checklist

- [ ] Snapshot of all records taken before any change.
- [ ] Only the new records added; nothing edited or deleted.
- [ ] MX, SPF, DKIM, DMARC and verification TXT records unchanged afterwards.
- [ ] Check script passes after the certificate is issued.
