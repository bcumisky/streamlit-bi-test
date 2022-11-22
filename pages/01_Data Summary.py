import streamlit as st

st.session_state['df'] = df

st.header('Statistics of Dataframe')
st.write(df.describe())