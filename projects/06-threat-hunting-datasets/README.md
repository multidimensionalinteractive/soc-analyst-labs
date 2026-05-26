# Project 06: Threat Hunting In Real Datasets

## Objective

Use public Windows, Zeek, Sysmon, or cloud datasets to run hypothesis-driven threat hunts and document evidence-backed findings.

## Tools

- Splunk, Elastic, Jupyter notebooks, or local query tools.
- Public datasets such as Splunk Security Datasets, Mordor/OTRF Security Datasets, Zeek logs, or malware-traffic-analysis exercises.

## Scenario

You are hunting for adversary behavior without starting from a single alert. You need to form a hypothesis, query data, inspect evidence, and decide whether activity deserves escalation.

## Lab Steps

1. Select a public dataset with documented attack activity.
2. Write a hunt hypothesis.
3. Identify relevant data sources and fields.
4. Run at least three queries that test the hypothesis.
5. Track false positives and tuning ideas.
6. Map findings to ATT&CK tactics and techniques where appropriate.
7. Write a hunt report with evidence and next steps.

## Example Hunt Hypotheses

```text
An attacker used PowerShell to download or execute remote content.
```

```text
An attacker performed discovery commands before lateral movement.
```

```text
An endpoint made repeated outbound network connections consistent with command and control.
```

## Evidence Checklist

- Dataset source and description.
- Hypothesis.
- Query notes.
- Screenshots of supporting events.
- False-positive notes.
- Hunt conclusion.

## Resume Bullet

Conducted hypothesis-driven threat hunts against public Windows and network telemetry datasets, wrote queries for adversary behavior, and documented evidence, false positives, and escalation criteria.
