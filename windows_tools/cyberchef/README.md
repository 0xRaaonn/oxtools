# CyberChef

**Use:** decode, transform, and inspect data by chaining operations in a browser. A shared recipe link can include input data; inspect before sharing.

**Workflow:** Paste text or load a file into Input. Search and drag operations into Recipe; they run top to bottom. Inspect output after every step. Set parameters such as alphabet, byte order, key type, delimiter, and character encoding. Save the recipe to reproduce your work. Magic guesses formats; verify its suggestions.

**Examples:** `SGVsbG8=` → From Base64 → `Hello`. `66 6c 61 67` → From Hex → `flag`. `%7B` → URL Decode → `{`. For binary output, use To Hex or download it; text rendering may hide NUL or invalid Unicode. For XOR, choose whether the key is text or hex.

**Pitfalls:** Encoding is reversible without a secret; encryption needs a key. Operation order matters. Large files may exhaust browser memory.

Source: [CyberChef project](https://github.com/gchq/CyberChef).

## Worked example: decode a layered message

Input: `ZmxhZ3t0ZXN0fQ%3D%3D`. Add **URL Decode**, then **From Base64**. URL Decode converts `%3D%3D` into `==`; From Base64 yields `flag{test}`. If you reverse those two operations, Base64 fails or produces the wrong bytes. Use the output pane to verify each layer before adding the next.

## More CTF scenario questions

### A string looks like Base64 but decoding gives gzip bytes. What next?

In CyberChef, apply **From Base64**, inspect the hex output for gzip magic `1F 8B`, then add **Gunzip**. A readable flag after decompression confirms both layers; if magic differs, identify that format before guessing.

### A repeated ciphertext may use one-byte XOR. How do I test it?

Use **XOR** with a one-byte hex key and test candidate values against a known prefix such as `flag{`. Confirm the entire output is coherent; random keys can produce short readable fragments.
