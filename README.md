# Pokémon Bulk Price Tracker

> An automated data engineering pipeline that tracks eBay prices for
> Pokémon TCG bulk cards — commons, reverse holos, holos, Poké Balls,
> and Master Balls.

## What it does

- Fetches live listings from the eBay Browse API on a schedule
- Stores raw snapshots in AWS S3 (Hive-partitioned JSON + Parquet)
- Persists listings and daily price aggregates in PostgreSQL
- Serves a Flask dashboard with filters, price history charts, and CSV export
- Runs the ETL pipeline serverlessly via AWS Lambda + EventBridge

## Tech stack

| Layer | Technology |
|---|---|
| Ingestion | Python, eBay Browse API, OAuth2 |
| Storage | AWS S3 (raw JSON + Parquet), PostgreSQL / SQLite |
| Transform | Pandas, custom deal-scoring logic |
| Orchestration | AWS Lambda, EventBridge (cron), APScheduler (local) |
| Serving | Flask, Chart.js |

## Files Created/Edited Folder Structure
- [x] Phase 1 — Project setup and config
myPokeBulk
|--config.py
|--.env
|--.gitignore
|--requirements.txt
- [ ] Phase 2 — eBay API client
- [ ] Phase 3 — Database layer
- [ ] Phase 4 — Pipeline and transforms
- [ ] Phase 5 — Flask dashboard
- [ ] Phase 6 — S3 and Lambda


## Setup

_(fill in during Phase 5 when the app is runnable)_

## Phase progress

- [x] Phase 1 — Project setup and config
- [ ] Phase 2 — eBay API client
- [ ] Phase 3 — Database layer
- [ ] Phase 4 — Pipeline and transforms
- [ ] Phase 5 — Flask dashboard
- [ ] Phase 6 — S3 and Lambda