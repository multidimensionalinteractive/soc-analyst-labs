# Project 05: Endpoint Monitoring With Sysmon And Wazuh

## Objective

Collect endpoint telemetry from a Windows lab host, forward it to Wazuh, and build detections for suspicious process and network activity.

## Status

Built as a GitHub-ready lab package. Live Sysmon and Wazuh screenshots are evidence pending.

## Built Artifacts

- `configs/sysmon-lab-config.xml`: minimal lab Sysmon configuration focused on suspicious process, network, file, and registry events.
- `queries/wazuh-discover-queries.md`: Wazuh searches for Sysmon process, network, startup, and registry events.
- `reports/sample-endpoint-report.md`: sample endpoint investigation report.
- `evidence/README.md`: endpoint evidence guidance.

## Tools

- Windows lab VM.
- Microsoft Sysmon.
- Wazuh manager and agent.
- Sysmon configuration such as SwiftOnSecurity or another reviewed baseline.

## Scenario

A Windows endpoint shows suspicious process activity. You need to collect telemetry, search events, and document which events matter for triage.

## Lab Steps

1. Create a Windows lab VM.
2. Install Sysmon with a reviewed configuration.
3. Install the Wazuh agent and confirm events are reaching the Wazuh dashboard.
4. Generate benign test activity such as PowerShell launch, network connection, file creation, and scheduled task creation.
5. Search for Sysmon Event IDs related to process creation, network connections, file creation, and registry persistence.
6. Tune one noisy event and document the trade-off.
7. Write a short endpoint investigation report.

## Detection Ideas

```text
Suspicious PowerShell:
Sysmon process creation where image ends with powershell.exe and command line includes encoded or download behavior.
```

```text
Persistence review:
Scheduled task creation, Run key changes, or service creation.
```

```text
Network review:
Unexpected process initiating outbound connection.
```

## Evidence Checklist

- Sysmon installation screenshot.
- Wazuh agent connection screenshot.
- Event search screenshots.
- Detection notes.
- Tuning notes.
- Incident report.

## Resume Bullet

Configured Sysmon and Wazuh endpoint monitoring, collected Windows telemetry, and wrote detections for suspicious process execution, persistence, and network connections.
