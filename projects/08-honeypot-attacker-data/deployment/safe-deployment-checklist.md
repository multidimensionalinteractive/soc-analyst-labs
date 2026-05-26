# Honeypot Safe Deployment Checklist

## Before Deployment

- Use a disposable VM or cloud instance.
- Use a dedicated lab account or project.
- Set a budget alert.
- Use unique credentials that are never reused.
- Restrict management SSH to your IP.
- Do not place the honeypot on a trusted internal network.
- Confirm logging location and retention.

## Deployment

1. Install Docker on the disposable host.
2. Copy `cowrie-docker-compose.yml` to the host.
3. Expose the honeypot on a non-management port first, such as TCP 2222.
4. Confirm management SSH is not sharing the honeypot listener.
5. Start the container.

```bash
docker compose -f cowrie-docker-compose.yml up -d
```

## Monitoring Window

- Record start time.
- Record exposed port.
- Capture authentication attempts and command logs.
- Stop the lab after the bounded time window.

## Teardown

1. Stop the container.
2. Archive sanitized logs.
3. Delete the VM or close exposed ports.
4. Confirm no public listener remains.
5. Confirm no unexpected cloud resources remain.
