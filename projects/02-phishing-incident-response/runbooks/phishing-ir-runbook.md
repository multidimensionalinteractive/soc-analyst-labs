# Phishing Incident Response Runbook

## Intake

1. Record reporter, timestamp, subject, sender, and mailbox.
2. Preserve message headers and original message if policy allows.
3. Do not click links from a trusted workstation.

## Triage

1. Validate sender display name, envelope sender, reply-to, SPF, DKIM, and DMARC results.
2. Extract URLs, domains, IP addresses, attachment names, and hashes.
3. Defang URLs before sharing.
4. Determine whether the message asks for credentials, payment, execution, or sensitive data.

## Scope

1. Search for matching sender, subject, URLs, attachment hashes, and message IDs.
2. Identify affected users and delivery timestamps.
3. Check whether any users clicked, replied, downloaded, or entered credentials.

## Containment

1. Remove or quarantine matching messages.
2. Block malicious sender, domain, URL, or hash where appropriate.
3. Reset credentials and revoke sessions for affected users if credential entry is suspected.
4. Open endpoint investigation for any attachment execution.

## Reporting

Use `templates/incident-report.md` and include:

- Root cause or lure theme.
- Affected users.
- IOCs.
- Actions taken.
- Recommended control improvements.
