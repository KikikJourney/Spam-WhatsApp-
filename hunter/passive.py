import json
import ssl
import urllib.request
from urllib.error import HTTPError, URLError
from .checks import check_cors, check_security_headers
from .models import Finding, HuntReport, Target
from .scope import validate_target

def fetch_headers(target: Target, timeout: int = 8) -> tuple[int, dict[str, str]]:
    url = validate_target(target.base_url)
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "ScopedBugHunter/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            return response.status, dict(response.headers.items())
    except HTTPError as exc:
        return exc.code, dict(exc.headers.items())
    except URLError as exc:
        raise RuntimeError(f"target fetch failed: {exc.reason}") from exc

def hunt(target: Target) -> HuntReport:
    if not target.in_scope:
        raise ValueError("target is marked out of scope")
    status, headers = fetch_headers(target)
    report = HuntReport(target=target)
    for check in (check_security_headers, check_cors):
        report.checks_run += 1
        report.findings.extend(check(target, headers))
    if status >= 500:
        report.add(Finding(
            check_id="availability/http-5xx", title="Server returned 5xx to HEAD", severity="info",
            target=target.base_url, evidence=f"HTTP status {status}.",
            remediation="Review server logs and error handling if the response is unexpected.",
            confidence="medium"))
    return report

def report_json(report: HuntReport) -> str:
    return json.dumps({
        "target": report.target.base_url,
        "checks_run": report.checks_run,
        "findings": [f.__dict__ for f in report.findings],
    }, indent=2)
