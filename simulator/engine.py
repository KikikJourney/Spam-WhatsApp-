import time
from .models import SimulationConfig, SimulationResult


def _percentile(values, p):
    if not values:
        return 0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((p / 100) * (len(ordered) - 1)))))
    return ordered[idx]


def _failure_slot(failure_rate):
    if failure_rate <= 0:
        return None
    return max(1, round(1 / failure_rate))


def run(config: SimulationConfig) -> SimulationResult:
    if config.messages < 0:
        raise ValueError("messages must be >= 0")
    if config.rate <= 0:
        raise ValueError("rate must be > 0")
    if not 0 <= config.failure_rate <= 1:
        raise ValueError("failure_rate must be between 0 and 1")
    if not 0 <= config.duplicate_rate <= 1:
        raise ValueError("duplicate_rate must be between 0 and 1")
    if config.retry_limit < 0:
        raise ValueError("retry_limit must be >= 0")

    started = time.perf_counter()
    generated = config.messages
    duplicates = int(generated * config.duplicate_rate)
    total_attempts = generated + duplicates
    failure_slot = _failure_slot(config.failure_rate)

    failed = 0
    retried = 0
    processed = 0
    dropped = 0
    latencies = []

    # Locust-style load-test concepts are represented here without a real transport:
    # event generation, bounded retries, failure injection, and measurable latency.
    # The rate is a virtual workload budget, so the benchmark never sleeps or calls
    # a network endpoint.
    for i in range(total_attempts):
        is_failure = failure_slot is not None and i % failure_slot == 0
        if not is_failure:
            processed += 1
            latencies.append(5 + (i % 11))
            continue

        failed += 1
        for attempt in range(config.retry_limit):
            retried += 1
            if failure_slot is None or (i + attempt + 1) % failure_slot != 0:
                processed += 1
                latencies.append(8 + ((i + attempt) % 13))
                break
        else:
            dropped += 1

    elapsed = max(time.perf_counter() - started, 1e-9)
    return SimulationResult(
        generated=generated,
        processed=processed,
        failed=failed,
        retried=retried,
        duplicates=duplicates,
        dropped=dropped,
        latency_ms=tuple(latencies),
        duration_seconds=elapsed,
        throughput_per_second=processed / elapsed,
    )


def summary(result: SimulationResult) -> dict:
    return {
        "generated": result.generated,
        "processed": result.processed,
        "failed": result.failed,
        "retried": result.retried,
        "duplicates": result.duplicates,
        "dropped": result.dropped,
        "p50_latency_ms": _percentile(result.latency_ms, 50),
        "p95_latency_ms": _percentile(result.latency_ms, 95),
        "p99_latency_ms": _percentile(result.latency_ms, 99),
        "duration_seconds": round(result.duration_seconds, 6),
        "throughput_per_second": round(result.throughput_per_second, 2),
        "configured_rate_per_second": result.generated / max(result.duration_seconds, 1e-9),
    }
