# Project 03: IDS Deployment And Packet Analysis With Snort Or Suricata

## Objective

Deploy an IDS sensor, review alerts, inspect packet captures, and write simple detection logic for suspicious network behavior.

## Tools

- Snort or Suricata.
- Wireshark or tshark.
- Safe PCAP samples from training datasets.
- Optional: Zeek for network metadata logs.

## Scenario

The SOC receives an IDS alert for suspicious outbound traffic. You need to validate the alert, inspect the packet evidence, and explain whether the traffic is malicious, suspicious, or benign.

## Lab Steps

1. Install Snort or Suricata in a lab VM.
2. Run the IDS against a safe PCAP sample.
3. Review generated alerts.
4. Open the PCAP in Wireshark and inspect the relevant stream.
5. Document source, destination, protocol, ports, timestamps, and payload clues.
6. Write one simple custom rule for a benign lab pattern.
7. Capture screenshots of alert output and packet analysis.

## Detection Ideas

```text
HTTP user agent anomaly:
Look for rare or scripted user agents in outbound HTTP traffic.
```

```text
DNS review:
Look for repeated queries to unusual domains or high-entropy subdomains.
```

```text
Outbound service mismatch:
Look for traffic using an unexpected port or protocol for the destination.
```

## Evidence Checklist

- IDS installation notes.
- Alert screenshot.
- PCAP screenshot with relevant packets.
- Custom rule and explanation.
- Incident report summary.

## Resume Bullet

Deployed Snort or Suricata in a lab environment, analyzed IDS alerts against PCAP evidence, and wrote custom detection logic for suspicious network traffic.
