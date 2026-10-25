# Rust (rustup, rustc, cargo)

## What it does

Compile/run Rust helpers and manage toolchains.

## First steps

Use `rustc --version`, `cargo new demo`, `cargo run`, and `cargo build --release`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Write a byte parser in Rust for a custom record, compile, then compare parsed integers with xxd/Python.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Cargo builds can fetch dependencies and execute build scripts; inspect `Cargo.toml` and source.
