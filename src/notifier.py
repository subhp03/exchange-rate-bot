"""Sends exchange-rate notifications via ntfy.

TODO: implement ntfy notification logic. Topic/credentials should be read
from environment variables (e.g. NTFY_TOPIC, NTFY_URL), not hardcoded.
"""


def send_notification(usd_to_inr: float, eur_to_inr: float) -> None:
    raise NotImplementedError
