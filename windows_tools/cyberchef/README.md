# CyberChef

**Use:** decode, transform, and inspect data by chaining operations in a browser. A shared recipe link can include input data; inspect before sharing.

**Workflow:** Paste text or load a file into Input. Search and drag operations into Recipe; they run top to bottom. Inspect output after every step. Set parameters such as alphabet, byte order, key type, delimiter, and character encoding. Save the recipe to reproduce your work. Magic guesses formats; verify its suggestions.

**Examples:** `SGVsbG8=` → From Base64 → `Hello`. `66 6c 61 67` → From Hex → `flag`. `%7B` → URL Decode → `{`. For binary output, use To Hex or download it; text rendering may hide NUL or invalid Unicode. For XOR, choose whether the key is text or hex.

**Pitfalls:** Encoding is reversible without a secret; encryption needs a key. Operation order matters. Large files may exhaust browser memory.

Source: [CyberChef project](https://github.com/gchq/CyberChef).

## Worked example: decode a layered message

Input: `ZmxhZ3t0ZXN0fQ%3D%3D`. Add **URL Decode**, then **From Base64**. URL Decode converts `%3D%3D` into `==`; From Base64 yields `flag{test}`. If you reverse those two operations, Base64 fails or produces the wrong bytes. Use the output pane to verify each layer before adding the next.
