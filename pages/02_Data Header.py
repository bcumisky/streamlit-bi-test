import streamlit as st

st.session_state['df'] = df

st.header('Header of Dataframe')
st.write(df.head())