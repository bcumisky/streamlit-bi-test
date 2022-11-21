import streamlit as st

df = st.session_state['df']
st.header('Statistics of Dataframe')
st.write(df.describe())