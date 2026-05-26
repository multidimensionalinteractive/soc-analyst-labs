# Project 09: IOC Research And Enrichment From Malware Or APT Campaigns

## Objective

Research indicators from a public malware or APT report, enrich them safely, score confidence, and produce a concise threat intelligence note for SOC use.

## Tools

- Public vendor or government threat reports.
- VirusTotal, MISP, CyberChef, WHOIS, DNS, passive DNS, or safe local enrichment tools.
- Spreadsheet or Markdown table for IOC tracking.

## Scenario

A new public report lists domains, IPs, file hashes, filenames, and behaviors. Your job is to enrich the indicators, identify which are useful for detection, and explain confidence and limitations.

## Lab Steps

1. Choose a public report that includes indicators.
2. Extract IOCs into a table.
3. Defang domains and URLs.
4. Enrich indicators using safe sources.
5. Score each indicator for confidence, freshness, and actionability.
6. Write detection recommendations.
7. Document caveats such as shared infrastructure, sinkholes, stale hashes, or false positives.

## IOC Table

| Indicator | Type | Source | Enrichment | Confidence | Recommended Use |
|-----------|------|--------|------------|------------|-----------------|
| | | | | | |

## Detection Ideas

```text
High confidence:
File hash from trusted report, observed in malware sample, recent.
```

```text
Medium confidence:
Domain linked to campaign but possibly shared or parked.
```

```text
Low confidence:
IP address from old report or shared hosting.
```

## Evidence Checklist

- Public report link.
- IOC extraction table.
- Enrichment screenshots or notes.
- Confidence scoring explanation.
- Detection recommendations.
- CTI summary.

## Safety Notes

Respect API terms and rate limits. Do not submit private files or confidential indicators to public services unless authorized.

## Resume Bullet

Researched and enriched campaign indicators from public threat intelligence, scored IOC confidence and actionability, and produced SOC-ready detection recommendations.
