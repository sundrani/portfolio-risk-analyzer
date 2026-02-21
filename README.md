# Portfolio Risk Analyzer (Risk Score + Allocation Bucket) 📈🛡️

A small, production-style Python project that:
- Computes portfolio risk metrics (volatility, max drawdown, VaR/CVaR, Sharpe, beta vs benchmark)
- Produces a **risk score (0–100)** and **risk bucket** (Conservative / Moderate / Aggressive)
- Optionally trains a lightweight ML classifier on synthetic data (so you can demo *Decision Trees / Model Selection* ideas)
- Exposes a **FastAPI** service with Swagger UI

> **No external API keys required.** The project runs offline using the included sample price data.  
> You can replace the sample CSVs with your own historical prices.
---

## Quick Start (VS Code)

### 1) Create & activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the API
```bash
uvicorn app.main:app --reload
```

Open:
- Swagger UI: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health

---


### Analyze the included sample portfolio
```bash
python -m src.cli analyze --portfolio data/sample_portfolio.json --prices_dir data/prices
```

### Call the API
```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -H "Content-Type: application/json" \
  -d @data/sample_request.json
```

---

## Input Formats

### Portfolio file (`data/sample_portfolio.json`)
```json
{
  "as_of": "2026-02-21",
  "base_currency": "USD",
  "benchmark": "SPY",
  "holdings": [
    {"ticker": "AAPL", "weight": 0.35},
    {"ticker": "MSFT", "weight": 0.35},
    {"ticker": "TLT",  "weight": 0.30}
  ]
}
```

### Price CSVs (`data/prices/<TICKER>.csv`)
Each CSV must have columns:
- `date` (YYYY-MM-DD)
- `close` (float)

Example:
```csv
date,close
2025-01-02,192.53
2025-01-03,191.15
...
```

---

## Docker (optional)
```bash
docker build -t portfolio-risk-analyzer .
docker run -p 8000:8000 portfolio-risk-analyzer
```

---

## Project Structure
```
portfolio-risk-analyzer/
  app/                # FastAPI service
  src/                # Core logic (metrics, scoring, optional ML)
  data/               # Sample portfolio + sample prices
  tests/              # Basic unit tests
```

---
