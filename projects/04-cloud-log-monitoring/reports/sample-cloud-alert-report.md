# Sample Cloud Alert Report

## Alert

- Detection: Security group opened to the internet.
- Platform: AWS CloudTrail lab account.
- Severity: High.
- Resource: `sg-lab-web`.

## Evidence

CloudTrail recorded `AuthorizeSecurityGroupIngress` with a CIDR range of `0.0.0.0/0`. The actor was a lab IAM user and the change affected an inbound rule.

## Assessment

Classification: Risky configuration change.

Opening administrative or sensitive service ports to the internet can expose workloads to brute force attempts, scanning, and exploit attempts.

## Recommended Response

1. Validate whether the change was approved.
2. Revert the broad ingress rule if unauthorized.
3. Check for connections during the exposure window.
4. Add alerting for future broad exposure changes.
5. Review IAM permissions for the actor.

## Evidence Pending

Add screenshots from CloudTrail, CloudTrail Lake, Security Hub, Defender for Cloud, or Sentinel after running the lab.
