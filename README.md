# Macro Turkey Dashboard

This project collects and visualizes basic macroeconomic indicators for Turkey using the World Bank API.  
The goal is a clean, reproducible workflow for small economics/finance projects.

## Contents
- `notebooks/01_Turkey_Macro_Basics.ipynb` — CPI inflation and GDP growth charts
- `notebooks/02_Turkey_Unemployment.ipynb` — unemployment and GDP overlay
- `notebooks/03_Turkey_Current_Account.ipynb` — current account (USD & % of GDP)
- `src/data/worldbank.py` — helper to fetch indicators
- `src/data/indicators.json` — list of codes used
- `app.py` — simple Streamlit app to browse indicators

## How to run
1. Create a virtual environment:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jupyter:
   ```bash
   jupyter lab
   ```
4. Streamlit (optional):
   ```bash
   pip install -r requirements-extra.txt
   streamlit run app.py
   ```

## Notes
- Data is fetched on the fly from the World Bank API (no keys needed).
- For policy rate and higher-frequency series, you can later add TCMB EVDS or FRED.
