# OpenVPN Client

**Use:** join a competition's private lab using its supplied `.ovpn` profile and credentials.

**Windows workflow:** Import the organizer's profile into OpenVPN Connect or the installed client. Connect, then check the assigned tunnel IP and routes with PowerShell `ipconfig` and `route print`. Test a supplied target with `Test-NetConnection <host> -Port <port>`. Disconnect afterward.

**Terminal:** If classic OpenVPN is installed, `openvpn --config challenge.ovpn` starts a session with required privileges. OpenVPN Connect uses a different CLI; do not assume this command exists. WSL traffic may not follow Windows VPN routes depending on WSL networking mode; test from both environments.

**Troubleshooting:** Read the client log for authentication failures, expired certificates, clock errors, DNS failures, and conflicting routes. A connected tunnel does not prove the target service is up.

**Pitfalls:** The profile and private keys are credentials. Keep them out of writeups and public repositories.

Source: [OpenVPN Connect docs](https://openvpn.net/connect-docs/).

## Worked example: verify a lab tunnel

Import `team.ovpn` provided by the organizer and connect. In PowerShell run `ipconfig` and find the VPN adapter address, then `Test-NetConnection 10.10.10.5 -Port 80` using the organizer's sample target. A successful TCP test confirms a route to that service; a failed test calls for checking the VPN log, route table, target IP, and target service status. Do not treat a green Connected label alone as proof of target reachability.
