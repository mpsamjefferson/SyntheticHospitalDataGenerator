\# Data Dictionary

\## Synthetic Hospital Data Generator



This document describes the columns in the `hospital\_patients.csv` dataset.



| Column Name | Data Type | Description | Example |

|---|---|---|---|

| Patient\_ID | String | Unique identifier assigned to each synthetic patient | P0001 |

| Age | Integer | Age of the fictional patient in years | 35 |

| Gender | String | Gender category assigned to the fictional patient | Male |

| Department | String | Hospital department associated with the patient | Cardiology |

| Diagnosis | String | Simulated diagnosis recorded for the patient | Hypertension |

| Admission\_Date | Date | Date of the simulated hospital admission | 2026-01-15 |

| Length\_of\_Stay | Integer | Number of days in the simulated hospital stay | 5 |

| Billing\_Amount | Decimal | Simulated billing amount for the hospital stay | 25000.50 |



\## Data Quality Rules



1\. Patient\_ID should be unique for each patient record.

2\. Age should be within the configured valid age range.

3\. Gender should use the categories defined in the data generator.

4\. Department should match an approved department name.

5\. Diagnosis should match a diagnosis defined in the generator.

6\. Admission\_Date should be stored in a consistent date format.

7\. Length\_of\_Stay should be a positive whole number.

8\. Billing\_Amount should not be negative.

9\. Required fields should not contain missing values.



\## Important Note



All patient records are synthetically generated for educational and software-development purposes. They do not represent real patients or actual hospital records.

