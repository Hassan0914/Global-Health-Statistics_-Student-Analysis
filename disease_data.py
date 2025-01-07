class Data:

    def __init__(self,df):
        self.df = df

    def total_population_affected_by_malaria(self):
        filtered_data = self.df[self.df['Disease Name'].str.contains('Malaria', case=False, na=False)]
        total_population_affected = filtered_data['Population Affected'].sum()
        return total_population_affected

    def most_common_disease(self):
        aggregated_data = self.df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
        most_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmax()]
        return most_common_disease
        

    def least_common_disease(self):
        aggregated_data = self.df.groupby('Disease Name', as_index=False)['Population Affected'].sum()
        least_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmin()]
        return least_common_disease

    def head_info_description(self):
        head = self.df.head()
        info = self.df.info()
        description = self.df.describe()
        return head,info,description

    def total_countries(self):
        unique_countries =self.df['Country'].nunique()
        return unique_countries
    def country_counts(self):
        country_counts = self.df['Country'].value_counts()
        return country_counts
    def mortality_rate(self):
        mortality_rate = self.df['Mortality Rate (%)'].describe()
        return mortality_rate
    def age_groups(self):
        age_groups = self.df['Age Group'].unique()
        return age_groups
    def disease_categories_counts(self):
        disease_categories = self.df['Disease Category'].value_counts()
        return disease_categories
    def healthcare_access_info(self):
        healthcare_access = self.df['Healthcare Access (%)'].info()
        return healthcare_access
    def target_countries(self,healthcare_access,hospitals_beds_per_1000,disease_name,disease_category):
        target_countries = self.df[(self.df['Healthcare Access (%)'] < healthcare_access) & (self.df['Hospital Beds per 1000']<hospitals_beds_per_1000) & (self.df['Disease Name']==disease_name) & (df['Disease Category'] == disease_category)]
        return target_countries
    def disease_by_age(self):
        disease_by_age = self.df.groupby('Disease Category')['Age Group'].value_counts()
        return disease_by_age
    def correlation_matrix(self,data):
        correelation_matrix = self.df[data].corr()
        return correelation_matrix

        


