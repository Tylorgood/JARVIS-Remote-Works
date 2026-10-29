from __future__ import annotations

import argparse
import json

from jarvis.ats_detector import detect_ats
from jarvis.scoring import ScoreInput, action_for, score_job
from jarvis.upwork import UpworkConfig


def main() -> None:
    parser = argparse.ArgumentParser(prog="jarvis-remote-works")
    sub = parser.add_subparsers(dest="command", required=True)

    detect = sub.add_parser("detect", help="Detect ATS from a job URL")
    detect.add_argument("url")

    score = sub.add_parser("score", help="Score an opportunity")
    score.add_argument("--skill", type=int, required=True)
    score.add_argument("--pay", type=int, required=True)
    score.add_argument("--remote", type=int, required=True)
    score.add_argument("--credibility", type=int, required=True)
    score.add_argument("--competition", type=int, required=True)

    sub.add_parser("upwork-status", help="Check whether Upwork credentials are configured")

    args = parser.parse_args()
    if args.command == "detect":
        print(json.dumps(detect_ats(args.url).__dict__, indent=2))
    elif args.command == "score":
        value = score_job(ScoreInput(args.skill, args.pay, args.remote, args.credibility, args.competition))
        print(json.dumps({"score": value, "action": action_for(value)}, indent=2))
    elif args.command == "upwork-status":
        cfg = UpworkConfig.from_env()
        print(json.dumps({"configured": cfg.configured(), "tenant_id_set": bool(cfg.tenant_id)}, indent=2))


if __name__ == "__main__":
    main()
