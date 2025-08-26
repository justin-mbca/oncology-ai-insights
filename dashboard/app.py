import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Oncology AI Insights Dashboard", layout="wide")
st.title("Oncology AI Insights Dashboard")

st.markdown("""
This dashboard visualizes synthetic oncology patient data and demonstrates how AI can support clinical insights.
""")

@st.cache_data
def load_data():
    return pd.read_csv("../data/synthetic_oncology_patients.csv")

df = load_data()

# Sidebar filters
cancer_types = df['cancer_type'].unique().tolist()
st.sidebar.header("Filter Data")
selected_cancer = st.sidebar.multiselect("Cancer Type", cancer_types, default=cancer_types)

filtered_df = df[df['cancer_type'].isin(selected_cancer)]

# Main dashboard
st.subheader("Patient Demographics")
st.dataframe(filtered_df[['patient_id', 'age', 'gender', 'cancer_type', 'stage']])

st.subheader("Cancer Type Distribution")
fig1 = px.histogram(filtered_df, x="cancer_type", color="gender", barmode="group", title="Cancer Type by Gender")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Biomarker Status vs. Treatment")
fig2 = px.histogram(filtered_df, x="biomarker_status", color="treatment", barmode="group", title="Biomarker Status by Treatment")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Survival Time Distribution")
fig3 = px.histogram(filtered_df, x="survival_months", nbins=8, title="Distribution of Survival Time")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.markdown("*Demo only. No real patient data is used.*")
