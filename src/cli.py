from __future__ import annotations

import argparse
import json
from pathlib import Path

from .io_utils import load_portfolio_json
from .analysis import analyze_portfolio
from .ml_model import train_decision_tree


def cmd_analyze(args: argparse.Namespace) -> int:
    portfolio = load_portfolio_json(args.portfolio)
    out = analyze_portfolio(portfolio, prices_dir=args.prices_dir)
    print(json.dumps(out, indent=2))
    return 0


def cmd_train_ml(args: argparse.Namespace) -> int:
    res = train_decision_tree(seed=args.seed)
    print("Decision Tree (synthetic risk classifier) report:")
    print(res.report)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="portfolio-risk-analyzer")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze", help="Analyze a portfolio using local price CSVs")
    a.add_argument("--portfolio", required=True, help="Path to portfolio JSON")
    a.add_argument("--prices_dir", required=True, help="Directory with <TICKER>.csv files")
    a.set_defaults(func=cmd_analyze)

    t = sub.add_parser("train-ml", help="Train a small decision tree model on synthetic data (demo)")
    t.add_argument("--seed", type=int, default=42)
    t.set_defaults(func=cmd_train_ml)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
