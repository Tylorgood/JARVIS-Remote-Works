# JARVIS Remote Works

API-first job-search operating system for Tylor Good.

## V1

- Upwork Worker: ingest -> normalize -> dedupe -> score -> shortlist -> draft -> approval -> submit -> track
- ATS Detector: identify ATS from a job URL and select the best application path
- Approval gate before any proposal/application is submitted
- Local SQLite ledger with export hooks for the JARVIS job tracker

## Safety rules

- Never commit API keys, OAuth tokens, passwords, or applicant-sensitive data.
- Never submit a proposal/application without an explicit approval state.
- Never fabricate qualifications or answers.
- Browser automation is a fallback, not the primary transport.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux
python -m jarvis.cli init-db
python -m jarvis.cli detect "https://boards.greenhouse.io/example/jobs/123"
```

Upwork remains disabled until API credentials and OAuth authorization are configured.
