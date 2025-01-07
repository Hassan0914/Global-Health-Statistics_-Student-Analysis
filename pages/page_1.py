
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Project Analysis")

plt.figure(figsize=(12,8))

df = pd.read_csv('Global Health Statistics.csv')
df['Population Affected'] = pd.to_numeric(df['Population Affected'], errors='coerce')
# Total population affected by the disease of Malaria
filtered_data = df[df['Disease Name'].str.contains('Malaria', case=False, na=False)]
total_population_affected = filtered_data['Population Affected'].sum()

aggregated_data = df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
most_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmax()]
least_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmin()]

st.write("aggregated Data")
st.write(aggregated_data)
st.write("Most Common Diseae")
st.write(most_common_disease)

st.write("Least Common Disease")
st.write(least_common_disease)

head = df.head(10)
st.write("First 10 rows")
st.write(head)


info = df.info()
st.write("Info")
st.write(info)

description = df.describe()
st.write("Description")
st.write(description)

country_counts = df['Country'].count()
st.write("Country Counts")
st.write(country_counts)

nuique = df.nunique()
st.write("Uniques Value of all columns")
st.write(nuique)

unique_countries =df['Country'].nunique()
st.write("Unique Countries")
st.write(unique_countries)

country_counts = df['Country'].value_counts()
st.write("Country Counts")
st.write(country_counts)


mortality_rate = df['Mortality Rate (%)'].describe()
st.write("Mortality Rate")
st.write(mortality_rate)

age_groups = df['Age Group'].unique()
st.write("Age Groups")
st.write(age_groups)

disease_categories = df['Disease Category'].value_counts()
st.write("Disease Categories")
st.write(disease_categories)

disesees = df['Disease Name'].value_counts()
st.write("Disease Value Counts")
st.write(disesees)

healthcare_access = df['Healthcare Access (%)'].info()
st.write("Healthcare Access")
st.write(healthcare_access)
#print(df['Healthcare Access (%)'].describe())
#Country with the healthcare access below 70 and hospital beds below 6 in the Category of Respiratory and Disease of Diabetes
target_countries = df[(df['Healthcare Access (%)'] < 70) & (df['Hospital Beds per 1000']<6) & (df['Disease Name']=='Diabetes') & (df['Disease Category'] == 'Respiratory')]
#print(target_countries.head(10))

countries = df[(df['Healthcare Access (%)'] < 70) & (df['Hospital Beds per 1000']<5)]
prevalence_by_disease= countries.groupby('Disease Name')['Prevalence Rate (%)'].mean().sort_values(ascending=True)
disease_by_age = countries.groupby('Disease Category')['Age Group'].value_counts()


#Country with the per capita income > 25000$ after 2020 and Education  Index > 0.70
country = df[(df['Per Capita Income (USD)'] > 55000) & (df['Year'] > 2020) & (df['Average Treatment Cost (USD)']<300)]

correelation_matrix = df[['Average Treatment Cost (USD)','Per Capita Income (USD)','Prevalence Rate (%)','Urbanization Rate (%)']].corr()
st.write("Correlation Matrix")
st.write(correelation_matrix)
#print(correelation_matrix['Urbanization Rate (%)'])

#Graph1

# aggregated_data = df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
# plt.bar(x=aggregated_data["Disease Name"],height=aggregated_data["Population Affected"],color="r",align="edge",width=0.5,edgecolor="green")
# plt.xlabel("Disease Name")
# plt.ylabel("Population Affected")
# plt.title("Disease and Population Ratio")
# plt.xticks(rotation=45,ha='right')
# plt.ylim(0,2)
# plt.tight_layout()
# plt.show()






