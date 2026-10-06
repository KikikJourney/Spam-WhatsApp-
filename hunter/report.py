from dataclasses import dataclass
from .models import Finding

@dataclass(frozen=True)
class SubmissionDraft:
    title: str
    summary: str
    impact: str
    reproduction: str
    evidence: str
    remediation: str

def from_finding(finding: Finding) -> SubmissionDraft:
    return SubmissionDraft(
        title=finding.title,
        summary=finding.evidence,
        impact="Validate concrete security impact against the program severity rules before submission.",
        reproduction="Document the minimal, non-destructive reproduction used to validate the finding.",
        evidence=finding.evidence,
        remediation=finding.remediation,
    )
