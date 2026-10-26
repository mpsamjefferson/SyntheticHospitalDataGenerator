
import pandas as pd

df = pd.read_csv("hospital_patients.csv")

allowed_departments = {
    "Cardiology",
    "General Medicine",
    "Neurology",
    "Orthopedics",
    "Pediatrics"
}

allowed_diagnoses = {
    "Common Cold",
    "Diabetes",
    "Fracture",
    "Hypertension",
    "Migraine"
}

required_columns = [
    "Patient_ID",
    "Age",
    "Gender",
    "Department",
    "Diagnosis",
    "Admission_Date",
    "Length_of_Stay",
    "Billing_Amount"
]

print("=== DETAILED DATA VALIDATION ===")

# 1. Check required columns
missing_columns = set(required_columns) - set(df.columns)
print("Missing required columns:", sorted(missing_columns))

# 2. Check missing values
print("Missing values:", df[required_columns].isnull().sum().sum()
      if not missing_columns else "Check required columns first")

# 3. Check duplicate IDs
print("Duplicate patient IDs:", df["Patient_ID"].duplicated().sum())

# 4. Check numeric values
age = pd.to_numeric(df["Age"], errors="coerce")
stay = pd.to_numeric(df["Length_of_Stay"], errors="coerce")
billing = pd.to_numeric(df["Billing_Amount"], errors="coerce")

print("Invalid ages:", (age.isna() | (age < 0) | (age > 120)).sum())
print("Invalid length of stay:",
      (stay.isna() | (stay < 1) | (stay % 1 != 0)).sum())
print("Invalid billing amounts:",
      (billing.isna() | (billing < 0)).sum())

# 5. Check admission dates
dates = pd.to_datetime(df["Admission_Date"], errors="coerce")
print("Invalid admission dates:", dates.isna().sum())

# 6. Check categories
print("Unapproved departments:",
      sorted(set(df["Department"].dropna()) - allowed_departments))

print("Undocumented diagnoses:",
      sorted(set(df["Diagnosis"].dropna()) - allowed_diagnoses))

print("Unexpected gender labels:",
      sorted(set(df["Gender"].dropna()) - {"Male", "Female"}))

# 7. Show combinations for review
print("\n=== DEPARTMENT AND DIAGNOSIS COMBINATIONS ===")
print(df.groupby(["Department", "Diagnosis"]).size().to_string())

print("\nValidation finished. Review any non-zero error counts.")
