# RsaCtfTool

**Use:** test deliberately weak RSA public keys in CTF crypto challenges and recover plaintext or a private key where a mathematical weakness exists.

**Commands:** `RsaCtfTool --help`; a common form is `RsaCtfTool --publickey pub.pem --private` to try recovering a private key, and `RsaCtfTool --publickey pub.pem --uncipherfile ciphertext.bin` to attempt decryption. Some installations expose `RsaCtfTool.py` or require `python -m`; use local help to confirm.

**RSA basics:** Public key is modulus `n` and exponent `e`. Private exponent `d` is derived from factors of `n`. Textbook RSA computes `c = m^e mod n`; real schemes add padding, so raw integer attacks may not apply. Weaknesses include small factors, shared factors across keys, low exponent misuse, or leaked parameters.

**CTF workflow:** Inspect key with OpenSSL, record `n`/`e` and ciphertext encoding, run relevant attacks, then verify decoded plaintext bytes and padding. Large strong keys are not realistically factorable.

**Pitfalls:** A failed attack says little beyond those strategies failing. Be careful about ciphertext as hex, Base64, big-endian integer, or padded binary.

Source: [RsaCtfTool project](https://github.com/RsaCtfTool/RsaCtfTool).

## Worked example: weak RSA modulus

Given `pub.pem` and `cipher.bin`, inspect `pub.pem` with `openssl pkey -pubin -in pub.pem -text -noout`. Run `RsaCtfTool --publickey pub.pem --private`. If it recovers a private key, run the installed tool's documented decipher command against `cipher.bin` and inspect raw bytes before text decoding. A successful factorization is meaningful only if the recovered key's public modulus matches the original.
