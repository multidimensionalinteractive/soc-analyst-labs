# Honeypot Log Analysis Queries

These examples assume Cowrie JSON logs. Adapt file paths to your deployment.

## Top Usernames

```bash
jq -r 'select(.eventid=="cowrie.login.failed" or .eventid=="cowrie.login.success") | .username' cowrie.json | sort | uniq -c | sort -nr | head
```

## Top Passwords

```bash
jq -r 'select(.eventid=="cowrie.login.failed" or .eventid=="cowrie.login.success") | .password' cowrie.json | sort | uniq -c | sort -nr | head
```

## Source IP Counts

```bash
jq -r '.src_ip // empty' cowrie.json | sort | uniq -c | sort -nr | head
```

## Commands Attempted

```bash
jq -r 'select(.eventid=="cowrie.command.input") | .input' cowrie.json | sort | uniq -c | sort -nr | head
```

## Time To First Contact

Record the public exposure time, then compare it with the first Cowrie event timestamp.
