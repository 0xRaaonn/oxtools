# can-utils

**Use:** inspect and generate Controller Area Network (CAN) frames through Linux SocketCAN. In CTFs, you may receive `candump` logs rather than a physical interface.

**Core commands (WSL/Linux with SocketCAN support):** `candump can0` reads frames; `cansend can0 123#DEADBEEF` sends standard-ID frame 0x123 with four data bytes; `cansend can0 123##1DEADBEEF` is a CAN FD example; `candump -L can0` logs with timestamps; `candump -l can0` writes a log file; `canplayer -I candump.log` replays a log; `cansniffer can0` highlights changed bytes. Run each command's `-h` for the installed syntax.

**Frame basics:** An 11-bit standard identifier or 29-bit extended identifier labels a message; up to 8 bytes in classic CAN, up to 64 in CAN FD. Identifier, DLC, and data are separate. The same ID usually represents one message type, not one endpoint address.

**CTF workflow:** Group frames by ID, compare periodicity and changing byte positions, test byte order and scaling, and reconstruct multi-frame payloads if the application protocol uses them.

**Pitfalls:** Sending frames can affect a real bus. Use only supplied lab interfaces. WSL may lack direct SocketCAN access; analyze logs offline if so.

Source: [can-utils README](https://github.com/linux-can/can-utils).

## Worked example: decode a changing CAN field

Given a candump log, look for frames such as `can0 123 [4] 10 27 00 00` and later `can0 123 [4] 20 27 00 00`. The first byte changed while the second stayed `27`. Test little-endian 16-bit values: `0x2710` then `0x2720`. If the challenge describes a sensor, compare periodic samples and scaling. Use `candump can0` only when the event provides an interface; do not transmit to a real bus.
