import pandas as pd

# Read AI results
df = pd.read_csv("output/results.csv")

# Random sample
sample = df.sample(
    n=20,
    random_state=42
).reset_index(drop=True)

# Columns for manual verification
sample["manual_authentication"] = ""
sample["manual_self_serve"] = ""
sample["manual_api_surface"] = ""
sample["manual_buildable"] = ""

sample["auth_correct"] = ""
sample["self_serve_correct"] = ""
sample["api_correct"] = ""
sample["buildable_correct"] = ""

sample["notes"] = ""

sample.to_csv(
    "output/verification_template.csv",
    index=False
)

print("Verification template created.")
