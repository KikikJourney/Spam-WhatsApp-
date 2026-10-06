from dataclasses import dataclass, field

@dataclass(frozen=True)
class Target:
    name: str
    base_url: str
    in_scope: bool = True
    notes: str = ""

@dataclass(frozen=True)
class Finding:
    check_id: str
    title: str
    severity: str
    target: str
    evidence: str
    remediation: str
    confidence: str = "medium"

@dataclass
class HuntReport:
    target: Target
    findings: list[Finding] = field(default_factory=list)
    checks_run: int = 0

    def add(self, finding: Finding) -> None:
        self.findings.append(finding)
