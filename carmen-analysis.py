import pandas as pd
import json

# Load the dataset
df = pd.read_csv("insurance.csv")

# Regional breakdown
region_counts = df['region'].value_counts()
print("🔍 Breakdown of patients by region:")
print(region_counts)

# Smoker vs. non-smoker costs
smoker_costs = df.groupby('smoker')['charges'].mean()
print("\n💸 Average insurance charges for smokers vs. non-smokers:")
print(smoker_costs)

# Correlation: BMI vs. charges
bmi_corr = df['bmi'].corr(df['charges'])
print(f"\n📊 Correlation between BMI and insurance charges: {bmi_corr:.4f}")

#

