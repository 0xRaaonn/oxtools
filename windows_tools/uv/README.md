# uv

**Use:** manage Python versions, virtual environments, dependencies, and one-off tools. It is a package manager, not an analyzer.

**Commands:** `uv --version`, `uv python list`, `uv venv .venv`, `uv pip install -r requirements.txt`, `uv run python script.py`, `uvx <tool> --help`. `uv init` creates project metadata; `uv add <package>` records a dependency. Use `uv pip list` or `uv tree` to record versions.

**CTF workflow:** Inspect a supplied script and its dependency list first. Create a case-local environment and install only required packages if rules permit. Offline installation works only from a cache or local wheel files.

**Pitfalls:** Packages and their install scripts can execute code. The contest may permit uv while restricting packages; check its rules. `uv pip install` targets an environment, so activate one or use `--python`.

Source: [uv official docs](https://docs.astral.sh/uv/).

## Worked example: isolate a supplied script

In the challenge folder, run `uv venv .venv`, then `uv pip install --python .venv -r requirements.txt` if the event permits those packages. Run `uv run python analyze.py` from the project, or directly `.venv\Scripts\python.exe analyze.py` on Windows. Record `uv pip list --python .venv` so your result can be reproduced. An installation failure while offline means the package is not cached or available locally.

## More CTF scenario questions

### A supplied Python script requires a package, but the event is offline. Can uv help?

Check `uv pip list` in your case environment and the local uv cache. If the package is not installed or cached, uv cannot invent it offline; use a permitted local wheel or a standard-library approach.

### The script behaves differently under two Python versions. How do I pin one?

Create `uv venv --python 3.11 .venv` if 3.11 is available, run the script with that interpreter, and record `python --version`. Bytecode and dependency compatibility may explain differences.
