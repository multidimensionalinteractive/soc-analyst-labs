# REMnux Safe Workflow

## Setup

Use REMnux or another malware-analysis VM in an isolated lab. Keep host-only or isolated networking unless a specific dynamic analysis step is authorized.

## Static First

1. Hash the file.
2. Identify file type.
3. Extract strings.
4. Inspect document metadata.
5. Extract embedded URLs and objects.
6. Decode obfuscated strings with CyberChef or local tools.

## Dynamic Only If Needed

1. Snapshot the VM.
2. Confirm network isolation.
3. Start packet capture and process monitoring.
4. Open the sample only in the sandbox.
5. Record observed behavior.
6. Stop capture.
7. Revert snapshot.

## Reporting

Document what was observed, what was not observed, and what assumptions remain. A sandbox that shows no behavior does not prove a file is safe.
