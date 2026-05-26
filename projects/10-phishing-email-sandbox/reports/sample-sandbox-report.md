# Sample Phishing Sandbox Report

## Sample

- Message type: Synthetic phishing email.
- Attachment: `invoice_update.html`.
- Link: `hxxps://secure-login-example[.]bad/session`.
- Analysis environment: Isolated VM.

## Static Findings

- The visible link text did not match the actual href.
- The attachment contained an embedded URL.
- The lure requested urgent invoice review.
- No real credentials were entered or collected.

## Behavioral Findings

Dynamic behavior was not executed in this sample report. If dynamic analysis is performed, record DNS queries, HTTP requests, process creation, file writes, registry changes, and network destinations.

## Analyst Decision

Classification: Malicious phishing lure in lab scenario.

## Recommended Response

1. Quarantine matching emails.
2. Block the defanged domain after validation.
3. Search proxy and DNS logs for clicks.
4. Reset credentials if any user submitted credentials.
5. Add a detection for similar sender, subject, attachment, and URL patterns.

## Caveats

Static analysis can miss behavior that triggers only after user interaction, time delay, geolocation checks, or sandbox evasion.
