# OpenSSH Session Key Recovery

**Use:** recover OpenSSH session key material from a compatible Linux memory image, then use that material to analyze an associated SSH packet capture. This is a research plugin collection, not an ordinary SSH client.

**Prerequisites:** You need a suitable memory snapshot, an OpenSSH session that was active in it, matching Volatility 3 version, Linux symbols for the kernel, the project's OpenSSH symbols, and often the corresponding PCAP. The project includes several scripts/plugins; read the specific README in your installed copy.

**Volatility 3 setup:** The project's documentation places its plugin path after Volatility's `-p` flag and the OpenSSH symbol directory after `-s`. A general invocation shape is `vol -f memory.raw -p /path/to/plugin -s /path/to/symbols <plugin-name>`. List available plugin names with `vol -h` after supplying paths and use the plugin's `-h` for required options.

**CTF workflow:** Confirm OS/OpenSSH architecture, run process discovery, use the plugin against the active SSH process, then match recovered key and cipher parameters with the PCAP/session. Account for rekeying and packet directions.

**Pitfalls:** A password or server host key is not enough to decrypt a modern SSH capture. Version mismatches and missing symbols are common. Never publish recovered session keys.

Source: [Fox-IT project README](https://github.com/fox-it/OpenSSH-Session-Key-Recovery).
