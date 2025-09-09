"""
Lightweight World Bank API helper used in the starter notebook.
No API key required.

Usage:
    from src.data.worldbank import fetch_indicator
    df = fetch_indicator(country='TUR', indicator='FP.CPI.TOTL.ZG')  # CPI inflation (annual %)
"""

from typing import Dict
import requests
import pandas as pd


BASE_URL = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=2000"


def fetch_indicator(country: str, indicator: str) -> pd.DataFrame:
    """
    Fetch a single World Bank indicator for a country.
    Returns a DataFrame with ['date', 'value'] sorted ascending by date.
    """
    url = BASE_URL.format(country=country, indicator=indicator)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list) or len(data) < 2:
        raise RuntimeError("Unexpected World Bank response.")
    rows = data[1]
    df = pd.DataFrame([{"date": int(x["date"]), "value": x["value"]} for x in rows if x.get("date")])
    df = df.dropna().sort_values("date").reset_index(drop=True)
    return df
