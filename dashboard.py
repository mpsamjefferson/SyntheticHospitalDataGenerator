
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hospital Data Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Synthetic Hospital Data Dashboard")
st.write("Explore fictional hospital patient records and statistics.")

# Load the generated patient data
df = pd.read_csv("hospital_patients.csv")

# Sidebar filters
st.sidebar.header("Filter Patients")

departments = st.sidebar.multiselect(
    "Select Department",
    options=sorted(df["Department"].unique()),
    default=sorted(df["Department"].unique())
)

filtered_df = df[df["Department"].isin(departments)]

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(filtered_df))

if len(filtered_df) > 0:
    col2.metric(
        "Average Patient Age",
        f"{filtered_df['Age'].mean():.1f} years"
    )

    col3.metric(
        "Total Billing",
        f"{filtered_df['Billing_Amount'].sum():,.2f}"
    )
else:
    col2.metric("Average Patient Age", "N/A")
    col3.metric("Total Billing", "0.00")

# Department chart
st.subheader("Patients by Department")

if not filtered_df.empty:
    counts = filtered_df["Department"].value_counts()

    fig, ax = plt.subplots(figsize=(9, 4))
    counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Department")
    ax.set_ylabel("Number of Patients")
    ax.tick_params(axis="x", rotation=20)

    st.pyplot(fig)
    plt.close(fig)

# Patient records table
st.subheader("Patient Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# Download filtered data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Patient Data as CSV",
    data=csv_data,
    file_name="filtered_hospital_patients.csv",
    mime="text/csv"
)
