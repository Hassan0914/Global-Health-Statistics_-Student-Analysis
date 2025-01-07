import streamlit as st
import homepagestreamlit
import charts
import pandas as pd
import matplotlib.pyplot as plt
import mlmodels_file as modls
from sklearn.linear_model import LinearRegression
import mlmodels_file as modls

df = pd.read_csv("Global Health Statistics.csv")
# """
# 'Country', 'Year', 'Disease Name', 'Disease Category',
#        'Prevalence Rate (%)', 'Incidence Rate (%)', 'Mortality Rate (%)',
#        'Age Group', 'Gender', 'Population Affected', 'Healthcare Access (%)',
#        'Doctors per 1000', 'Hospital Beds per 1000', 'Treatment Type',
#        'Average Treatment Cost (USD)', 'Availability of Vaccines/Treatment',
#        'Recovery Rate (%)', 'DALYs', 'Improvement in 5 Years (%)'
# """
page = st.sidebar.selectbox("Choose a page", ["Home", "Page 1", "Page 2", "Page 3"])
st.title("Global Health Statistics")
if page == "Home":
    homepagestreamlit.homepage()
elif page == "Page 1":
    import pages.page_1
elif page == "Page 2":
    import pages.page_2
elif page == "Page 3":
    import pages.page_3

chart_option = st.selectbox("Select a chart to display:", [
    "Bar Chart: Population Affected",
    "Box Plot: Treatment Cost",
    "Histogram: Mortality Rate",
    "Scater: population_vs_recovery",
    "line: healthcare_access",
    "heatmap: correlation",
    "stacked_bar: gender_population",
    "violin_plot: dalys",
    "bubble_chart: hospital_beds_vs_healthcare"
    ""
])

if chart_option == "Bar Chart: Population Affected":
    st.pyplot(charts.bar_chart_population_affected(df))
elif chart_option == "Box Plot: Treatment Cost":
    st.pyplot(charts.box_plot_treatment_cost(df))
elif chart_option == "Histogram: Mortality Rate":
    st.pyplot(charts.histogram_mortality_rate(df))
elif chart_option == "Scater: population_vs_recovery":
    st.pyplot(charts.scatter_population_vs_recovery(df))
elif chart_option == "line: healthcare_access":
    st.pyplot(charts.line_chart_healthcare_access(df))
elif chart_option == "heatmap: correlation":
    st.pyplot(charts.heatmap_correlation(df))
elif chart_option == "stacked_bar: gender_population":
    st.pyplot(charts.stacked_bar_gender_population(df))
elif chart_option == "violin_plot: dalys":
    st.pyplot(charts.violin_plot_dalys(df))
elif chart_option == "bubble_chart: hospital_beds_vs_healthcare":
    st.pyplot(charts.bubble_chart_hospital_beds_vs_healthcare(df))

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
#Apply ML Models
file_path = "Global Health Statistics.csv"
df = pd.read_csv(file_path)

available_columns = df.select_dtypes(include=['number']).columns.tolist()
total_features = st.number_input("Total Features:", min_value=1, max_value=len(available_columns), step=1, value=2)

features = st.multiselect(
    "Select Features:",
    available_columns,
    default=available_columns[:total_features] 
)

target = st.selectbox("Select Target Feature:", available_columns)

if len(features) > 0 and target:
    X_train, X_test, y_train, y_test = modls.preprocess_data(file_path, features, target)
    X_train_scaled, X_test_scaled = modls.scale_features(X_train, X_test)

    model_to_apply = LinearRegression()
    model = modls.train_model(model_to_apply, X_train_scaled, y_train)
    metrics = modls.evaluate_model(model, X_test_scaled, y_test)

    st.write("Model Evaluation Metrics:")
    st.write(metrics)

    st.write("Make a Prediction:")
    input_values = [st.number_input(f"Enter value for {feature}:", value=0.0) for feature in features]
    if st.button("Predict"):
        prediction = model.predict([input_values])
        st.write(f"Prediction: {prediction[0]}")
else:
    st.write("Please select features and target.")







"""
python -m streamlit run "d:/Semester 5/Intro to Data Science/IDS Project/streamlitt.py"

"""

