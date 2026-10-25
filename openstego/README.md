# OpenStego

## What it does

Hide/extract data in images and support watermarking modes.

## First steps

Use GUI or `java -jar openstego.jar help`; CLI commands are documented by the installed JAR.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open a provided stego image, choose Extract Data, supply a known password if given, and inspect extracted bytes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

OpenStego formats need matching mode/password; arbitrary LSB images may not be OpenStego payloads.
