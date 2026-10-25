# Python 3

**Use:** automate parsing, decoding, and small search spaces. The standard library covers many CTF tasks.

**Start:** PowerShell: `py -3 --version` and `py -3 script.py`; WSL: `python3 --version` and `python3 script.py`. Interactive shell: `python3` then `exit()`. Create a virtual environment with `python3 -m venv .venv` and activate it with `source .venv/bin/activate` in WSL or `.\.venv\Scripts\Activate.ps1` in PowerShell.

**Bytes example:**

```python
from pathlib import Path
import base64, struct
raw = Path('sample.bin').read_bytes()
print(raw[:32].hex())
print(base64.b64decode('SGVsbG8='))
print(struct.unpack('<I', raw[:4])[0])  # little-endian uint32
Path('copy.bin').write_bytes(raw)
```

Useful modules: `re`, `json`, `csv`, `hashlib`, `itertools`, `collections`, `zipfile`, `gzip`, `lzma`, `socket`. `bytes.fromhex('66 6c 61 67')` yields `b'flag'`; `int.from_bytes(data, 'little')` converts bytes to an integer.

**Pitfalls:** `str` is Unicode text; `bytes` is raw data. Decode only with a known encoding. `eval` and `pickle.load` can execute untrusted content.

Source: [Python standard library](https://docs.python.org/3/library/).

## Worked example: decode repeating XOR

Suppose `cipher.bin` was XORed with one unknown byte. This script prints candidates beginning with the known PNG signature:

```python
from pathlib import Path
data = Path('cipher.bin').read_bytes()
for key in range(256):
    plain = bytes(b ^ key for b in data)
    if plain.startswith(bytes.fromhex('89504e470d0a1a0a')):
        print(f'key=0x{key:02x}')
        Path('candidate.png').write_bytes(plain)
```

Open `candidate.png` and validate it with a PNG parser; a header match alone is not enough.

## More CTF scenario questions

### Four bytes are `78 56 34 12`. What integer do they represent?

Use `int.from_bytes(bytes.fromhex('78 56 34 12'), 'little')` to get `0x12345678`. Try big-endian only if the format specifies it, and compare against expected ranges or headers.

### A script reads a file as UTF-8 and crashes on byte `FF`. What changed?

The file is binary or another encoding. Read with `Path('file.bin').read_bytes()`, inspect hex, then decode only the text field with a known encoding. Using replacement characters can hide evidence.
