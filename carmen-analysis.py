import pandas as pd
import json

=======
# Load the dataset
>>>>>>> anisha-analysis
df = pd.read_csv("insurance.csv")

# Regional breakdown
region_counts = df['region'].value_counts()
print("🔍 Breakdown of patients by region:")
print(region_counts)

# Smoker vs. non-smoker costs
smoker_costs = df.groupby('smoker')['charges'].mean()
print("\n💸 Average insurance charges for smokers vs. non-smokers:")
print(smoker_costs)


# Correlations
bmi_corr = df['bmi'].corr(df['charges'])
children_corr = df['children'].corr(df['charges'])
print(f"\n📊 Correlation between BMI and charges: {bmi_corr:.2f}")
print(f"📊 Correlation between children and charges: {children_corr:.2f}")

# Save to JSON
results = {
    "region_counts": region_counts.to_dict(),
    "smoker_costs": smoker_costs.to_dict(),
    "bmi_charges_correlation": round(bmi_corr, 2),
    "children_charges_correlation": round(children_corr, 2)
}

# Ensure results folder exists
import os
os.makedirs("results", exist_ok=True)

with open("results/carmen_results.json", "w") as file:
    json.dump(results, file, indent=2)
=======
# Correlation: BMI vs. charges
bmi_corr = df['bmi'].corr(df['charges'])
print(f"\n📊 Correlation between BMI and insurance charges: {bmi_corr:.4f}")

#


