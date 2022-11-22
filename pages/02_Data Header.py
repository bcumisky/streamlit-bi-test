import streamlit as st

df = pd.read_csv(dummy_data)

st.header('Header of Dataframe')
st.write(df.head())