import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

st.session_state['df'] = df

col1, col2 = st.columns(2)

x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns) 
chart_color = st.color_picker('Select a plot color')
  
plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
plot.update_traces(marker=dict(color=chart_color))
st.plotly_chart(plot, use_container_width=True)


## Data
with st.spinner('Updating Report...'):
    
    #Metrics setting and rendering
    hosp_df = pd.read_excel('data/DataforMock.xlsx',sheet_name = 'Hospitals')
    hosp = st.selectbox('Choose Hospital', hosp_df, help = 'Filter report to show only one hospital')

    g1, g2, g3 = st.columns((1,1,1))
    
    # Patient Satisfaction by Patient Hospital
    fgdf = pd.read_excel('data/DataforMock.xlsx',sheet_name = 'Graph')
    
    fgdf = fgdf[fgdf['Hospital Attended']==hosp] 
    
    fig = px.bar(fgdf, x = 'Arrived Destination Resolved', y='Number of Handovers', template = 'seaborn')
    
    fig.update_traces(marker_color='#264653')
    
    fig.update_layout(title_text="Patient Satisfaction by Hospital",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    
    g1.plotly_chart(fig, use_container_width=True) 
    
    # Patient Satisfaction by Patient Type
    fcst = pd.read_excel('data/DataforMock.xlsx',sheet_name = 'Forecast')
    
    fcst = fcst[fcst['Hospital Attended']==hosp]
    
    fig = px.bar(fcst, x = 'Arrived Destination Resolved', y='y', template = 'seaborn')
    
    fig.update_traces(marker_color='#7A9E9F')
    
    fig.update_layout(title_text="Patient Satisfaction by Patient Type",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    
    g2.plotly_chart(fig, use_container_width=True)  
    
    # Patient Satisfaction by Service Line
    fig = px.bar(fgdf, x = 'Arrived Destination Resolved', y='Average Duration',color = "Average Duration", template = 'seaborn', color_continuous_scale=px.colors.diverging.Temps)
    
    fig.add_scatter(x=fgdf['Arrived Destination Resolved'], y=fgdf['Target'], mode='lines', line=dict(color="black"), name='Target')
    
    fig.update_layout(title_text="Patient Satisfaction by Service Line",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
    
    g3.plotly_chart(fig, use_container_width=True) 