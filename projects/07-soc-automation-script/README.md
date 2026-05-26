# Project 07: SOC Automation With Python Or PowerShell

## Objective

Build a small analyst automation that reduces repetitive triage work without hiding the evidence or making irreversible decisions.

## Tools

- Python or PowerShell.
- CSV or JSON alert input.
- Optional safe enrichment sources such as local allowlists, internal asset inventory exports, or public reputation APIs with test keys.

## Scenario

An analyst receives a CSV of alerts containing IPs, domains, hashes, users, and hostnames. The script should normalize the input, enrich what it can safely enrich, score priority, and produce a clean analyst summary.

## Lab Steps

1. Define a simple alert input format.
2. Write validation rules for missing or malformed fields.
3. Normalize indicators to lowercase where appropriate.
4. Enrich indicators from safe local data first.
5. Add optional external enrichment only through environment variables and documented rate limits.
6. Output a CSV or Markdown triage summary.
7. Add tests for parsing, validation, scoring, and output formatting.

## Automation Ideas

```text
Input:
alert_id, timestamp, source, indicator_type, indicator_value, host, user, severity
```

```text
Output:
alert_id, normalized_indicator, enrichment_summary, priority_score, recommended_next_step
```

## Evidence Checklist

- Script source.
- Test run screenshot.
- Sample input with fake data.
- Sample output.
- Explanation of scoring logic.
- Notes on rate limits and API key handling.

## Safety Notes

Never hardcode API keys. Do not upload private indicators or customer data to third-party services without authorization.

## Resume Bullet

Created a Python or PowerShell SOC automation that validates alert data, normalizes indicators, performs safe enrichment, scores priority, and exports analyst-ready triage summaries.
