# tcpdump

## What it does

Capture and inspect packets from an interface or PCAP.

## First steps

Use `tcpdump -nn -r capture.pcap` and `tcpdump -i IFACE -w capture.pcap` for authorized capture.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Read a supplied PCAP with `tcpdump -nn -r`, filter `host 10.0.0.5 and port 80`, then pivot to Wireshark for stream reconstruction.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Capture filters use BPF syntax and can omit packets permanently; live capture may need privileges.
