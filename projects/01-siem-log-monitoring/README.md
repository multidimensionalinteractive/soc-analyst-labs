# Project 01: SIEM Log Monitoring With Splunk Or ELK

## Objective

Build a small SIEM lab that ingests security logs, normalizes useful fields, creates searches, and documents alert triage decisions.

## Tools

- Splunk Enterprise or Elastic Security.
- Public security datasets such as Splunk Security Datasets or generated lab logs.
- Optional: Windows Event Logs, Sysmon, Zeek, or Suricata logs.

## Scenario

You are a Tier 1 SOC analyst reviewing authentication, endpoint, and network events. Your job is to build searches that surface suspicious activity and show how you would triage the alerts.

## Lab Steps

1. Choose Splunk or Elastic Security.
2. Ingest at least two log sources.
3. Confirm important fields are searchable: timestamp, host, user, source IP, destination IP, process, command line, event ID, and alert category.
4. Build saved searches for suspicious authentication, suspicious PowerShell, and unusual outbound network activity.
5. Create a small dashboard showing alert counts, affected hosts, and top users.
6. Investigate one alert and write a short incident report.

## Detection Ideas

```text
Suspicious PowerShell:
process_name="powershell.exe" AND command_line contains one of:
- encodedcommand
- downloadstring
- iex
- bypass
```

```text
Authentication review:
Group failed logons by user, source IP, and destination host.
Escalate repeated failures followed by a success.
```

```text
Network review:
Group outbound connections by host and destination.
Escalate rare destinations, unusual ports, or repeated beacon-like intervals.
```

## Evidence Checklist

- Screenshot of ingested data.
- Screenshot of three working searches.
- Screenshot of dashboard or visualization.
- Sanitized incident report.
- Notes on false positives and tuning.

## Resume Bullet

Built a SIEM monitoring lab using Splunk or Elastic, ingested multiple security log sources, created detection searches for suspicious authentication and endpoint activity, and documented analyst triage results.
