# Threat Hunt Plan

## Dataset

Use a public, documented dataset such as Splunk Security Datasets, OTRF/Mordor Security Datasets, Zeek logs, or malware-traffic-analysis exercises.

## Hunt 1: Suspicious PowerShell Download Behavior

- Hypothesis: An attacker used PowerShell to download or execute remote content.
- Data sources: Sysmon Event ID 1, Windows PowerShell logs, proxy logs, DNS logs.
- Key fields: host, user, image, command line, parent image, destination, timestamp.
- Escalation criteria: encoded command, download cradle, suspicious parent, untrusted destination, or execution from user-writable path.

## Hunt 2: Discovery Before Lateral Movement

- Hypothesis: An attacker ran discovery commands before attempting lateral movement.
- Data sources: process creation, command line, authentication logs.
- Key fields: command line, user, host, logon type, source IP.
- Escalation criteria: `net view`, `whoami /groups`, `nltest`, `dsquery`, `ipconfig /all`, or remote admin tooling from a workstation.

## Hunt 3: Beacon-Like Network Activity

- Hypothesis: A compromised endpoint is making periodic outbound connections.
- Data sources: Zeek `conn.log`, proxy logs, DNS logs, EDR network events.
- Key fields: source IP, destination IP, port, bytes, interval, user agent, DNS query.
- Escalation criteria: repeated interval, rare destination, low bytes, unusual process, or suspicious domain.

## Report Format

Each hunt report should include the hypothesis, data source, query, result count, evidence, false-positive notes, conclusion, and next step.
