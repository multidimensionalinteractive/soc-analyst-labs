# Sample IDS Packet Analysis Report

## Alert

- Rule: LAB Suspicious scripted user agent.
- Sensor: Suricata lab VM.
- Severity: Medium.
- Source: `192.0.2.25`.
- Destination: `198.51.100.50`.

## Evidence

The IDS alert identified outbound HTTP traffic with a scripted user agent. Packet review showed the user agent string `python-requests` and repeated requests to the same path.

## Assessment

Classification: Suspicious.

This behavior can be benign automation, but it deserves review when observed from a workstation or when paired with unusual destinations, authentication failures, or new process creation.

## Next Steps

1. Identify the host and owning user.
2. Check endpoint process telemetry for the process that opened the connection.
3. Search DNS and proxy logs for the same destination.
4. Tune the rule for known automation hosts.
