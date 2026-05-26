# Project 04: Cloud Log Monitoring With AWS CloudTrail Or Microsoft Defender For Cloud

## Objective

Monitor cloud audit and security events, detect risky identity or resource activity, and document an alert triage workflow.

## Tools

- AWS CloudTrail, CloudWatch, and IAM Access Analyzer, or Microsoft Defender for Cloud and Azure Activity Logs.
- Optional: Security Hub, GuardDuty, Microsoft Sentinel, or KQL queries in a lab tenant.

## Scenario

An analyst receives an alert about unusual cloud activity. Your job is to determine who did what, from where, against which resource, and whether the activity should be escalated.

## Lab Steps

1. Use a dedicated lab cloud account or subscription.
2. Enable audit logging.
3. Generate safe administrative events such as login, failed login, IAM policy change, storage bucket change, or security group change.
4. Query logs for identity, source IP, action, resource, and result.
5. Create at least three alert ideas for risky cloud activity.
6. Write a short cloud incident report.
7. Tear down resources and confirm billing controls.

## Detection Ideas

```text
Identity risk:
Console login failure spikes, login from unusual country, or root account use.
```

```text
Permission risk:
New administrative policy attached to a user, role, or group.
```

```text
Exposure risk:
Storage bucket public access change or security group opened to the internet.
```

## Evidence Checklist

- Logging configuration screenshot.
- Query results for generated events.
- Alert logic notes.
- Sanitized incident report.
- Teardown confirmation.

## Safety Notes

Use a lab account, set a budget alert, and do not publish account IDs, ARNs, tenant IDs, subscription IDs, tokens, access keys, or raw logs containing private identifiers.

## Resume Bullet

Built a cloud monitoring lab using AWS CloudTrail or Microsoft Defender for Cloud, queried audit events for identity and exposure risks, and documented cloud alert triage.
