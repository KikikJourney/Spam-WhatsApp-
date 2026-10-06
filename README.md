# WhatsApp Target Load Simulator

Local-only simulator for testing message-processing behavior against a synthetic transport.

## Safety boundary

This project does **not** connect to WhatsApp, WhatsApp Web, Meta Cloud API, Twilio, or any external messaging service. It never sends messages.

The configured phone value is a **fixture only** for parsing/validation tests:

```text
TARGET_PHONE=+6285722907443
REAL_PHONE_TRANSPORT=false
NETWORK_TRANSPORT=false
```

All generated traffic is processed by an in-memory simulator.

## Run

```bash
python -m simulator --scenario burst --messages 10000 --rate 1000
python -m simulator --scenario sustained --messages 50000 --rate 500
python -m simulator --scenario retry-storm --messages 20000 --rate 1000 --failure-rate 0.05
python -m unittest discover -s tests -v
```

## Scenarios

- burst
- sustained
- duplicates
- retry-storm

## Metrics

Generated, processed, failed, retried, duplicates, dropped messages, deterministic simulated latency, p50/p95/p99 latency, and benchmark throughput.

No network transport is implemented.
