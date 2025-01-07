import streamlit as st
from disease_data import Data
import charts
import pandas as pd
def homepage():
    df = pd.read_csv('Global Health Statistics.csv')
    st.write(df)
    
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    chart1 = charts.bar_chart_population_affected(df)
    st.pyplot(chart1)
    
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
  
  
