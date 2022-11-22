import streamlit as st
import matplotlib.pyplot as plt

st.session_state['df'] = df

st.header('Plot of Data')

fig, ax = plt.subplots(1,1)
ax.scatter(x=df['age'], y=df['satisfaction_rating'])
ax.set_xlabel('Age')
ax.set_ylabel('Satisfaction Rating')
    
st.pyplot(fig)