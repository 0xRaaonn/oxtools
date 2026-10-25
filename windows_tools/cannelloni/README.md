# cannelloni

**Use:** tunnel Linux SocketCAN frames over a network between hosts. It is not the same as decoding CAN data; pair it with can-utils.

**Concept:** One process reads a local SocketCAN interface and forwards frames over UDP or SCTP; the peer injects them into its local SocketCAN interface. The program needs matching transport/ports and a working local CAN or virtual CAN interface on each side.

**Start:** Run `cannelloni -h` and inspect the README for your exact build before selecting client/server syntax; flags differ among packaged releases. A typical lab uses a local `vcan0` virtual interface and a peer address/port, then verifies traffic with `candump vcan0`. Record whether traffic is classic CAN or CAN FD and whether timestamps are preserved.

**CTF workflow:** If organizers provide a tunnel endpoint, connect only to that endpoint, observe frames with candump, and send frames only when the challenge calls for it.

**Pitfalls:** Network connectivity alone does not prove frames are reaching SocketCAN. WSL may not have the required kernel CAN features. Do not point it at a production vehicle or bus.

Source: [cannelloni project](https://github.com/mguentner/cannelloni).

## Worked example: validate a provided CAN tunnel

After starting the two cannelloni endpoints with the organizer's connection parameters, run `candump vcan0` on the receiving side. If the sender emits a known test frame `123#DEADBEEF`, the receiver should show ID `123` and four bytes `DE AD BE EF`. If no frame arrives, check interface names, transport/port, firewall, and whether the peer tunnel process is running. Use the installed `cannelloni -h` for exact startup flags.

## More CTF scenario questions

### Both tunnel processes run, but `candump vcan0` shows nothing. What next?

Check each endpoint's local interface name, UDP/SCTP transport and ports, peer address, and whether any sender actually emits frames. A running tunnel does not create traffic.

### Frames appear twice after reconnecting. Is the data duplicated?

Inspect both local CAN interfaces and tunnel topology for a loop or replay, and compare timestamps/IDs. Deduplicate only after proving repeated frames are transport artifacts.
