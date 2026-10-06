# Scoped Bug Hunter

This repository has been rebuilt as a scope-first bug-hunting toolkit for authorized security research. The former WhatsApp traffic simulator is no longer the primary workflow.

## Operating model

1. Define an explicitly authorized target.
2. Run non-destructive passive checks.
3. Capture evidence and confidence.
4. Manually validate before submission.
5. Report only through the program's approved channel.

Bug-bounty programs require researchers to stay within published target scope and testing rules. Out-of-scope testing can make a report ineligible and can affect platform access.

## Current checks

- HSTS, CSP, X-Content-Type-Options, and Referrer-Policy checks.
- Wildcard CORS detection.
- Basic HTTP status observation.
- URL and scope validation.

The hunter does not brute-force, exploit, flood, bypass authentication, or attack unspecified third-party systems.

## Run

    python -m unittest discover -s tests -v
    python -m hunter --target https://YOUR-AUTHORIZED-TARGET.example --name my-target

Only use an asset explicitly listed as in-scope by the applicable bounty program.

## Reporting

A useful finding should contain target, affected component, reproduction steps, evidence or PoC, impact, and remediation. Manually validate findings before submission.

Do not publicly disclose private-program findings without program permission; follow the program's disclosure policy.
