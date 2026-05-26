# Sample Phishing Incident Report

## Summary

- Incident title: Credential phishing email reported by user.
- Severity: Medium.
- Status: Contained in lab scenario.

## Initial Alert

A user reported an email claiming an invoice required immediate review. The visible sender impersonated a finance contact, while the reply-to and link domain did not align with the expected organization.

## Timeline

| Time | Event | Evidence |
|------|-------|----------|
| 18:00 UTC | Email delivered | Message metadata |
| 18:07 UTC | User reported suspicious email | Helpdesk ticket |
| 18:12 UTC | Analyst extracted IOCs | IOC table |
| 18:20 UTC | Matching messages searched | Mail log query |
| 18:30 UTC | Containment recommended | Incident notes |

## Findings

- The message used urgency and invoice language to request link interaction.
- The link pointed to `hxxps://login-example[.]bad`.
- No real credentials were collected in this lab scenario.

## Containment

- Quarantine matching messages.
- Block the defanged domain after validation.
- Search proxy and DNS logs for user interaction.
- Provide user awareness feedback.

## Lessons Learned

Header alignment, URL defanging, and mailbox scoping should happen before reputation checks so the investigation has a clean evidence base.
