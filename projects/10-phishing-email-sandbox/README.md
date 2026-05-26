# Project 10: Phishing Email And Attachment Analysis In A Sandbox

## Objective

Analyze phishing emails and suspicious attachments in a controlled environment, extract indicators, and document safe handling decisions.

## Status

Built as a GitHub-ready lab package. Live sandbox screenshots and static analysis outputs are evidence pending.

## Built Artifacts

- `analysis/static-analysis-checklist.md`: email, link, attachment, and sandbox checklist.
- `sandbox/remnux-safe-workflow.md`: safe REMnux-oriented workflow.
- `iocs/sample-email-iocs.csv`: synthetic defanged IOC table.
- `reports/sample-sandbox-report.md`: sample phishing sandbox report.
- `evidence/README.md`: malware and private-message safety guidance.

## Tools

- Isolated analysis VM.
- REMnux or other malware analysis toolkit for static analysis.
- CyberChef for decoding and defanging.
- Email header analyzer.
- Optional sandbox service approved for the data you are handling.

## Scenario

A suspicious email includes a link or attachment. You need to inspect it safely, determine likely intent, extract useful IOCs, and recommend containment or user guidance.

## Lab Steps

1. Use a synthetic or trusted training sample.
2. Work in an isolated VM with snapshots.
3. Preserve original metadata without opening attachments on a trusted machine.
4. Perform static analysis first: file type, hashes, strings, metadata, macros, URLs, and embedded objects.
5. Decode suspicious strings or links with CyberChef.
6. If dynamic analysis is needed, use a controlled sandbox and document network behavior.
7. Write an incident report with IOCs and containment recommendations.

## Analysis Ideas

```text
Email:
Review headers, sender alignment, reply-to mismatch, authentication results, links, and attachment names.
```

```text
Attachment:
Review file type, hash, embedded URLs, macros, suspicious strings, and observed process or network behavior.
```

```text
URL:
Defang, expand only with safe tooling, capture redirect chain if authorized, and document final landing behavior.
```

## Evidence Checklist

- Sanitized email screenshot.
- Header analysis notes.
- Attachment metadata.
- Hashes and defanged IOCs.
- Sandbox observations.
- Incident report.

## Safety Notes

Do not execute live malware on personal or business systems. Do not upload private files to public sandboxes without authorization. Preserve evidence, but do not commit malicious attachments to this repository.

## Resume Bullet

Analyzed phishing emails and suspicious attachments in an isolated sandbox, extracted defanged IOCs, reviewed static and behavioral evidence, and wrote containment recommendations.
