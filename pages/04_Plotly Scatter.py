import streamlit as st
import plotly_express as px

df = st.session_state['df']

col1, col2 = st.columns(2)

x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns) 
chart_color = st.color_picker('Select a plot color')
  
plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
plot.update_traces(marker=dict(color=chart_color))
st.plotly_chart(plot, use_container_width=True)