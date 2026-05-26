# Project 08: Honeypot Deployment And Attacker Data Capture

## Objective

Deploy a controlled honeypot, capture attacker interaction data, analyze common patterns, and document defensive lessons without endangering trusted systems.

## Tools

- Cowrie SSH/Telnet honeypot or another reviewed honeypot.
- Disposable cloud VM or isolated lab host.
- Firewall rules and cloud budget alerts.
- Log analysis tool such as jq, Python, Splunk, or Elastic.

## Scenario

You deploy a deception host to observe unsolicited internet activity. Your job is to capture telemetry, summarize attacker behavior, and recommend defensive controls.

## Lab Steps

1. Create a disposable VM in a dedicated lab account.
2. Lock down management access.
3. Install and configure the honeypot.
4. Forward or preserve logs.
5. Run the honeypot for a bounded period.
6. Analyze top usernames, passwords, source countries or ASNs, commands, and attempted downloads.
7. Tear down the VM and confirm no resources remain.
8. Write a report with graphs or tables.

## Analysis Ideas

```text
Top attempted usernames and passwords.
```

```text
Time from exposure to first connection.
```

```text
Most common commands attempted after login.
```

```text
Source IP clustering by ASN or country, with caution about attribution limits.
```

## Evidence Checklist

- Architecture sketch.
- Honeypot configuration notes.
- Sanitized log excerpts.
- Summary tables.
- Teardown screenshot.
- Lessons learned.

## Safety Notes

Do not reuse credentials. Do not expose internal networks. Do not run downloaded attacker files. Do not publish raw logs that include sensitive infrastructure details.

## Resume Bullet

Deployed an isolated honeypot, captured unsolicited attacker telemetry, analyzed login and command patterns, and translated findings into defensive monitoring recommendations.
