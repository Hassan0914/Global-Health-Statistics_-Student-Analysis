from disease_data import Data
import charts

import numpy as np 
import pandas as pd 


df = pd.read_csv('Global Health Statistics.csv')

"""
'Country', 'Year', 'Disease Name', 'Disease Category',
       'Prevalence Rate (%)', 'Incidence Rate (%)', 'Mortality Rate (%)',
       'Age Group', 'Gender', 'Population Affected', 'Healthcare Access (%)',
       'Doctors per 1000', 'Hospital Beds per 1000', 'Treatment Type',
       'Average Treatment Cost (USD)', 'Availability of Vaccines/Treatment',
       'Recovery Rate (%)', 'DALYs', 'Improvement in 5 Years (%)'
"""

data = Data(df)

toatal = data.total_population_affected_by_malaria()
correlation_matrix = data.correlation_matrix(['Prevalence Rate (%)', 'Incidence Rate (%)'])
#print(toatal)
#print(correlation_matrix)

##Make Charts
#charts.bar_chart_population_affected(df)
charts.line_chart_healthcare_access(df)
charts.bubble_chart_hospital_beds_vs_healthcare(df)

