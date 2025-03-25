import pandas as pd

# Load your dataset
df = pd.read_csv("insurance.csv")

# Save features as variables
ages = df['age']
sexes = df['sex']
bmis = df['bmi']
children = df['children']
smokers = df['smoker']
regions = df['region']
charges = df['charges']

# Region breakdown
region_counts = regions.value_counts()
most_common_region = region_counts.idxmax()
most_common_count = region_counts.max()

print(f"\nThere are four regions in the dataset. The most represented region is '{most_common_region}' with {most_common_count} individuals.\n")
print(region_counts)

# Smoker vs. non-smoker costs
smoker_costs = df.groupby('smoker')['charges'].mean()
print("\nWe analyzed the difference in medical insurance charges between smokers and non-smokers:")
print(f"- Non-smokers pay an average of ${smoker_costs['no']:.2f}")
print(f"- Smokers pay an average of ${smoker_costs['yes']:.2f}, which is almost 4 times more.\n")

# Cost influence based on BMI and children
bmi_corr = bmis.corr(charges)
children_corr = children.corr(charges)

print("We also explored how BMI and number of children influence insurance costs:")
print(f"- Correlation between BMI and charges: {bmi_corr:.2f} (low positive correlation)")
print(f"- Correlation between number of children and charges: {children_corr:.2f} (very weak correlation)\n")

carmen_results = {
    "region_analysis": {
        "counts": region_counts.to_dict(),
        "most_common_region": most_common_region,
        "count": most_common_count
    },
    "smoker_vs_nonsmoker_costs": smoker_costs.to_dict(),
    "cost_estimates_based_on_variables": {
        "bmi_to_charges_correlation": bmi_corr,
        "children_to_charges_correlation": children_corr
    }
}

import json

with open("results/carmen_results.json", "w") as file:
    json.dump(carmen_results, file, indent=2)

