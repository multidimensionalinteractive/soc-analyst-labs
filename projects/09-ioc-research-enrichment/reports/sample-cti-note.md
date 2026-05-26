# Sample CTI Note

## Executive Summary

A synthetic campaign brief described credential phishing infrastructure and a JavaScript attachment lure. The strongest indicators are the file hash and campaign domain. The IP address and filename are useful for context but should not be used alone for blocking without validation.

## Source

- Report title: Synthetic Credential Phishing Campaign Brief.
- Publisher: Lab scenario.
- Publication date: 2026-05-25.
- Confidence in source: Medium for lab exercise.

## Indicators

| Indicator | Type | Confidence | Recommended Use | Notes |
|-----------|------|------------|-----------------|-------|
| malicious-example[.]bad | Domain | Medium | DNS and proxy hunt | Defanged for sharing |
| 198[.]51[.]100[.]77 | IP | Low | Context only | Could be shared infrastructure |
| 44d88612fea8a8f36de82e1278abb02f | MD5 | High | File hash detection | Lab-safe reference |
| invoice_update.js | Filename | Low | Email search | Weak by itself |

## Detection Opportunities

- Search email logs for the attachment name and sender theme.
- Search DNS/proxy logs for the defanged domain.
- Search endpoint telemetry for script execution from downloads or temp directories.
- Add an enrichment note so analysts understand confidence and caveats.

## Caveats

Indicators age quickly. IP-based blocking can create false positives when infrastructure is shared. File names are weak indicators unless paired with sender, hash, or behavior.
