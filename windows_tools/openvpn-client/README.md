# OpenVPN Client

**Use:** join a competition's private lab using its supplied `.ovpn` profile and credentials.

**Windows workflow:** Import the organizer's profile into OpenVPN Connect or the installed client. Connect, then check the assigned tunnel IP and routes with PowerShell `ipconfig` and `route print`. Test a supplied target with `Test-NetConnection <host> -Port <port>`. Disconnect afterward.

**Terminal:** If classic OpenVPN is installed, `openvpn --config challenge.ovpn` starts a session with required privileges. OpenVPN Connect uses a different CLI; do not assume this command exists. WSL traffic may not follow Windows VPN routes depending on WSL networking mode; test from both environments.

**Troubleshooting:** Read the client log for authentication failures, expired certificates, clock errors, DNS failures, and conflicting routes. A connected tunnel does not prove the target service is up.

**Pitfalls:** The profile and private keys are credentials. Keep them out of writeups and public repositories.

Source: [OpenVPN Connect docs](https://openvpn.net/connect-docs/).
