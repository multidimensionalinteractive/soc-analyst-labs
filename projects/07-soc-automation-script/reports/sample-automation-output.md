# Sample SOC Automation Output

Run:

```powershell
$env:PYTHONPATH="projects/07-soc-automation-script/automation"
python projects/07-soc-automation-script/automation/triage_enricher.py --alerts projects/07-soc-automation-script/automation/sample_alerts.csv --context projects/07-soc-automation-script/automation/local_context.json --output projects/07-soc-automation-script/automation/triage_summary.csv
```

Expected output:

```text
Wrote 3 triage summaries to projects/07-soc-automation-script/automation/triage_summary.csv
```

The generated CSV includes normalized indicators, local enrichment reasons, a priority score, and a recommended next step.
