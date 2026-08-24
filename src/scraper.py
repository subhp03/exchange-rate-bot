"""Fetches current USD->INR and EUR->INR exchange rates from Yahoo Finance."""

import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}
CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}" # Yahoo finance uses INR=X for USD/INR and EURINR=X for EUR/INR


def _get_rate(symbol: str) -> float:
    response = requests.get(
        CHART_URL.format(symbol=symbol), headers=HEADERS, timeout=10
    )
    response.raise_for_status()
    data = response.json()
    return float(data["chart"]["result"][0]["meta"]["regularMarketPrice"])


def get_usd_to_inr() -> float:
    return _get_rate("INR=X")


def get_eur_to_inr() -> float:
    return _get_rate("EURINR=X")
