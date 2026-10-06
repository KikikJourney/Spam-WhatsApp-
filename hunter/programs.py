"""Curated public bounty targets whose published rules support crypto rewards.
Network/payment terms are informational and must be re-checked before submission.
No private credentials or payout wallet addresses belong in this repository.
"""
PROGRAMS = [
    {"name":"Symbiosis","platform":"Immunefi","program_url":"https://immunefi.com/bug-bounty/symbiosis/information/","max_bounty_usd":100000,"payouts":["USDT(BEP20)","USDT(ERC20)","USDC(ERC20)","USDC(Polygon)"],"scope_mode":"local-fork-only","poc_required":True},
    {"name":"Tether","platform":"Direct program","program_url":"https://tether.io/bug-bounty/","max_bounty_usd":10000000,"payouts":["USDt","Bitcoin","other digital token at Tether discretion"],"scope_mode":"program-rules","poc_required":True},
    {"name":"Lido","platform":"Immunefi","program_url":"https://immunefi.com/bug-bounty/lido/information/","max_bounty_usd":1000000,"payouts":["USDC","USDS","DAI","USDT"],"scope_mode":"program-rules","poc_required":True},
]
def payout_candidates(network: str = "BEP20") -> list[dict]:
    needle = network.upper().replace("-", "")
    return [p for p in PROGRAMS if any(needle in payout.upper().replace("-", "") for payout in p["payouts"])]
