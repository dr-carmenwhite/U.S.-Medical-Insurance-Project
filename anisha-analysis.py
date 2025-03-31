import pandas as pd
import json

# Load the dataset
df = pd.read_csv("insurance.csv")

# Average age of all patients
average_age = df['age'].mean()
print(f"👥 The average age of all patients is: {average_age:.2f} years")

# Average age of patients with at least one child
parents_df = df[df['children'] > 0]
average_parent_age = parents_df['age'].mean()
print(f"👶 The average age of patients with at least one child is: {average_parent_age:.2f} years")

# Save to JSON
results = {
    "average_age_all_patients": round(average_age, 2),
    "average_age_parents": round(average_parent_age, 2)
}

with open("results/anisha_results.json", "w") as file:
    json.dump(results, file, indent=2)


