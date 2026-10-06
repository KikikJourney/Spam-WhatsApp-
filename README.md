# Scoped Bug Hunter

This repository is now a scope-first bug-hunting workspace. The previous WhatsApp traffic simulator is retired from the primary workflow.

## Profit target

The objective is to find valid, in-scope vulnerabilities and submit them through the program's approved channel for bounty payment. The target payment preference is crypto; programs are selected only when their published terms support a compatible payout.

A payout wallet is never committed to this public repository. Keep the payout address in a private account/platform payout setting or an untracked local secret.

## Current crypto-bounty targets

- Symbiosis / Immunefi — published maximum bounty $100,000 and explicitly supports USDT(BEP20), USDT(ERC20), USDC(ERC20), and USDC(Polygon). Its rules require PoC for all severities and require local-fork testing rather than testing deployed mainnet/public-testnet code.
- Tether — published bounty program; rewards are denominated in USD and may be paid in USDt, Bitcoin, or another digital token at Tether's discretion. Do not assume a particular network.
- Lido / Immunefi — publishes rewards payable in USDT and other stablecoins; exact network/payment terms must be confirmed before submission.

## Hunter workflow

scope -> passive discovery -> evidence -> manual validation -> severity -> report draft -> submit

The engine is deliberately non-destructive. It does not brute-force, flood, exploit third-party systems, bypass authentication, or scan assets that are not explicitly authorized.

## Run

    python -m unittest discover -s tests -v
    python -m hunter --target https://YOUR-AUTHORIZED-TARGET.example --name my-target

Only use an asset after confirming it is in scope and that the program permits the planned testing method.

## Money rule

No bounty is counted as revenue until the program confirms the finding as valid and awards payment. Duplicate, informational, out-of-scope, or unverified reports are not treated as profit.

## Evidence standard

Every serious candidate should have: exact in-scope asset, affected component, minimal reproduction, evidence/PoC, concrete impact, severity rationale, remediation, program-specific policy check, submission reference, and final bounty status.

The repository contains no private payout wallet, API token, session cookie, or platform credential.
