# Sample SIEM Triage Report

## Alert

- Detection: Suspicious PowerShell execution.
- Source: Splunk saved search.
- Severity: Medium.
- Affected host: `WIN-LAB-01`.
- User: `lab.user`.

## Evidence

The alert matched a PowerShell command line containing encoded execution flags and a web download pattern. The parent process was a user-launched shell, and the event was followed by an outbound connection from the same host.

## Analyst Decision

Classification: Suspicious, escalation recommended.

## Next Steps

1. Pull surrounding process creation events for the host.
2. Review network telemetry for destination domain and IP.
3. Check whether the user recently received phishing email.
4. Preserve command line, process GUID, parent process, and destination details.

## Tuning Notes

Do not suppress all encoded PowerShell. Tune by known admin scripts, signed automation paths, and approved management hosts.
