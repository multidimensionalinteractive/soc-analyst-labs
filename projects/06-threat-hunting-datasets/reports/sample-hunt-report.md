# Sample Threat Hunt Report

## Hunt

- Hypothesis: An attacker used PowerShell to download or execute remote content.
- Dataset: Public Windows/Sysmon training dataset.
- Data sources: Sysmon process creation, DNS, network telemetry.

## Query

See `queries/threat-hunts.spl`.

## Findings

The hunt identified PowerShell commands containing web download patterns. One host also showed DNS and network connections shortly after execution.

## False Positive Review

Potential benign explanations:

- Administrative script deployment.
- Software installation workflow.
- Developer automation.

Required validation:

- Script path and signer.
- Change ticket or owner.
- Parent process and user context.

## Conclusion

Classification: Suspicious pending owner validation.

## Recommended Next Steps

1. Decode or reconstruct command safely.
2. Review destination reputation and DNS history.
3. Pull endpoint timeline around process execution.
4. Add detection for repeated download cradle patterns.
