# Macro Turkey Dashboard

This project collects and visualizes basic macroeconomic indicators for Turkey using data from the World Bank API.  
The goal is to keep a clean, reproducible workflow for small economics/finance projects.

## Contents
- `notebooks/01_Turkey_Macro_Basics.ipynb` → CPI inflation and GDP growth charts
- `src/data/worldbank.py` → small helper to fetch data from the World Bank
- `requirements.txt` → Python dependencies

## How to run
1. Create a virtual environment:
   ```bash
   python -m venv .venv && source .venv/bin/activate
2. Install dependencies:
pip install
-r requirements.txt

3. Open Jupyter and run the notebook:
4. jupyter lab
