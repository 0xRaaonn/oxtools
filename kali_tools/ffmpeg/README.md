# FFmpeg

## What it does

Inspect, convert, extract, and filter audio/video streams.

## First steps

Use `ffmpeg -i media.mp4` for stream info and `ffmpeg -i media.mp4 frame_%04d.png` for frames.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract all frames from a supplied video and inspect a one-frame QR code with ZBar; use `ffmpeg -i media.mp4 -vn audio.wav` for audio.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Transcoding is lossy unless configured; keep original and extract without conversion when possible.
