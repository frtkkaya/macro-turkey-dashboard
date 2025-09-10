# src/data/worldbank.py
from __future__ import annotations
import json
from typing import List, Dict
import pandas as pd
import requests

WB_API = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=20000"

class WorldBankError(RuntimeError):
    pass

def fetch_indicator(country: str, indicator: str) -> pd.DataFrame:
    """World Bank'ten tek bir göstergeyi (TR, SP.POP.TOTL vb.) çeker.
    DataFrame: columns=['date','value','indicator','country'] (yıllık, string yıl → int)."""
    url = WB_API.format(country=country, indicator=indicator)
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        raise WorldBankError(f"HTTP {r.status_code}: {url}")

    payload = r.json()
    if not isinstance(payload, list) or len(payload) < 2:
        raise WorldBankError(f"Beklenmeyen yanıt: {json.dumps(payload)[:200]}")

    data = payload[1] or []
    df = pd.DataFrame(data)[["date", "value"]].copy()
    df["date"] = pd.to_numeric(df["date"], errors="coerce").astype("Int64")
    df["indicator"] = indicator
    df["country"] = country.upper()
    return df.dropna(subset=["date"]).sort_values("date")

def fetch_many(country: str, indicators: List[str]) -> pd.DataFrame:
    """Birden fazla göstergeyi uzun formda birleştirir."""
    frames = [fetch_indicator(country, ind) for ind in indicators]
    return pd.concat(frames, ignore_index=True)

def wide_pivot(df_long: pd.DataFrame) -> pd.DataFrame:
    """Uzun veriyi (date, indicator, value) → geniş tablo (date satır, kolon=indicator)."""
    out = df_long.pivot_table(index="date", columns="indicator", values="value")
    return out.sort_index()

# Örnek çağrı:
# df = fetch_many("TUR", ["FP.CPI.TOTL.ZG", "NY.GDP.MKTP.KD.ZG"])
# wide = wide_pivot(df)
Update worldbank.py with robust fetch functions
