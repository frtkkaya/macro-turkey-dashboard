# Macro Turkey Dashboard (starter)

A minimal, clean starter repo to analyze Turkey's macro data (inflation, GDP growth) with Python and Jupyter.

## What this repo shows recruiters
- Structured project (notebooks + src + docs)
- Clean README and requirements
- Simple, readable plots
- Reproducible steps

## Quickstart
1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. **Install packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Open Jupyter and run the notebook**:
   ```bash
   jupyter lab  # or: jupyter notebook
   ```
4. Run `notebooks/01_Turkey_Macro_Basics.ipynb` end-to-end.

## Data Sources (no API keys required in starter)
- **World Bank API** (JSON): CPI inflation (annual %) and GDP growth (annual %).

> Tip: Later, expand with **TCMB EVDS** (needs API key) and **FRED** (needs API key).

## Repo structure
```
macro-turkey-dashboard/
├─ notebooks/
│  └─ 01_Turkey_Macro_Basics.ipynb
├─ src/
│  └─ data/
│     └─ worldbank.py
├─ .gitignore
├─ LICENSE
├─ README.md
└─ requirements.txt
```

## Next ideas
- Add policy rate, FX, unemployment, current account.
- Create a simple `app.py` to display plots with Streamlit.
- Write a short LinkedIn post linking to this repo.