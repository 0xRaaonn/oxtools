# Zui (formerly Brim)

## What it does

GUI exploration of structured logs and packet-derived data using Zed queries.

## First steps

Open a PCAP or Zed data pool, then filter events by service, IP, or field.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Import a challenge PCAP, find DNS events for a rare domain, then inspect the exact packets in Wireshark/TShark.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Schema and query syntax differ from SQL; imported data may be summarized rather than full raw packets.
