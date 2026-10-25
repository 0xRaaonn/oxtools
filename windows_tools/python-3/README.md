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
