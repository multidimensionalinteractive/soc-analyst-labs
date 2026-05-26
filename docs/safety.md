# Safety Notes

These labs are defensive, educational, and authorization-bound. Keep the work inside systems you own or have explicit permission to test.

## Do Not Commit

- API keys, tokens, passwords, SSH keys, cloud credentials, browser cookies, or session files.
- Raw email bodies from private mailboxes.
- Customer, employee, or client data.
- Malware samples or suspicious attachments.
- Public IPs tied to your home, clients, or employers unless intentionally disclosed.
- Full packet captures containing private traffic.

## Safe Lab Defaults

- Use disposable virtual machines.
- Use private virtual networks where possible.
- Snapshot machines before risky tests.
- Prefer public training datasets over live malware.
- Sanitize screenshots before publishing.
- Keep cloud experiments in a dedicated account or subscription.
- Set budgets and alerts before running cloud resources.
- Tear down cloud and honeypot resources after the lab.

## Phishing Labs

Use synthetic messages and owned test inboxes. Do not send realistic phishing to real users unless you have a formal, written authorization process.

## Malware And Attachment Labs

Do not execute live malware on personal or business machines. Use trusted training environments, disconnected VMs, and static analysis first. If a sample is suspicious, treat it as hostile.

## Honeypot Labs

A honeypot intentionally invites hostile traffic. Use a disposable system, unique credentials, restrictive firewall rules, logging, and a teardown checklist. Do not place a honeypot on a trusted internal network.
