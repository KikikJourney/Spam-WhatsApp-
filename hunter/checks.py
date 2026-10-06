from .models import Finding, Target

def check_security_headers(target: Target, headers: dict[str, str]) -> list[Finding]:
    findings = []
    normalized = {k.lower(): v for k, v in headers.items()}
    required = {
        "strict-transport-security": ("HSTS missing", "high"),
        "content-security-policy": ("Content-Security-Policy missing", "medium"),
        "x-content-type-options": ("X-Content-Type-Options missing", "low"),
        "referrer-policy": ("Referrer-Policy missing", "low"),
    }
    for header, (title, severity) in required.items():
        if header not in normalized:
            findings.append(Finding(
                check_id=f"headers/{header}", title=title, severity=severity,
                target=target.base_url,
                evidence=f"Response did not expose {header}.",
                remediation=f"Consider setting {header} with a policy appropriate to the application.",
                confidence="high"))
    return findings

def check_cors(target: Target, headers: dict[str, str]) -> list[Finding]:
    value = next((v for k, v in headers.items() if k.lower() == "access-control-allow-origin"), None)
    if value == "*":
        return [Finding(
            check_id="cors/wildcard", title="Wildcard CORS policy", severity="medium",
            target=target.base_url,
            evidence="Access-Control-Allow-Origin is '*'.",
            remediation="Restrict allowed origins when authenticated or sensitive resources are exposed.",
            confidence="medium")]
    return []
