# SOC Analyst Labs

Hands-on blue team projects for building evidence of SOC analyst skills: log monitoring, incident response, packet analysis, cloud security monitoring, endpoint telemetry, threat hunting, automation, honeypots, IOC enrichment, and phishing analysis.

This repository is built as a portfolio workspace. Each project folder includes a lab objective, tool stack, runbook, detection ideas, evidence checklist, and writeup prompt so the finished work can be used in resumes, interviews, and LinkedIn posts.

## Source Inspiration

This lab list is based on Artem Polynko's LinkedIn post, "SOC Analyst Hands-on Projects," checked on 2026-05-26:

https://www.linkedin.com/posts/artem-polynko_soc-analyst-hands-on-projects-ugcPost-7454327097235472384-Bxuf/

## Portfolio Projects

| # | Project | Primary Skills | Status |
|---|---------|----------------|--------|
| 01 | [SIEM log monitoring with Splunk or ELK](projects/01-siem-log-monitoring/) | Ingestion, parsing, dashboards, alert triage | Built |
| 02 | [Simulated phishing attack and incident response](projects/02-phishing-incident-response/) | Phishing triage, containment, reporting | Built |
| 03 | [IDS deployment and packet analysis with Snort or Suricata](projects/03-ids-packet-analysis/) | IDS rules, PCAP review, network detections | Built |
| 04 | [Cloud log monitoring with AWS CloudTrail or Microsoft Defender for Cloud](projects/04-cloud-log-monitoring/) | Cloud audit logs, identity events, alerting | Built |
| 05 | [Endpoint monitoring with Sysmon and Wazuh](projects/05-endpoint-sysmon-wazuh/) | Endpoint telemetry, Windows events, EDR-style triage | Built |
| 06 | [Threat hunting in real datasets](projects/06-threat-hunting-datasets/) | Hypothesis-driven hunting, Windows and Zeek logs | Built |
| 07 | [SOC automation with Python or PowerShell](projects/07-soc-automation-script/) | Alert enrichment, repeatable workflows, analyst tooling | Built |
| 08 | [Honeypot deployment and attacker data capture](projects/08-honeypot-attacker-data/) | Deception, telemetry capture, exposure analysis | Built |
| 09 | [IOC research and enrichment from malware or APT campaigns](projects/09-ioc-research-enrichment/) | OSINT, enrichment, confidence scoring, CTI notes | Built |
| 10 | [Phishing email and attachment analysis in a sandbox](projects/10-phishing-email-sandbox/) | Header analysis, attachment triage, sandbox evidence | Built |

Status note: `Built` means the GitHub lab package is ready with runbooks, detections, sample data, templates, and sample reports. `Evidence complete` should be used only after the live lab has been run and sanitized screenshots or outputs have been added.

## Repository Structure

```text
soc-analyst-labs/
  docs/
    build-status.md
    portfolio-roadmap.md
    safety.md
    source-notes.md
  projects/
    01-siem-log-monitoring/
    02-phishing-incident-response/
    03-ids-packet-analysis/
    04-cloud-log-monitoring/
    05-endpoint-sysmon-wazuh/
    06-threat-hunting-datasets/
    07-soc-automation-script/
    08-honeypot-attacker-data/
    09-ioc-research-enrichment/
    10-phishing-email-sandbox/
  templates/
    detection-notes.md
    incident-report.md
    lab-writeup.md
```

## How To Use This Repo

1. Pick one project and run the lab in a controlled environment.
2. Save screenshots in that project's `evidence/` folder.
3. Add sanitized queries, rules, diagrams, and incident notes.
4. Complete the project README's evidence checklist.
5. Write a short public-facing summary using `templates/lab-writeup.md`.
6. Update the status table above from `Built` to `Evidence complete` after the hands-on evidence is added.

## Evidence Standard

Every completed lab should show:

- What was monitored or analyzed.
- Which data sources were used.
- Which detections, queries, or rules were written.
- What alert or finding was investigated.
- What conclusion was reached.
- What screenshots or sanitized logs prove the work.
- What would be improved in a production SOC.

## Safety Boundary

These projects are for authorized defensive learning only. Do not send phishing emails to real users, run malware on a host connected to personal or business networks, expose honeypots with reused credentials, scan third-party systems, or publish sensitive logs, IP addresses, tokens, customer data, or private email content.

See [docs/safety.md](docs/safety.md) before starting labs involving phishing, malware, honeypots, cloud accounts, or live network capture.
