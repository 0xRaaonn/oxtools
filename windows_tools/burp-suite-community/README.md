# Burp Suite Community Edition

**Use:** inspect and edit HTTP(S) traffic to a web challenge through an intercepting proxy.

**Setup:** Start Burp; use its built-in browser or configure Chrome's proxy to Burp's listener (often `127.0.0.1:8080`). The built-in browser handles the proxy certificate setup. With an external browser, install Burp's CA certificate only into that test browser/profile to inspect HTTPS. Use Proxy → HTTP history and Intercept; send a request to Repeater to edit and resend it.

**CTF workflow:** Capture a request, change one parameter or header, send with Repeater, compare status, headers, body, and timing. Use Decoder for simple encodings and Comparer for response differences. Scope the target to organizer-provided hosts.

**Community limits:** Some automated features are restricted or slower than Professional; use the manual tools and check your installed edition.

**Pitfalls:** Burp's proxy will not see traffic from programs not configured to use it. A browser may cache responses. Some apps use certificate pinning or non-HTTP protocols. Disable interception when you just want to browse normally.

Source: [PortSwigger Burp documentation](https://portswigger.net/burp/documentation).
