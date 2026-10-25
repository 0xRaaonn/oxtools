# Zeek

**Use:** turn network captures into protocol and behavioral logs. It is useful for broad triage of large PCAPs.

**Commands (WSL/Linux):** Run in an empty output directory: `zeek -r ../capture.pcap`. This creates logs such as `conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log`, depending on traffic. `zeek -r ../capture.pcap LogAscii::use_json=T` emits JSON logs in supported versions. Inspect tab-separated logs with `head` or JSON logs with `jq`.

**Fields:** `conn.log` records source/destination, ports, duration, byte counts, and connection state. `dns.log` includes queries and answers. `http.log` includes methods, hosts, URIs, status codes, and user agents. `files.log` tracks observed file transfers; file extraction needs an explicit policy/script and varies by version.

**CTF workflow:** Find odd hosts, high data volumes, many failed connections, unusual DNS answers, or suspicious HTTP paths; pivot to Wireshark/TShark for packet-level detail.

**Pitfalls:** Zeek logs summarize observations and may omit incomplete or unsupported traffic. No log entry does not prove no packet existed. Analyze a copy and keep output per case.

Source: [Zeek documentation](https://docs.zeek.org/en/current/).

## Worked example: find a suspicious DNS query

In an empty output directory run `zeek -r ../capture.pcapng`. Open `dns.log` and find an unusual query such as `ZmxhZw.example.test`. The leading label resembles Base64; decode it in CyberChef or Python and then verify the corresponding DNS packet in Wireshark. Zeek gives the lead; the PCAP proves what was actually transmitted.

## More CTF scenario questions

### Zeek creates `conn.log` but no `http.log`. Is there no web traffic?

Check ports and protocol detection in the PCAP. The traffic may be HTTPS, incomplete, non-HTTP, or encoded on an unusual port. Use Wireshark to inspect a representative stream.

### `files.log` reports a transferred file. How do I get it?

Find the file UID and corresponding connection, then use Wireshark's Export Objects or configure Zeek's file extraction policy. `files.log` is metadata; it is not the file bytes.
