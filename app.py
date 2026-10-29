from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="JARVIS Remote Works", version="0.1.0")


@app.get("/")
def root():
    return {"service": "JARVIS Remote Works", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/auth/upwork/callback")
def upwork_callback(
    code: str | None = Query(default=None),
    state: str | None = Query(default=None),
    error: str | None = Query(default=None),
):
    """
    OAuth redirect target for Upwork.

    This endpoint intentionally does not exchange or persist tokens yet.
    Once credentials are approved, the token exchange will be added using
    environment variables on Render rather than committed secrets.
    """
    if error:
        return JSONResponse(
            status_code=400,
            content={"status": "oauth_error", "error": error, "state": state},
        )

    if code:
        return {
            "status": "authorization_received",
            "message": "OAuth authorization code received. Token exchange is not enabled yet.",
            "state": state,
        }

    return {
        "status": "ready",
        "message": "JARVIS Upwork OAuth callback endpoint is online.",
    }
