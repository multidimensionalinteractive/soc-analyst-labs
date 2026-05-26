# Project 02: Simulated Phishing Attack And Incident Response

## Objective

Practice phishing investigation from initial report through triage, containment, user impact analysis, IOC extraction, and final reporting.

## Status

Built as a GitHub-ready lab package. Live mailbox screenshots and sanitized mail-log evidence are evidence pending.

## Built Artifacts

- `runbooks/phishing-ir-runbook.md`: analyst workflow from intake to reporting.
- `iocs/phishing-ioc-table.csv`: synthetic IOC table with defanged values.
- `reports/sample-incident-report.md`: sample phishing incident report.
- `evidence/README.md`: screenshot and privacy guidance.

## Tools

- Owned test mailbox or synthetic email samples.
- Email header analyzer.
- URL defanging and decoding tools.
- Screenshot and reporting templates.
- Optional: Microsoft 365 Defender, Google Workspace logs, or mail gateway logs if available in a lab tenant.

## Scenario

A user reports a suspicious email. You need to determine whether it is phishing, identify indicators, assess who else received it, and recommend containment.

## Lab Steps

1. Create or collect a safe synthetic phishing email.
2. Preserve headers and message metadata.
3. Extract sender, reply-to, subject, URLs, attachment names, hashes, and delivery timestamps.
4. Defang all URLs before documenting them.
5. Check whether the sender domain, URLs, and attachment hashes appear suspicious using safe reputation sources.
6. Build a timeline from delivery to report to containment.
7. Write an incident report using `templates/incident-report.md`.

## Investigation Questions

- Does the sender align with the display name?
- Do links point to expected domains?
- Is the message trying to create urgency, fear, payment pressure, or credential entry?
- Were attachments present?
- Which users or mailboxes were affected?
- What containment is appropriate?

## Evidence Checklist

- Sanitized screenshot of email body.
- Sanitized header excerpt.
- IOC table with defanged URLs and domains.
- Timeline.
- Containment recommendations.

## Safety Notes

Do not send realistic phishing to real users. Do not collect credentials. Do not click live suspicious links from a trusted machine.

## Resume Bullet

Performed a simulated phishing incident response workflow, extracted and enriched IOCs, assessed mailbox impact, and produced a containment-focused incident report.
