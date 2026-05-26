# Static Analysis Checklist

## Email Metadata

- Sender display name:
- Envelope sender:
- Reply-to:
- SPF, DKIM, DMARC:
- Subject:
- Message ID:
- Delivery timestamp:

## Link Analysis

- Defang URLs before sharing.
- Identify visible URL versus actual href.
- Expand shortened links only with safe tooling.
- Record redirect chain only in an isolated environment.

## Attachment Analysis

- File name:
- File type from magic bytes:
- File size:
- Hashes:
- Embedded URLs:
- Macros:
- Suspicious strings:
- Creation and modification metadata:

## Sandbox Review

- Snapshot before execution.
- Disable shared clipboard and shared folders.
- Capture DNS, HTTP, process, file, registry, and network behavior.
- Revert snapshot after analysis.

## Decision

- Benign:
- Suspicious:
- Malicious:
- Inconclusive:
