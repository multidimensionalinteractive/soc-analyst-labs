# Sample Endpoint Monitoring Report

## Alert

- Detection: Suspicious PowerShell command line.
- Tooling: Sysmon forwarded to Wazuh.
- Host: `WIN-LAB-01`.
- User: `lab.user`.

## Evidence

Sysmon Event ID 1 showed PowerShell with encoded execution flags. The process was launched from an interactive user session and was followed by a Sysmon Event ID 3 network connection.

## Analyst Assessment

Classification: Suspicious.

Encoded PowerShell can be legitimate, but the combination of encoded execution and outbound network activity should be investigated.

## Recommended Response

1. Pull process tree around the Sysmon ProcessGuid.
2. Decode the command safely in a lab.
3. Review destination IP, DNS, and proxy telemetry.
4. Check for persistence events after execution.
5. Preserve timeline for incident report.

## Tuning Notes

Known administrative scripts should be allowlisted by script path, signer, management host, and owner, not by broadly suppressing PowerShell.
