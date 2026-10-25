# Google Chrome

**Use:** interact with web challenges and inspect browser-side behavior.

**DevTools:** Open with `F12` or `Ctrl+Shift+I`. Elements shows the live DOM, which can differ from raw source (`Ctrl+U`). Network shows requests, responses, headers, bodies, redirects, and timing; enable Preserve log before navigating. Application shows cookies, local/session storage, service workers, and cache. Sources has JavaScript and breakpoints. Console shows errors and lets you inspect values.

**CTF examples:** Inspect a login request and response in Network. Search loaded JavaScript for routes, encoded constants, and client-side validation. Compare cookie flags (HttpOnly, Secure, SameSite) before and after login. Disable cache and hard reload if behavior seems stale.

**Pitfalls:** Editing the DOM only changes your browser view. Client code and console output can be attacker controlled. Extensions and service workers can affect requests; use a clean profile when behavior conflicts with the network trace.

Source: [Chrome DevTools docs](https://developer.chrome.com/docs/devtools/).

## Worked example: inspect a form request

Open a challenge page, press F12, select **Network**, enable **Preserve log**, and submit a harmless sample value `test123`. Select the new request and inspect method, URL, request body, response status, and Set-Cookie. If the page says “incorrect” but the response JSON includes another field, that field is a lead. Change one input at a time and compare the resulting requests.

## More CTF scenario questions

### A button is disabled in the page, but the challenge asks what request it sends. How can I inspect it?

Use DevTools **Elements** and **Sources** to find its event handler or loaded JavaScript, then inspect Network while triggering authorized page actions. Client-side disablement is UI state; the server response determines whether an action is accepted.

### A value changes after refresh. Where might it be stored?

Inspect **Application** for cookies, localStorage, sessionStorage, and service workers. Compare values before/after refresh, then check Network response headers for Set-Cookie. A DOM value alone does not tell you who stored it.
