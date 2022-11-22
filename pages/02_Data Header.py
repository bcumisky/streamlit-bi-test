import streamlit as st
import pandas as pd

dummy_data = 'https://raw.githubusercontent.com/bcumisky/temp_data/main/EOC.csv'
df = pd.read_csv(dummy_data)

st.header('Header of Dataframe')
st.write(df.head())