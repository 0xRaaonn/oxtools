# ewf-tools (libewf)

## What it does

Read EWF/E01 forensic disk images and expose raw content.

## First steps

Use `ewfinfo evidence.E01`, `ewfverify evidence.E01`, and `ewfexport evidence.E01` or `ewfmount` with local help.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Verify a provided E01 image, export a raw copy, and pass it to The Sleuth Kit/Autopsy.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

E01 segments must be complete; exported data can be very large.
