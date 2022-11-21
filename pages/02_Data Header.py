import streamlit as st

df = st.session_state['df']
st.header('Header of Dataframe')
st.write(df.head())