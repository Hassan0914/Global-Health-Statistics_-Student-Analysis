import matplotlib.pyplot as plt
import seaborn as sns

#Chart1
import matplotlib.pyplot as plt

def bar_chart_population_affected(df):
    aggregated_data = df.groupby('Disease Name')['Population Affected'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    aggregated_data.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
    ax.set_title("Total Population Affected by Each Disease")
    ax.set_xlabel("Disease Name")
    ax.set_ylabel("Population Affected")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    return fig


#Chart2
def box_plot_treatment_cost(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x='Disease Category', y='Average Treatment Cost (USD)', data=df, palette='Set2', ax=ax)
    ax.set_title("Comparison of Treatment Costs by Disease Category")
    ax.set_xlabel("Disease Category")
    ax.set_ylabel("Average Treatment Cost (USD)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    return fig



#Chart3
def histogram_mortality_rate(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Mortality Rate (%)'], bins=20, color='orange', edgecolor='black', alpha=0.7)
    ax.set_title("Distribution of Mortality Rate")
    ax.set_xlabel("Mortality Rate (%)")
    ax.set_ylabel("Frequency")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return fig


#Chart4
def scatter_population_vs_recovery(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Population Affected'], df['Recovery Rate (%)'], alpha=0.7, c='blue', edgecolors='black')
    ax.set_title("Population Affected vs Recovery Rate")
    ax.set_xlabel("Population Affected")
    ax.set_ylabel("Recovery Rate (%)")
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig


#Chart5
def line_chart_healthcare_access(df):
    aggregated_year_data = df.groupby('Year')['Healthcare Access (%)'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(aggregated_year_data.index, aggregated_year_data.values, marker='o', color='green', linestyle='-', linewidth=2)
    ax.set_title("Healthcare Access Over the Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Healthcare Access (%)")
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig


#Chart6
def heatmap_correlation(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = df[numerical_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap")
    plt.tight_layout()
    return fig


#Chart7
def stacked_bar_gender_population(df):
    gender_data = df.groupby(['Disease Category', 'Gender'])['Population Affected'].sum().unstack()
    fig, ax = plt.subplots(figsize=(12, 6))
    gender_data.plot(kind='bar', stacked=True, ax=ax, color=['blue', 'pink'])
    ax.set_title("Gender-wise Population Affected by Disease Category")
    ax.set_xlabel("Disease Category")
    ax.set_ylabel("Population Affected")
    ax.legend(title="Gender")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    return fig


#Chart8
def violin_plot_dalys(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.violinplot(x='Disease Category', y='DALYs', data=df, palette='muted', ax=ax)
    ax.set_title("Distribution of DALYs by Disease Category")
    ax.set_xlabel("Disease Category")
    ax.set_ylabel("DALYs")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    return fig


#Chart9
def bubble_chart_hospital_beds_vs_healthcare(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    scatter = ax.scatter(
        df['Hospital Beds per 1000'], 
        df['Healthcare Access (%)'], 
        s=df['Population Affected'] / 1000,  # Scale bubble size
        alpha=0.5, c=df['Mortality Rate (%)'], cmap='coolwarm', edgecolor='black'
    )
    ax.set_title("Hospital Beds vs Healthcare Access")
    ax.set_xlabel("Hospital Beds per 1000")
    ax.set_ylabel("Healthcare Access (%)")
    fig.colorbar(scatter, label="Mortality Rate (%)")
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig











