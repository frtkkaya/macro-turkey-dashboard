# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from src.data.worldbank import fetch_many, wide_pivot, WorldBankError

st.set_page_config(page_title="Macro Turkey Dashboard", layout="wide")

st.title("Macro Turkey Dashboard")
st.caption("World Bank API ile temel göstergeler • Country=TUR")

with st.sidebar:
    st.header("Ayarlar")
    indicators_default = [
        "FP.CPI.TOTL.ZG",     # CPI inflation, % (yıllık)
        "NY.GDP.MKTP.KD.ZG",  # Real GDP growth, %
        "SL.UEM.TOTL.ZS",     # Unemployment, %
        "NE.EXP.GNFS.ZS",     # Exports of goods/services, % of GDP
    ]
    indicators = st.tags_input(
        "World Bank Indicator Codes", value=indicators_default
    ) if hasattr(st, "tags_input") else indicators_default
    min_year, max_year = st.slider("Year range", 1980, 2025, (2000, 2025))

try:
    df_long = fetch_many("TUR", indicators)
    df_wide = wide_pivot(df_long)
    df_wide = df_wide.loc[(df_wide.index >= min_year) & (df_wide.index <= max_year)]

    st.subheader("Tablo (geniş format)")
    st.dataframe(df_wide.round(3))

    st.subheader("Grafikler")
    for col in df_wide.columns:
        fig = px.line(df_wide.reset_index(), x="date", y=col, markers=True, title=col)
        st.plotly_chart(fig, use_container_width=True)

except WorldBankError as e:
    st.error(f"World Bank hatası: {e}")
except Exception as e:
    st.exception(e)
