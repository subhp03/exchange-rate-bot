# exchange-rate-bot

A small daily exchange-rate tracker, built as a learning project for scheduled
GitHub Actions jobs, web scraping, data persistence, environment variables /
secrets, and external notifications.

## What it does (once fully implemented)

Once a day, around 4:00 PM IST, a GitHub Actions workflow will:

1. Scrape the current USD→INR and EUR→INR exchange rates from Google Search.
2. Validate and timestamp the scraped rates.
3. Append the result as a new row in [data/rates.csv](data/rates.csv), building
   up a historical record rather than overwriting previous data.
4. Send a push notification with the rates via [ntfy](https://ntfy.sh).
5. Commit and push the updated CSV back to the repository.

## Architecture

```text
exchange-rate-bot/
├── .github/
│   └── workflows/
│       └── exchange-rate.yml   # daily schedule, run + commit/push (TODO)
├── src/
│   ├── scraper.py               # scrape/parse rates from Google Search (TODO)
│   ├── notifier.py              # send rate notification via ntfy (TODO)
│   └── main.py                  # orchestrates scrape -> validate -> save -> notify (TODO)
├── data/
│   └── rates.csv                 # historical daily exchange-rate records
├── .gitignore
├── README.md
└── requirements.txt
```

- **scraper.py** — will contain the Google Search scraping/parsing logic and
  return the USD→INR and EUR→INR rates.
- **notifier.py** — will handle sending the exchange-rate notification through
  ntfy.
- **main.py** — orchestrates the application: scrape rates, validate them,
  timestamp the result, append it to the CSV, and send the notification.
- **data/rates.csv** — historical daily exchange-rate records, appended to
  (never overwritten).
- **.github/workflows/exchange-rate.yml** — will run the application on a
  daily schedule and commit/push updated data back to the repo.

ntfy credentials/topic are provided via GitHub Actions environment
variables/secrets, never hardcoded in source.

## Running locally

```bash
pip install -r requirements.txt
python src/main.py
```

## Status

This repository currently contains only the initial project scaffolding.
Scraping, notification, and GitHub Actions automation are not yet
implemented.
