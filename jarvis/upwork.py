from __future__ import annotations

import os
from dataclasses import dataclass

import httpx

UPWORK_GRAPHQL_URL = "https://api.upwork.com/graphql"
UPWORK_TOKEN_URL = "https://www.upwork.com/api/v3/oauth2/token"


@dataclass
class UpworkConfig:
    client_id: str
    client_secret: str
    redirect_uri: str
    tenant_id: str | None = None

    @classmethod
    def from_env(cls) -> "UpworkConfig":
        return cls(
            client_id=os.getenv("UPWORK_CLIENT_ID", ""),
            client_secret=os.getenv("UPWORK_CLIENT_SECRET", ""),
            redirect_uri=os.getenv("UPWORK_REDIRECT_URI", ""),
            tenant_id=os.getenv("UPWORK_TENANT_ID") or None,
        )

    def configured(self) -> bool:
        return bool(self.client_id and self.client_secret and self.redirect_uri)


class UpworkClient:
    def __init__(self, access_token: str, tenant_id: str | None = None):
        self.access_token = access_token
        self.tenant_id = tenant_id

    def graphql(self, query: str, variables: dict | None = None) -> dict:
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        if self.tenant_id:
            headers["X-Upwork-API-TenantId"] = self.tenant_id
        with httpx.Client(timeout=30) as client:
            response = client.post(
                UPWORK_GRAPHQL_URL,
                headers=headers,
                json={"query": query, "variables": variables or {}},
            )
            response.raise_for_status()
            payload = response.json()
            if payload.get("errors"):
                raise RuntimeError(f"Upwork GraphQL error: {payload['errors']}")
            return payload.get("data", {})


def submission_allowed(approval_status: str) -> bool:
    """Hard gate: proposals/applications only leave JARVIS after approval."""
    return approval_status.upper() == "APPROVED"
