# MediaInfo

## What it does

Report audio/video container, codec, bitrate, frame rate, and tags.

## First steps

Use `mediainfo media.mp4` or `mediainfo --Output=JSON media.mp4`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A clip reports two audio streams; extract the unexpected stream with FFmpeg and listen separately.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Metadata can be wrong or spoofed; file container parsing is not proof of visible content.
