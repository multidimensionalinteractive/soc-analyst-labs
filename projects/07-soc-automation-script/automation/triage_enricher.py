import argparse
import csv
import json
from pathlib import Path


REQUIRED_COLUMNS = {
    "alert_id",
    "timestamp",
    "source",
    "indicator_type",
    "indicator_value",
    "host",
    "user",
    "severity",
}

OUTPUT_COLUMNS = [
    "alert_id",
    "timestamp",
    "source",
    "indicator_type",
    "normalized_indicator",
    "host",
    "user",
    "severity",
    "enrichment_summary",
    "priority_score",
    "recommended_next_step",
]

SEVERITY_SCORES = {
    "informational": 10,
    "low": 20,
    "medium": 40,
    "high": 60,
    "critical": 80,
}


def normalize_indicator(indicator_type, indicator_value):
    value = indicator_value.strip()
    if indicator_type.lower() in {"domain", "url", "email", "hash_md5", "hash_sha1", "hash_sha256"}:
        return value.lower()
    return value


def load_context(context_path):
    if not Path(context_path).exists():
        return {"known_bad": {}, "crown_jewel_hosts": [], "privileged_users": []}

    with Path(context_path).open(encoding="utf-8") as handle:
        context = json.load(handle)

    return {
        "known_bad": context.get("known_bad", {}),
        "crown_jewel_hosts": [host.lower() for host in context.get("crown_jewel_hosts", [])],
        "privileged_users": [user.lower() for user in context.get("privileged_users", [])],
    }


def validate_columns(fieldnames):
    missing = sorted(REQUIRED_COLUMNS - set(fieldnames or []))
    if missing:
        raise ValueError(f"Input CSV missing required columns: {', '.join(missing)}")


def enrich_alert(alert, context):
    indicator_type = alert["indicator_type"].strip().lower()
    normalized_indicator = normalize_indicator(indicator_type, alert["indicator_value"])
    host = alert["host"].strip()
    user = alert["user"].strip()
    severity = alert["severity"].strip().lower()

    score = SEVERITY_SCORES.get(severity, 20)
    reasons = []

    known_bad_values = {
        value.lower()
        for value in context["known_bad"].get(indicator_type, [])
    }
    if normalized_indicator.lower() in known_bad_values:
        score += 25
        reasons.append("Known bad indicator")

    if host.lower() in context["crown_jewel_hosts"]:
        score += 10
        reasons.append("crown jewel host")

    if user.lower() in context["privileged_users"]:
        score += 10
        reasons.append("privileged user")

    score = min(score, 100)

    if score >= 90:
        next_step = "Escalate immediately"
    elif score >= 70:
        next_step = "Triage as high priority"
    elif score >= 50:
        next_step = "Review in analyst queue"
    else:
        next_step = "Monitor or enrich further"

    return {
        "alert_id": alert["alert_id"].strip(),
        "timestamp": alert["timestamp"].strip(),
        "source": alert["source"].strip(),
        "indicator_type": indicator_type,
        "normalized_indicator": normalized_indicator,
        "host": host,
        "user": user,
        "severity": severity,
        "enrichment_summary": "; ".join(reasons) if reasons else "No local enrichment hits",
        "priority_score": str(score),
        "recommended_next_step": next_step,
    }


def process_alert_file(alerts_path, context_path, output_path):
    context = load_context(context_path)
    summaries = []

    with Path(alerts_path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        validate_columns(reader.fieldnames)
        for row in reader:
            summaries.append(enrich_alert(row, context))

    with Path(output_path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(summaries)

    return summaries


def build_parser():
    parser = argparse.ArgumentParser(description="Normalize and enrich SOC alert CSV data.")
    parser.add_argument("--alerts", required=True, help="Input alert CSV path.")
    parser.add_argument("--context", required=True, help="Local context JSON path.")
    parser.add_argument("--output", required=True, help="Output triage summary CSV path.")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    summaries = process_alert_file(args.alerts, args.context, args.output)
    print(f"Wrote {len(summaries)} triage summaries to {args.output}")


if __name__ == "__main__":
    main()
