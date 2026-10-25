# Go

## What it does

Build and run Go programs.

## First steps

Use `go version`, `go run main.go`, and `go build -o app .`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Write a tiny parser for a length-prefixed message, run it on provided bytes, and verify field lengths against xxd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Go modules may download dependencies; inspect `go.mod` and source before running.
