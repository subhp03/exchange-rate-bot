"""Sends exchange-rate notifications via ntfy."""

import os

import requests

NTFY_URL = "https://ntfy.sh/{topic}"


def send_notification(usd_to_inr: float, eur_to_inr: float) -> None:
    topic = os.environ["NTFY_TOPIC"]
    message = f"USD -> INR: {usd_to_inr:.4f} | EUR -> INR: {eur_to_inr:.4f}"
    response = requests.post(NTFY_URL.format(topic=topic), data=message.encode())
    response.raise_for_status()
