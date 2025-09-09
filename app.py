import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.data.worldbank import fetch_indicator

st.set_page_config(page_title="Macro Turkey Dashboard", layout="wide")
st.title("Macro Turkey Dashboard")

with open('src/data/indicators.json', 'r', encoding='utf-8') as f:
    IND = json.load(f)["TUR"]

choices = {
    "CPI inflation (annual %)": IND["CPI_inflation_annual_percent"],
    "GDP growth (annual %)": IND["GDP_growth_annual_percent"],
    "Unemployment (%)": IND["Unemployment_total_percent"],
    "Current account (% of GDP)": IND["Current_account_balance_percent_GDP"],
    "Current account (USD bn)": IND["Current_account_balance_USD"]
}

opt = st.selectbox("Indicator", list(choices.keys()))
code = choices[opt]

df = fetch_indicator('TUR', code).copy()
if "USD bn" in opt:
    df["value"] = df["value"] / 1e9

st.write(f"World Bank indicator code: `{code}`")
fig, ax = plt.subplots()
ax.plot(df["date"], df["value"])
ax.set_title(opt)
ax.set_xlabel("Year")
ax.grid(True)
st.pyplot(fig)