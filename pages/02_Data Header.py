import streamlit as st
import pandas as pd

df = st.session_state['df']

st.header('Header of Dataframe')
st.write(df.head())