"""Orchestrates the exchange-rate tracker: scrape -> save -> notify."""

import json
from datetime import datetime, timezone
from pathlib import Path

from notifier import send_notification
from scraper import get_eur_to_inr, get_usd_to_inr

_RUNS_DIR = Path(__file__).resolve().parent.parent / "runs"


def main() -> None:
    usd_to_inr = get_usd_to_inr()
    eur_to_inr = get_eur_to_inr()

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    _RUNS_DIR.mkdir(exist_ok=True)
    run_path = _RUNS_DIR / f"{timestamp.replace(':', '-')}.json"
    run_path.write_text(
        json.dumps(
            {
                "timestamp": timestamp,
                "usd_rate": usd_to_inr,
                "euro_rate": eur_to_inr,
            },
            indent=2,
        ),
        encoding="UTF-8"
    )

    send_notification(usd_to_inr, eur_to_inr)


if __name__ == "__main__":
    main()
