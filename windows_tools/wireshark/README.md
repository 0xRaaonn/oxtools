# Wireshark

**Use:** inspect PCAP/PCAPNG packet captures visually or capture live traffic through an allowed interface.

**Workflow:** Open the capture; check Statistics → Protocol Hierarchy, Conversations, and Endpoints. Select a packet: the top pane lists packets, middle decodes protocols, bottom shows raw bytes. Right click a TCP packet → Follow → TCP Stream. File → Export Objects recovers objects from supported protocols.

**Display filters:** `http`, `dns`, `tcp.stream == 3`, `ip.addr == 10.0.0.5`, `tcp.port == 443`, `frame contains "flag"`, `http.request.method == "POST"`. Combine with `&&`, `||`, `!`. Capture filters use different BPF syntax, such as `host 10.0.0.5 and port 80`, and prevent excluded packets from being recorded.

**CTF path:** Look for HTTP bodies, DNS TXT records, transferred files, unusual ports, and repeated small packets. Compare both directions of a stream.

**Pitfalls:** TCP retransmits and out-of-order packets make single frames misleading. Use reassembly. TLS content needs session secrets or endpoint plaintext; a server private key alone usually cannot decrypt modern TLS. A display filter does not change the capture file.

Sources: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/), [filter syntax](https://www.wireshark.org/docs/man-pages/wireshark-filter.html).

## Worked example: find a flag in HTTP

Open a supplied `capture.pcapng` and enter display filter `http.request`. Select a request to see the host and URI, then right click it → **Follow → TCP Stream**. Suppose the response body contains `flag{http_stream}`: record the stream number and packet numbers, then clear the display filter and confirm the bytes in the corresponding response packets. If the response is compressed, use Wireshark's decoded entity view or export the object.

## More CTF scenario questions

### A PCAP contains many DNS queries with long labels. Could they hide data?

Filter `dns.qry.name` and inspect requests from one source in frame order. Remove the common domain suffix, join the variable labels only if sequence/timing supports it, then try Base64/hex decoding. Check responses and retransmissions before counting duplicates.

### A webpage download is visible but the supplied file is missing. Can I recover it?

Filter HTTP traffic, select the response, then try **File → Export Objects → HTTP**. Save the object to a new folder and confirm its signature and length. If TLS is encrypted without keys, the HTTP body will not be visible.
