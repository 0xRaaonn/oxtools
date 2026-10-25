# OpenSSL

**Use:** inspect certificates and keys, calculate digests, encode/decode Base64, and perform standard cryptographic operations. Exact command behavior varies by major version.

**Commands:** `openssl version`; `openssl dgst -sha256 file.bin`; `openssl base64 -d -in encoded.txt -out decoded.bin`; `openssl x509 -in cert.pem -text -noout`; `openssl pkey -in key.pem -text -noout`; `openssl asn1parse -in object.der -inform DER`. For TLS diagnosis: `openssl s_client -connect host:443 -servername host`.

**CTF workflow:** Identify PEM versus DER, inspect certificate fields/modulus/public exponent, calculate hashes to compare files, and decode provided Base64. To decrypt a known ciphertext, determine the exact cipher, mode, IV/nonce, padding, and key derivation; guesses can appear to work by accident.

**Pitfalls:** `openssl enc` has version-dependent password derivation and does not support every modern authenticated mode. Do not paste private keys into online tools. An MD5/SHA hash is not reversible encryption.

Source: [OpenSSL command manuals](https://docs.openssl.org/master/man1/).
