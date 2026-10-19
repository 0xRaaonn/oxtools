# Sherlock

Sherlock checks a username against many social networks and reports pages where that username may exist. It is a command-line OSINT tool for username discovery; a matching username is only a lead and does not by itself prove that accounts belong to the same person.

## Links

- Source repository: <https://github.com/sherlock-project/sherlock>
- Official installation guide: <https://sherlockproject.xyz/installation>
- Official usage guide: <https://sherlockproject.xyz/usage>

## Install

The Sherlock project recommends `pipx` for an isolated Python command-line installation:

```bash
pipx install sherlock-project
```

Check that it is available:

```bash
sherlock --version
```

If `pipx` is not installed, follow its official setup instructions for your operating system: <https://pipx.pypa.io/stable/installation/>. The Sherlock installation guide also documents Docker, package-manager, and source-based options.

## Examples

Search for one username:

```bash
sherlock example_username
```

Search for several usernames:

```bash
sherlock username_one username_two
```

Save a single user's results to a file:

```bash
sherlock example_username --output example_username.txt
```

Use these searches only for lawful, authorized research. Check any reported profile manually; sites can return false positives, and username reuse does not establish identity.
