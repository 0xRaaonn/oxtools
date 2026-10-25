# uv

**Use:** manage Python versions, virtual environments, dependencies, and one-off tools. It is a package manager, not an analyzer.

**Commands:** `uv --version`, `uv python list`, `uv venv .venv`, `uv pip install -r requirements.txt`, `uv run python script.py`, `uvx <tool> --help`. `uv init` creates project metadata; `uv add <package>` records a dependency. Use `uv pip list` or `uv tree` to record versions.

**CTF workflow:** Inspect a supplied script and its dependency list first. Create a case-local environment and install only required packages if rules permit. Offline installation works only from a cache or local wheel files.

**Pitfalls:** Packages and their install scripts can execute code. The contest may permit uv while restricting packages; check its rules. `uv pip install` targets an environment, so activate one or use `--python`.

Source: [uv official docs](https://docs.astral.sh/uv/).
