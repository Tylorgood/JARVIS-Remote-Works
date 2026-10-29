from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class ATSResult:
    provider: str
    confidence: float
    host: str
    application_path: str


HOST_RULES = {
    "greenhouse.io": "greenhouse",
    "boards.greenhouse.io": "greenhouse",
    "job-boards.greenhouse.io": "greenhouse",
    "lever.co": "lever",
    "jobs.lever.co": "lever",
    "ashbyhq.com": "ashby",
    "jobs.ashbyhq.com": "ashby",
    "myworkdayjobs.com": "workday",
    "smartrecruiters.com": "smartrecruiters",
    "jobs.smartrecruiters.com": "smartrecruiters",
    "workable.com": "workable",
    "apply.workable.com": "workable",
    "recruitee.com": "recruitee",
    "personio.de": "personio",
    "personio.com": "personio",
    "bamboohr.com": "bamboohr",
    "breezy.hr": "breezy",
}


def detect_ats(url: str) -> ATSResult:
    host = urlparse(url).netloc.lower().split(":")[0]
    for suffix, provider in HOST_RULES.items():
        if host == suffix or host.endswith("." + suffix):
            return ATSResult(provider, 0.99, host, "public_api_or_direct")
    return ATSResult("unknown", 0.20, host, "inspect_then_browser_fallback")
