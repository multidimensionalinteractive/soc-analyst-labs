# Portfolio Roadmap

This roadmap turns the 10 SOC Analyst labs into a publishable GitHub portfolio. The goal is not to rush through tools. The goal is to produce evidence that an interviewer can inspect.

## Suggested Build Order

### Phase 1: Core Monitoring

1. SIEM log monitoring.
2. Endpoint monitoring with Sysmon and Wazuh.
3. IDS packet analysis.

Why: These create the basic muscle memory of log ingestion, search, field extraction, detection logic, and triage.

### Phase 2: Investigation Workflows

4. Phishing incident response.
5. Phishing email and attachment sandbox analysis.
6. Threat hunting in public datasets.

Why: These show that you can move from an alert to an evidence-backed conclusion.

### Phase 3: Cloud, Automation, and Threat Intel

7. Cloud log monitoring.
8. SOC automation script.
9. IOC research and enrichment.

Why: These show breadth across modern SOC workflows and reduce repetitive analyst work.

### Phase 4: Deception and Real-World Telemetry

10. Honeypot attacker data capture.

Why: This is valuable but should be done carefully because it can expose a system to the public internet.

## Definition Of Done For Each Lab

- A clear scenario.
- A diagram or short architecture description.
- A list of tools and data sources.
- At least three useful detection or investigation queries.
- A screenshot checklist.
- A sanitized incident report.
- Lessons learned.
- Resume bullets that describe the skill demonstrated.

## Resume Translation

Good lab entries are specific:

- "Built a Splunk lab ingesting Windows, Sysmon, and Suricata logs; wrote SPL searches for suspicious PowerShell, account activity, and network beaconing."
- "Investigated simulated phishing incident from mailbox triage through containment, documented IOCs, affected users, and recommended controls."
- "Deployed Wazuh with Sysmon telemetry and tuned alerts for process creation, persistence, and suspicious network connections."

Avoid vague entries:

- "Used Splunk."
- "Learned phishing."
- "Worked with logs."
