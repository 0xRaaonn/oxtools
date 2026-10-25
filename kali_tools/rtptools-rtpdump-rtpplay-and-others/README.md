# rtptools (rtpdump, rtpplay and others)

## What it does

Inspect, replay, or manipulate RTP packet streams for media forensics.

## First steps

Use `rtpdump -h` and select the installed command matching the capture format.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract an RTP stream from a supplied PCAP, reconstruct its payload, and compare audio timing with Wireshark stream analysis.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

RTP codecs and sequence loss affect playback; do not replay onto real networks without authorization.
