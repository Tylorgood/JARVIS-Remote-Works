from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreInput:
    skill_match: int
    pay_quality: int
    remote_fit: int
    credibility: int
    competition: int


def score_job(x: ScoreInput) -> int:
    """Return a 0-100 opportunity score.

    competition is 0-100 where a higher value means more competition.
    """
    raw = (
        x.skill_match * 0.45
        + x.pay_quality * 0.20
        + x.remote_fit * 0.15
        + x.credibility * 0.15
        + (100 - x.competition) * 0.05
    )
    return max(0, min(100, round(raw)))


def action_for(score: int) -> str:
    if score >= 90:
        return "INTERRUPT_APPLY_ASAP"
    if score >= 80:
        return "PROPOSAL_TODAY"
    if score >= 70:
        return "BACKLOG_REVIEW"
    return "IGNORE"
