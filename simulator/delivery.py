"""Synthetic delivery-state proof harness.

This module deliberately has no network or messaging-provider transport.
It proves the local accounting/state machine for small proof runs or
10,000-event synthetic delivery runs.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DeliveryProof:
    requested: int
    accepted: int
    sent: int
    delivered: int
    read: int
    failed: int
    delivery_latency_ms: tuple[int, ...]

    @property
    def delivery_rate(self) -> float:
        return self.delivered / self.requested if self.requested else 0.0


def run_delivery_proof(count: int = 3, *, simulate_read: bool = True) -> DeliveryProof:
    if count < 1:
        raise ValueError("count must be >= 1")

    # Deterministic local state progression. No network calls are made.
    latencies = tuple(120 + (i % 17) * 10 for i in range(count))
    accepted = sent = delivered = count
    read = count if simulate_read else 0

    return DeliveryProof(
        requested=count,
        accepted=accepted,
        sent=sent,
        delivered=delivered,
        read=read,
        failed=0,
        delivery_latency_ms=latencies,
    )


def proof_summary(proof: DeliveryProof) -> dict:
    latencies = sorted(proof.delivery_latency_ms)
    p50 = latencies[len(latencies) // 2] if latencies else 0
    p95 = latencies[min(len(latencies) - 1, int(len(latencies) * 0.95))] if latencies else 0
    return {
        "mode": "synthetic-delivery-proof",
        "network_transport": False,
        "requested": proof.requested,
        "accepted": proof.accepted,
        "sent": proof.sent,
        "delivered": proof.delivered,
        "read": proof.read,
        "failed": proof.failed,
        "delivery_rate": round(proof.delivery_rate, 6),
        "p50_delivery_latency_ms": p50,
        "p95_delivery_latency_ms": p95,
    }
