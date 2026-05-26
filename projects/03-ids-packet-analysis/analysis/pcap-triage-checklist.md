# PCAP Triage Checklist

## Alert Context

- IDS rule name:
- Alert timestamp:
- Source IP and port:
- Destination IP and port:
- Protocol:
- Related hostname or user:

## Packet Review

1. Open the PCAP in Wireshark or tshark.
2. Filter on the alert source and destination pair.
3. Follow the TCP or HTTP stream if safe.
4. Record user agent, host header, DNS query, TLS SNI, and payload clues.
5. Compare the packet evidence to the IDS rule.
6. Decide whether the alert is true positive, false positive, or inconclusive.

## Useful Filters

```text
ip.addr == 192.0.2.10
```

```text
http.request or dns or tls
```

```text
tcp.stream eq 3
```

## Reporting Notes

Explain what the packets prove. Do not rely on the IDS alert alone.
