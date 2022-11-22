import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dummy_data = 'https://raw.githubusercontent.com/bcumisky/temp_data/main/EOC.csv'
df = pd.read_csv(dummy_data)

st.header('Plot of Data')

fig, ax = plt.subplots(1,1)
ax.scatter(x=df['age'], y=df['satisfaction_rating'])
ax.set_xlabel('Age')
ax.set_ylabel('Satisfaction Rating')
    
st.pyplot(fig)