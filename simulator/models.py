from dataclasses import dataclass

@dataclass(frozen=True)
class SimulationConfig:
    scenario: str = "burst"
    messages: int = 100
    rate: int = 100
    failure_rate: float = 0.0
    duplicate_rate: float = 0.0
    retry_limit: int = 2
    target_id: str = "test-user-0001"

@dataclass(frozen=True)
class SimulationResult:
    generated: int
    processed: int
    failed: int
    retried: int
    duplicates: int
    dropped: int
    latency_ms: tuple[int, ...]
    duration_seconds: float
    throughput_per_second: float
