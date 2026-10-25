# jq

**Use:** query and transform JSON on the command line. It reads JSON and outputs JSON by default.

**Commands:** `jq '.' data.json` pretty prints; `jq -r '.user.name' data.json` returns raw text; `jq '.items[] | select(.active == true) | .id' data.json` filters; `jq 'keys' data.json` lists object keys; `jq -s 'length' lines.jsonl` counts JSON lines after slurping; `jq -c '.[]' array.json` emits compact JSON lines.

**Syntax:** `.foo` selects key foo; `.[0]` selects first array element; `[]` iterates an array/object; `?` suppresses errors for missing values; `//` supplies a default; `map(...)` transforms arrays. Quote the filter for your shell. In PowerShell, single quotes around a jq program are usually easiest.

**CTF workflow:** Inspect API responses, Zeek JSON logs, challenge metadata, and tool output. Use `-r` when piping values to another command; otherwise strings remain quoted JSON.

**Pitfalls:** `jq` expects valid JSON, not arbitrary JavaScript object notation. `-s` loads all input into memory. Missing keys yield `null` unless you handle them.

Source: [jq manual](https://jqlang.org/manual/).

## Worked example: filter API data

Given `users.json` containing `{"users":[{"name":"Ada","active":true},{"name":"Bob","active":false}]}`, run `jq -r '.users[] | select(.active) | .name' users.json`. Output is `Ada` without JSON quotes. The `[]` iterates users, `select` keeps active entries, and `-r` emits plain text. If the file contains one JSON object per line, use a filter for each line or `-s` to collect them first.

## More CTF scenario questions

### An API response has many records; how do I print only active IDs?

For a JSON object with `items` array, run `jq -r '.items[] | select(.active == true) | .id' response.json`. Check a sample record first; a missing or string-valued `active` field changes the filter.

### The file has one JSON object per line and `jq '.items[]'` fails. Why?

JSON Lines has multiple top-level objects, not one array. Run a filter that operates on each line, such as `jq -r '.id' data.jsonl`, or use `jq -s` only if you intentionally want one large array.
