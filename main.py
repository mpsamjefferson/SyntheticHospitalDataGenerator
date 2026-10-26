

import random
import pandas as pd
from datetime import date, timedelta

random.seed(42)

departments = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "General Medicine"
]

diagnoses = [
    "Hypertension",
    "Migraine",
    "Fracture",
    "Common Cold",
    "Diabetes"
]

patients = []

# Generate 100 fictional patient records
for i in range(1, 101):
    admission_date = date.today() - timedelta(
        days=random.randint(0, 365)
    )

    patient = {
        "Patient_ID": f"P{i:03d}",
        "Age": random.randint(1, 95),
        "Gender": random.choice(["Male", "Female"]),
        "Department": random.choice(departments),
        "Diagnosis": random.choice(diagnoses),
        "Admission_Date": admission_date.isoformat(),
        "Length_of_Stay": random.randint(1, 15),
        "Billing_Amount": round(
            random.uniform(500, 50000), 2
        )
    }

    patients.append(patient)

df = pd.DataFrame(patients)

# Save patient records
df.to_csv("hospital_patients.csv", index=False)

print("Synthetic hospital data generated successfully!")
print("Total patient records:", len(df))

# Validate the data
print("\n--- DATA VALIDATION ---")

print("Missing values:", df.isnull().sum().sum())
print("Duplicate patient IDs:", df["Patient_ID"].duplicated().sum())

print(
    "Invalid ages:",
    ((df["Age"] < 0) | (df["Age"] > 120)).sum()
)

print(
    "Invalid billing amounts:",
    (df["Billing_Amount"] < 0).sum()
)

# Analyze hospital data
print("\n--- HOSPITAL STATISTICS ---")

print("Average patient age:", round(df["Age"].mean(), 2))
print(
    "Average hospital stay:",
    round(df["Length_of_Stay"].mean(), 2),
    "days"
)

print(
    "Total billing amount:",
    round(df["Billing_Amount"].sum(), 2)
)

print(
    "Average billing amount:",
    round(df["Billing_Amount"].mean(), 2)
)

# Count patients in each department
department_summary = (
    df.groupby("Department")
    .agg(
        Patient_Count=("Patient_ID", "count"),
        Average_Stay=("Length_of_Stay", "mean"),
        Total_Billing=("Billing_Amount", "sum")
    )
    .round(2)
    .reset_index()
)

print("\n--- DEPARTMENT SUMMARY ---")
print(department_summary.to_string(index=False))

# Save department analysis
department_summary.to_csv(
    "hospital_department_summary.csv",
    index=False
)

print("\nFiles saved successfully:")
print("1. hospital_patients.csv")
print("2. hospital_department_summary.csv")




import matplotlib.pyplot as plt

# Chart 1: Number of patients in each department
plt.figure(figsize=(10, 5))

plt.bar(
    department_summary["Department"],
    department_summary["Patient_Count"]
)

plt.title("Number of Patients by Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("patients_by_department.png")
plt.show()

# Chart 2: Total billing by department
plt.figure(figsize=(10, 5))

plt.bar(
    department_summary["Department"],
    department_summary["Total_Billing"]
)

plt.title("Total Billing by Department")
plt.xlabel("Department")
plt.ylabel("Total Billing Amount")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("billing_by_department.png")
plt.show()

print("Hospital charts generated successfully!")
print("1. patients_by_department.png")
print("2. billing_by_department.png")

