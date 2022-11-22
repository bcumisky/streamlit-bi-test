#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

st.set_page_config(layout="wide")

# Functions for each of the pages
def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['age'], y=df['satisfaction_rating'])
    ax.set_xlabel('Age')
    ax.set_ylabel('Satisfaction Rating')
    
    st.pyplot(fig)

def interactive_plot():
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns) 
    chart_color = st.color_picker('Select a plot color')
  
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=chart_color))
    st.plotly_chart(plot, use_container_width=True)

# Add a title and intro text
st.title('Episode of Care Data Explorer')
st.text('This is a web app to allow exploration of PX Data')

# Sidebar setup
st.sidebar.title('Sidebar')
dummy_data = 'https://raw.githubusercontent.com/bcumisky/temp_data/main/EOC.csv'

st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Data Summary', 'Data Header', 'Scatter Plot', 'Interactive Plot'])

df = pd.read_csv(dummy_data)
st.session_state['df'] = df

# Navigation options
if options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()
elif options == 'Interactive Plot':
    interactive_plot()