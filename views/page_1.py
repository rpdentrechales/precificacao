import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Sample Page 1", page_icon="💎",layout="wide")

@st.cache_data
def load_dataframe(worksheet):

  conn = st.connection("gsheets", type=GSheetsConnection)
  df = conn.read(worksheet=worksheet)

  return df


  conn = st.connection("gsheets", type=GSheetsConnection)
  df = conn.read(worksheet=worksheet)
  df = df.drop_duplicates(subset=duplicates_subset)

  return df

st.title("Meu novo dataframe")

df = load_dataframe("BI")

st.dataframe(df)
