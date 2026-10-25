# TShark

**Use:** Wireshark's CLI packet analyzer. It reads PCAP/PCAPNG and uses the same display-filter engine.

**Commands:** `tshark -r capture.pcapng` lists packets; `tshark -r capture.pcapng -Y 'dns'` filters displayed packets; `tshark -r capture.pcapng -Y 'http.request' -T fields -e frame.number -e http.host -e http.request.uri` prints selected fields; `tshark -r capture.pcapng -q -z io,phs` shows protocol hierarchy; `tshark -r capture.pcapng -q -z conv,tcp` lists TCP conversations; `tshark -G fields` lists field names.

**Filters:** `-Y` is a display filter when reading a file; `-f` is a capture filter when capturing live traffic. `-T fields` plus repeated `-e` fields is ideal for scripts. `-E separator=,` can change output delimiters. `-w filtered.pcapng` writes selected packets, subject to the chosen options/version.

**CTF workflow:** First summarize protocols and endpoints; extract DNS names, HTTP paths, or a suspicious stream number; inspect details in Wireshark. Use `-z follow,tcp,ascii,STREAM` where supported to follow a TCP stream.

**Pitfalls:** Field names and follow syntax vary by version; use local `-G fields` and `-z help`. Packet fields can repeat, producing multi-value output. Preserve original capture.

Source: [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html).

## Worked example: extract DNS names

Run `tshark -r capture.pcapng -Y 'dns.flags.response == 0' -T fields -e frame.number -e dns.qry.name`. Suppose frame `84` asks for `ZmxhZw.example.test`. Decode the leading label separately and then inspect frame 84 in Wireshark to verify the packet and source host. If a query name appears twice, check retransmissions rather than counting it as two distinct messages.

## More CTF scenario questions

### How do I list all DNS query names without opening Wireshark?

Run `tshark -r file.pcapng -Y 'dns.flags.response == 0' -T fields -e frame.number -e dns.qry.name`. Inspect frame numbers for retransmissions and verify suspicious names in packets.

### A field extraction prints several values in one row. Is the output corrupt?

A packet can contain repeated occurrences of a field. Set an aggregator/separator with `-E` or use full packet output; check `tshark -G fields` for exact field names.
