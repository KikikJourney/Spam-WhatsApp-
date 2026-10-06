import argparse
import json

from .engine import run, summary
from .models import SimulationConfig


def main():
    parser = argparse.ArgumentParser(description="Local-only message traffic load simulator")
    parser.add_argument("--scenario", choices=["burst", "sustained", "duplicates", "retry-storm"], default="burst")
    parser.add_argument("--messages", type=int, default=100)
    parser.add_argument("--rate", type=int, default=100)
    parser.add_argument("--failure-rate", type=float, default=0.0)
    parser.add_argument("--duplicate-rate", type=float, default=0.0)
    parser.add_argument("--retry-limit", type=int, default=2)
    args = parser.parse_args()

    cfg = SimulationConfig(
        scenario=args.scenario,
        messages=args.messages,
        rate=args.rate,
        failure_rate=args.failure_rate if args.failure_rate else (0.05 if args.scenario == "retry-storm" else 0.0),
        duplicate_rate=args.duplicate_rate if args.duplicate_rate else (1.0 if args.scenario == "duplicates" else 0.0),
    )
    print(json.dumps(summary(run(cfg)), indent=2))


if __name__ == "__main__":
    main()
