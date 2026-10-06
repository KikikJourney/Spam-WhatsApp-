# WhatsApp Target Load Simulator

Local-only load/flood simulator for testing message-processing behavior against a synthetic transport.

## Safety boundary

This project does **not** connect to WhatsApp, WhatsApp Web, Meta Cloud API, Twilio, or any external messaging service. It never sends messages.

The real-number value used for fixture validation is stored only in code under `simulator/fixture.py`. It is never used as a network destination.

All generated traffic is processed by an in-memory simulator.

## Run

```bash
python -m simulator --scenario burst --messages 10000 --rate 1000
python -m simulator --scenario sustained --messages 50000 --rate 500
python -m simulator --scenario duplicates --messages 10000 --rate 1000
python -m simulator --scenario retry-storm --messages 20000 --rate 1000 --failure-rate 0.05
python -m simulator --scenario delivery-proof --delivery-count 3
python -m simulator --scenario delivery-proof --delivery-count 10000
python -m unittest discover -s tests -v
```

## Delivery proof mode

`delivery-proof` is a **synthetic** state-machine test. The minimum proof run is 1 event; the default is 3 events; 10,000 events are supported for stress validation. It reports `accepted → sent → delivered → read` accounting and delivery-latency statistics, but `network_transport` remains `false` by design. Therefore it is not evidence that a real WhatsApp message reached a handset.

## Scenarios

- **burst** — immediate synthetic burst against the virtual queue.
- **sustained** — synthetic traffic budget evaluated across the configured rate.
- **duplicates** — duplicate-event pressure.
- **retry-storm** — deterministic failure and bounded-retry pressure.
- **delivery-proof** — synthetic delivery-state accounting; supports small proof runs through 10,000 events.

The workload model follows the same core ideas used by mature load-testing tools such as Locust: configurable request/event volume, rate, failure injection, retries, and measurable outcomes. This repository keeps the transport layer deliberately synthetic.

## Metrics

Generated, processed, failed, retried, duplicates, dropped events, deterministic simulated latency, p50/p95/p99 latency, and benchmark throughput.

## Guarantees

- No WhatsApp transport.
- No browser automation.
- No external messaging API.
- No virtual phone/SIM provisioning.
- No network calls from the simulator.
- Fixture phone data is isolated in code and never used for delivery.
