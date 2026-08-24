# exchange-rate-bot

A simple daily currency exchange-rate tracker to track USD-INR and EUR-INR rates

## What it does

Once a day, at 11:00 AM IST, a GitHub Actions workflow will:

1. Fetch the current USD→INR and EUR→INR exchange rates from Yahoo Finance.
2. Timestamp the result and save it as a new JSON file in [runs/](runs/),
   building up a historical record rather than overwriting previous data.
3. Send a push notification with the rates via [ntfy](https://ntfy.sh).
4. Commit and push the new run file back to the repository.

## Architecture

```text
exchange-rate-bot/
├── .github/
│   └── workflows/
│       └── exchange-rate.yml   # run + commit/push
├── src/
│   ├── scraper.py               # fetch rates from Yahoo Finance
│   ├── notifier.py              # send rate notification via ntfy
│   └── main.py                  # orchestrates scrape -> save -> notify
├── runs/
│   └── *.json                    # one file per run saved as json
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

- **scraper.py** — fetches USD→INR and EUR→INR rates from Yahoo Finance's
  quote API.
- **notifier.py** — sends the exchange-rate notification through ntfy.
- **main.py** — orchestrates the application: scrape rates, timestamp the
  result, save it to `runs/`, and send the notification.
- **runs/** — one JSON file per run (timestamp + both rates), appended to
  (never overwritten).
- **.github/workflows/exchange-rate.yml** — runs the application daily and
  commits/pushes the new run file back to the repo.

ntfy topic is provided via GitHub Actions environment
variables/secrets, never hardcoded in source. See [.env.example](.env.example)
for the expected variable when running locally. No credentials needed apart from the secret for running NTFY via the public server.

## Running locally

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in your NTFY_TOPIC
python src/main.py
```

## Status

Scraping, notification, run persistence, and the daily GitHub Actions
schedule are all implemented.
