# SoX (Sound eXchange)

## What it does

Inspect, convert, trim, reverse, and analyze audio from the CLI.

## First steps

Use `soxi audio.wav`, `sox audio.wav trimmed.wav trim 5 10`, and `sox audio.wav -n spectrogram -o spec.png`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Create a spectrogram from a supplied WAV, see DTMF-like tones, then decode with a suitable allowed tool or manual frequency check.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Resampling and compression can remove clues; use copies and record parameters.
