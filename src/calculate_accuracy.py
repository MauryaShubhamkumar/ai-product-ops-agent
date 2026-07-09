import pandas as pd
import json

df = pd.read_csv("output/verification_template.csv")

fields = [
    "auth_correct",
    "self_serve_correct",
    "api_correct",
    "buildable_correct"
]

total = 0
correct = 0

for field in fields:

    values = df[field].fillna("").astype(str).str.lower()

    correct += values.isin(["true", "yes"]).sum()

    total += len(values)

accuracy = (correct / total) * 100

print(f"Accuracy : {accuracy:.2f}%")
print(f"{correct}/{total}")

summary = {
    "sample_size": len(df),
    "total_checks": total,
    "correct": int(correct),
    "accuracy": round(accuracy, 2)
}

with open(
    "output/verification_summary.json",
    "w"
) as f:

    json.dump(summary, f, indent=4)

print("Verification summary saved successfully.")

# Error Analysis
errors = []

for _, row in df.iterrows():

    if str(row["auth_correct"]).lower() not in ["true", "yes"]:
        errors.append({
            "app": row["app_name"],
            "field": "Authentication"
        })

    if str(row["api_correct"]).lower() not in ["true", "yes"]:
        errors.append({
            "app": row["app_name"],
            "field": "API Surface"
        })

    if str(row["self_serve_correct"]).lower() not in ["true", "yes"]:
        errors.append({
            "app": row["app_name"],
            "field": "Self Serve"
        })

    if str(row["buildable_correct"]).lower() not in ["true", "yes"]:
        errors.append({
            "app": row["app_name"],
            "field": "Buildable"
        })

pd.DataFrame(errors).to_csv(
    "output/errors.csv",
    index=False
)

print(f"Errors list saved successfully. Total errors: {len(errors)}")
