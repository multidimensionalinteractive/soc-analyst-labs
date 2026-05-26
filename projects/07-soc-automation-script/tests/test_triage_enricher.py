import csv
import json
import tempfile
import unittest
from pathlib import Path

import triage_enricher


class TriageEnricherTest(unittest.TestCase):
    def test_normalizes_and_scores_alerts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            alerts_path = temp_path / "alerts.csv"
            context_path = temp_path / "context.json"
            output_path = temp_path / "summary.csv"

            with alerts_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "alert_id",
                        "timestamp",
                        "source",
                        "indicator_type",
                        "indicator_value",
                        "host",
                        "user",
                        "severity",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "alert_id": "A-100",
                        "timestamp": "2026-05-25T18:00:00Z",
                        "source": "siem",
                        "indicator_type": "domain",
                        "indicator_value": " Evil.Example.COM ",
                        "host": "WIN-7",
                        "user": "analyst",
                        "severity": "high",
                    }
                )

            context_path.write_text(
                json.dumps(
                    {
                        "known_bad": {"domain": ["evil.example.com"]},
                        "crown_jewel_hosts": ["WIN-7"],
                        "privileged_users": ["analyst"],
                    }
                ),
                encoding="utf-8",
            )

            summaries = triage_enricher.process_alert_file(alerts_path, context_path, output_path)

            self.assertEqual(len(summaries), 1)
            self.assertEqual(summaries[0]["normalized_indicator"], "evil.example.com")
            self.assertEqual(summaries[0]["priority_score"], "100")
            self.assertEqual(summaries[0]["recommended_next_step"], "Escalate immediately")

            with output_path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))

            self.assertEqual(rows[0]["enrichment_summary"], "Known bad indicator; crown jewel host; privileged user")

    def test_rejects_missing_required_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            alerts_path = temp_path / "alerts.csv"
            context_path = temp_path / "context.json"
            output_path = temp_path / "summary.csv"

            alerts_path.write_text("alert_id,indicator_type\nA-200,ip\n", encoding="utf-8")
            context_path.write_text("{}", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "missing required columns"):
                triage_enricher.process_alert_file(alerts_path, context_path, output_path)


if __name__ == "__main__":
    unittest.main()
