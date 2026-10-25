# OpenSSL

**Use:** inspect certificates and keys, calculate digests, encode/decode Base64, and perform standard cryptographic operations. Exact command behavior varies by major version.

**Commands:** `openssl version`; `openssl dgst -sha256 file.bin`; `openssl base64 -d -in encoded.txt -out decoded.bin`; `openssl x509 -in cert.pem -text -noout`; `openssl pkey -in key.pem -text -noout`; `openssl asn1parse -in object.der -inform DER`. For TLS diagnosis: `openssl s_client -connect host:443 -servername host`.

**CTF workflow:** Identify PEM versus DER, inspect certificate fields/modulus/public exponent, calculate hashes to compare files, and decode provided Base64. To decrypt a known ciphertext, determine the exact cipher, mode, IV/nonce, padding, and key derivation; guesses can appear to work by accident.

**Pitfalls:** `openssl enc` has version-dependent password derivation and does not support every modern authenticated mode. Do not paste private keys into online tools. An MD5/SHA hash is not reversible encryption.

Source: [OpenSSL command manuals](https://docs.openssl.org/master/man1/).

## Worked example: inspect a public key and ciphertext

Run `openssl pkey -pubin -in pub.pem -text -noout` to read RSA modulus and exponent. If the challenge provides `cipher.bin`, first determine whether it is raw bytes or Base64 text; for Base64, use `openssl base64 -d -in cipher.b64 -out cipher.bin`. Feed the key and decoded ciphertext to RsaCtfTool only if a weak-key attack is plausible. Record key size, exponent, and ciphertext byte length before trying attacks.
