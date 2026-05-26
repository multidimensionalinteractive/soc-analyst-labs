# Sample Honeypot Report

## Scope

- Honeypot: Cowrie SSH/Telnet.
- Deployment: Disposable lab VM.
- Exposure window: 24 hours.
- Public listener: TCP 2222 in lab scenario.

## Findings

- Brute force login attempts began shortly after exposure.
- Common usernames included `root`, `admin`, and `test`.
- Command attempts should be reviewed for downloader behavior, persistence, and reconnaissance.

## Analyst Notes

Honeypot data shows unsolicited internet activity but does not prove targeted intrusion. Avoid over-attribution based on source IP alone because traffic may come from compromised infrastructure, VPNs, or scanners.

## Defensive Recommendations

1. Disable password SSH authentication on real systems.
2. Restrict administrative ports by source IP or VPN.
3. Alert on repeated failed authentication.
4. Monitor for commands that download and execute remote scripts.
5. Keep management services off the public internet where possible.

## Evidence Pending

Add sanitized tables for top usernames, passwords, source IPs, and commands after running the lab.
