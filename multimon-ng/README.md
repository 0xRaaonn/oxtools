# multimon-ng

## What it does

Decode selected radio/audio modulation protocols from audio.

## First steps

Use `multimon-ng -h`; a common offline form is `multimon-ng -a MODE -t wav signal.wav`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For a supplied WAV with AFSK1200 tones, enable that decoder and inspect recovered text or packet lines.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Mode and sample format must match; noisy audio creates false decodes.
