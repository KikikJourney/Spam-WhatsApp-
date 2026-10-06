"""Curated public bounty targets with crypto-compatible rewards.

Network/payment terms are informational and must be re-checked before submission.
No private credentials or payout wallet addresses belong in this repository.
"""
PROGRAMS = [
    {
        "name": "Symbiosis",
        "platform": "Immunefi",
        "program_url": "https://immunefi.com/bug-bounty/symbiosis/information/",
        "scope_url": "https://immunefi.com/bug-bounty/symbiosis/scope/",
        "max_bounty_usd": 100000,
        "payouts": ["USDT(BEP20)", "USDT(ERC20)", "USDC(ERC20)", "USDC(Polygon)"],
        "scope_mode": "local-fork-only",
        "poc_required": True,
        "scope_assets": 8,
        "scope_impacts": ["ERC-20 fund theft", "permanent ERC-20 fund freezing"],
        "excluded": ["best-practice-only", "Sybil-only", "centralization-only", "public-mainnet-testing", "public-testnet-testing"],
    },
    {
        "name": "Tether",
        "platform": "Direct program",
        "program_url": "https://tether.io/bug-bounty/",
        "scope_url": "https://github.com/tetherto/tether-io-bug-bounty-scope",
        "max_bounty_usd": 10000000,
        "payouts": ["USDt", "Bitcoin", "other digital token at Tether discretion"],
        "scope_mode": "program-rules",
        "poc_required": True,
        "excluded": ["best-practice-only", "unverified-scanner-output", "theoretical-only", "destructive-DoS"],
    },
    {
        "name": "Lido",
        "platform": "Immunefi",
        "program_url": "https://immunefi.com/bug-bounty/lido/information/",
        "max_bounty_usd": 1000000,
        "payouts": ["USDC", "USDS", "DAI", "USDT"],
        "scope_mode": "program-rules",
        "poc_required": True,
    },
]


def payout_candidates(network: str = "BEP20") -> list[dict]:
    needle = network.upper().replace("-", "")
    return [p for p in PROGRAMS if any(needle in payout.upper().replace("-", "") for payout in p["payouts"])]


def research_queue(preferred_network: str = "BEP20") -> list[dict]:
    """Deterministic priority queue; performs no network or target activity."""
    candidates = payout_candidates(preferred_network)
    return sorted(candidates, key=lambda p: p["max_bounty_usd"], reverse=True)
