# Google Chrome

**Use:** interact with web challenges and inspect browser-side behavior.

**DevTools:** Open with `F12` or `Ctrl+Shift+I`. Elements shows the live DOM, which can differ from raw source (`Ctrl+U`). Network shows requests, responses, headers, bodies, redirects, and timing; enable Preserve log before navigating. Application shows cookies, local/session storage, service workers, and cache. Sources has JavaScript and breakpoints. Console shows errors and lets you inspect values.

**CTF examples:** Inspect a login request and response in Network. Search loaded JavaScript for routes, encoded constants, and client-side validation. Compare cookie flags (HttpOnly, Secure, SameSite) before and after login. Disable cache and hard reload if behavior seems stale.

**Pitfalls:** Editing the DOM only changes your browser view. Client code and console output can be attacker controlled. Extensions and service workers can affect requests; use a clean profile when behavior conflicts with the network trace.

Source: [Chrome DevTools docs](https://developer.chrome.com/docs/devtools/).

## Worked example: inspect a form request

Open a challenge page, press F12, select **Network**, enable **Preserve log**, and submit a harmless sample value `test123`. Select the new request and inspect method, URL, request body, response status, and Set-Cookie. If the page says “incorrect” but the response JSON includes another field, that field is a lead. Change one input at a time and compare the resulting requests.
