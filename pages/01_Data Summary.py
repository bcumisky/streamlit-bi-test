import streamlit as st

df = pd.read_csv(dummy_data)

st.header('Statistics of Dataframe')
st.write(df.describe())