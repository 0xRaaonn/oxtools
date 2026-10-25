# aircrack-ng

## What it does

Analyze captured Wi-Fi handshakes and test candidate passphrases in authorized labs.

## First steps

Start with `aircrack-ng --help`; typical offline form is `aircrack-ng -w words.txt capture.cap`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Given a competition-provided WPA handshake capture and small supplied wordlist, run the offline check and verify a reported key by reusing it in the lab setup.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A PCAP without a complete relevant handshake cannot validate a password; do not capture or attack unrelated networks.
