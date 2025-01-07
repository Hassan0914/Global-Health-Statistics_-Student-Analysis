
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,8))

df = pd.read_csv('Global Health Statistics.csv')
df['Population Affected'] = pd.to_numeric(df['Population Affected'], errors='coerce')
# Total population affected by the disease of Malaria
filtered_data = df[df['Disease Name'].str.contains('Malaria', case=False, na=False)]
total_population_affected = filtered_data['Population Affected'].sum()
print(f"Total population affected by Malaria: {total_population_affected:,}")

aggregated_data = df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
most_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmax()]
least_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmin()]

print("Most Common Disease: ", most_common_disease)
print("Least Common Disease: ", least_common_disease)

head = df.head()

info = df.info()

description = df.describe()

country_counts = df['Country'].count()
#print("Total countries in the dataset: ")

nuique = df.nunique()

unique_countries =df['Country'].nunique()

#print("Total no of countries: ",unique_countries)

country_counts = df['Country'].value_counts()

#print("Country counts",country_counts)

mortality_rate = df['Mortality Rate (%)'].describe()

#print("Mortality Rate: ",mortality_rate)

age_groups = df['Age Group'].unique()

#print("Age Groups: ",age_groups)

disease_categories = df['Disease Category'].value_counts()
#print("Disese Categories: ",disease_categories)

#print(df['Disease Name'].nunique())
disesees = df['Disease Name'].value_counts()

healthcare_access = df['Healthcare Access (%)'].info()
#print(df['Healthcare Access (%)'].describe())
#Country with the healthcare access below 70 and hospital beds below 6 in the Category of Respiratory and Disease of Diabetes
target_countries = df[(df['Healthcare Access (%)'] < 70) & (df['Hospital Beds per 1000']<6) & (df['Disease Name']=='Diabetes') & (df['Disease Category'] == 'Respiratory')]
#print(target_countries.head(10))

countries = df[(df['Healthcare Access (%)'] < 70) & (df['Hospital Beds per 1000']<5)]
prevalence_by_disease= countries.groupby('Disease Name')['Prevalence Rate (%)'].mean().sort_values(ascending=True)
disease_by_age = countries.groupby('Disease Category')['Age Group'].value_counts()


#Country with the per capita income > 25000$ after 2020 and Education  Index > 0.70
country = df[(df['Per Capita Income (USD)'] > 55000) & (df['Year'] > 2020) & (df['Average Treatment Cost (USD)']<300)]

correelation_matrix = df[['Average Treatment Cost (USD)','Per Capita Income (USD)','Prevalence Rate (%)','Urbanization Rate (%)','Urbanization Rate (%)']].corr()
#print(correelation_matrix['Urbanization Rate (%)'])

#Graph1

aggregated_data = df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
plt.bar(x=aggregated_data["Disease Name"],height=aggregated_data["Population Affected"],color="r",align="edge",width=0.5,edgecolor="green")
plt.xlabel("Disease Name")
plt.ylabel("Population Affected")
plt.title("Disease and Population Ratio")
plt.xticks(rotation=45,ha='right')
plt.ylim(0,2)
plt.tight_layout()
plt.show()






