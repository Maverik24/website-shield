# Security baseline for a small business website

**As of 2026-10-27.** These are practical defaults, not a full security review. Header behaviour can change between browser versions; recheck the linked documentation.

## 1. Secrets scan (do this first)

Search every file in the project, including build output and scripts, for:
- `apiKey`, `api_key`, `api-key`, `secret`, `password`, `token`, `access_token`, `Bearer `
- provider key prefixes such as `sk_live`, `sk_test`, `sk-`, `pit-`, `AIza` (Google), `ghp_` / `gho_` (GitHub)
- webhook URLs and private API hosts of CRMs and payment tools
- `.env` files and anything that looks like a private key block

Rules:
- A secret in front-end code is public, even if the file is minified. **If you find one, tell the user immediately so they can revoke it at the provider**, then move the call to a server function or remove it.
- Public identifiers are not secrets: a booking widget ID, a publishable analytics ID, an IndexNow key file. Say so, so the user does not panic.
- Keep `.env*` and local caches out of version control (see section 5).

## 2. Database, storage and backend rules

- List every backend service in use (for example Firestore, Realtime Database, Storage, Supabase tables, serverless functions).
- Open rules (for example "allow read, write: if true") mean anyone on the internet can read or change the data. Lock them down to the minimum the site needs, and test with the provider's emulator or rules simulator.
- If an API is disabled or a service was never created, record that too. "Not in use" is a valid audit result.
- If you cannot check something from the command line, give the user the exact console steps instead of guessing.

## 3. Security headers

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

## 4. Content-Security-Policy: report-only first, then enforce

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
7. **Hashes and line endings:** browsers normalise CRLF line endings to LF before hashing inline scripts ([WHATWG Infra, normalize newlines](https://infra.spec.whatwg.org/#normalize-newlines)). Compute hashes on LF-normalised text, or files built on Windows will appear to "fail" in your own checks while working in the browser. See `gotchas.md`.

## 5. Version control and backups

- Use git. Commit once per phase with a clear message.
- Add a `.gitignore` before the first commit, covering at least: `.env`, `.env.*`, provider caches (for example `.firebase/`), `node_modules/`, and any private files that must never be published (for example a paid ebook or client data).
- Before pushing, run `git status` and `git ls-files` and confirm none of those are tracked.
- Back up to a **private** repository. Confirm visibility after creating it (for example `gh repo view <name> --json visibility` must say `PRIVATE`). If the repo will contain a legal page with personal ID numbers, it must never be public.
- If the repository name is already taken, stop and ask the user. Never force-push over an existing repository.
- GitHub turns on secret scanning and push protection by default for new public repositories owned by personal accounts ([GitHub changelog, 11 March 2024](https://github.blog/changelog/2024-03-11-secret-scanning-and-push-protection-are-enabled-by-default-on-new-public-repositories/)). Private repos may not have this, so your own secrets scan still matters.

## 6. Accounts: two-factor login everywhere

- Turn on two-factor authentication for: the domain registrar and DNS host, the hosting provider, the code host (GitHub), email, the CRM or booking tool, and any payment provider.
- GitHub has required 2FA for code contributors on GitHub.com since 2023 ([GitHub Docs, mandatory 2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication)).
- Prefer an authenticator app or security key over SMS codes.

## 7. Search engine notifications (optional)

If you use IndexNow to tell Bing and others about updated pages, run it after deploys of the **live** site only. A preview deploy that pings search engines sends them to pages that still show the old content. See `gotchas.md`.
