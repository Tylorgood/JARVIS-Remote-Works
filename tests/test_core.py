from jarvis.ats_detector import detect_ats
from jarvis.scoring import ScoreInput, action_for, score_job
from jarvis.upwork import submission_allowed


def test_detect_greenhouse():
    result = detect_ats("https://boards.greenhouse.io/acme/jobs/123")
    assert result.provider == "greenhouse"


def test_detect_workday():
    result = detect_ats("https://company.wd5.myworkdayjobs.com/jobs/job/abc")
    assert result.provider == "workday"


def test_score_and_action():
    value = score_job(ScoreInput(98, 95, 100, 90, 20))
    assert value >= 90
    assert action_for(value) == "INTERRUPT_APPLY_ASAP"


def test_submission_gate():
    assert submission_allowed("APPROVED") is True
    assert submission_allowed("DRAFT") is False
