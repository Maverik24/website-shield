# Gotchas from a real compliance project

**As of 2026-10-27.** Tool behaviour changes between versions; retest on your own setup.

These are problems that came up while taking a real small business site through this process (static site, Python build script, Firebase Hosting, third-party booking embed, built on Windows). Each one wasted time or nearly caused a false result. Check for them early.

## 1. Windows line endings make CSP hashes look wrong

**Symptom:** you hash each inline script in the built HTML and compare with the CSP header. They do not match, yet the browser reports no violations and the scripts run.
**Cause:** files written on Windows contain CRLF line endings. Browsers normalise CRLF to LF before hashing ([WHATWG Infra, normalize newlines](https://infra.spec.whatwg.org/#normalize-newlines)), so the browser's hash matches your header but a raw-bytes hash of the file does not.
**Fix:** compute hashes from the in-memory text with LF line endings (in the build step, before writing files), and normalise CRLF to LF in any checking script.

## 2. The local emulator may ignore custom headers

**Symptom:** security headers and CSP are in the host config, but local tests show none of them.
**Cause:** in the project this came from, the hosting emulator served files without applying any custom headers from the config, not even cache headers.
**Fix:** to test CSP locally, intercept each page request in a headless browser and serve it with the exact headers from the config. Then check the real headers again on the live site after deploy.

## 3. "Zero violations" can mean a broken test

**Symptom:** the CSP test reports zero violations everywhere.
**Risk:** the listener may not be attached, or the header may not be applied.
**Fix:** run a **control test**: on one page, inject an inline script and an image from an outside domain. The test must report both. Only then trust the zero.

## 4. Headless Chrome may report "reduce motion"

**Symptom:** animations, or code that only runs when motion is allowed, appear broken in automated tests.
**Cause:** the test machine had system animations turned off, so the browser reported `prefers-reduced-motion: reduce` and the site correctly skipped the animation.
**Fix:** emulate the media feature explicitly in tests, once with `reduce` and once with `no-preference`, and check both.

## 5. Old preview deploys keep serving old claims

**Symptom:** you fix a claim on the live site, but a preview or staging URL still shows the old wording, and anyone with the link can see it.
**Fix:** list preview channels after a copy change and delete the ones you no longer need. Confirm the old URL returns 404.

## 6. Preview deploys can trigger "live site" hooks

**Symptom:** a post-deploy script (for example one that notifies search engines) runs on preview deploys too, pinging search engines for pages that still show old content.
**Fix:** make the hook check that the live pages match the build before it runs, and skip otherwise.

## 7. Build steps that append config blocks duplicate them

**Symptom:** each build adds another copy of the same header block to the host config.
**Fix:** when a build step writes into a config file, have it remove its own previous blocks first, then write fresh ones. Run the build twice and confirm the config is unchanged.

## 8. Third-party embeds bring their own third parties

**Symptom:** the site "has no trackers", but one page sets a cookie and contacts Google.
**Cause:** a booking calendar embed loaded its own scripts, a bot-protection cookie (Cloudflare `__cf_bm`), Google Fonts and files from Google Cloud Storage.
**Fix:** measure network requests and cookies per page with the embed fully loaded (pick a date, open a step). Disclose what the embed loads in the privacy and cookie policies, or load it only after a click if the owner prefers. It also lowers some Lighthouse best-practices scores (third-party cookies), which you cannot fix from your own code; explain this rather than chase it.

## 9. Forcing a Node process to exit can crash it on Windows

**Symptom:** a post-deploy script that calls `process.exit()` right after network requests crashes on Windows with a non-zero exit code, which can fail the deploy.
**Fix:** set `process.exitCode = 0` and let Node exit on its own.

## 10. backdrop-filter traps fixed-position menus

**Symptom:** the mobile menu panel opens with zero height or is clipped.
**Cause:** a `backdrop-filter` on the sticky header creates a containing block for fixed-position children.
**Fix:** remove the filter while the menu is open, or move the panel outside the header.

## 11. Headless Chrome cannot render narrower than about 500px

**Symptom:** full-page screenshots at "375px" show content cut off on the right.
**Fix:** render the page inside a 375px-wide iframe, or use device emulation in Puppeteer or Playwright, instead of a 375px window.

## 12. Repository names may already be taken

**Symptom:** creating the backup repository fails because a repository with that name already exists (an old project).
**Fix:** stop and ask. Offer a new name or a new branch. Never force-push over existing work.
