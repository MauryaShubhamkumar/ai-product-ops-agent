import json
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/results.csv")

print(df.head())

print("="*40)
print("AUTHENTICATION ANALYSIS:")
print("="*40)
auth = (
    df["authentication"]
    .fillna("Unknown")
    .value_counts()
)
print(auth)

print("\n" + "="*40)
print("SELF SERVE VS GATED:")
print("="*40)
self_serve = (
    df["self_serve"]
    .fillna("Unknown")
    .value_counts()
)
print(self_serve)

print("\n" + "="*40)
print("BUILDABILITY ANALYSIS:")
print("="*40)
buildable = (
    df["buildable"]
    .fillna("Unknown")
    .value_counts()
)
print(buildable)

print("\n" + "="*40)
print("BLOCKERS ANALYSIS:")
print("="*40)
blockers = (
    df["blocker"]
    .fillna("None")
    .value_counts()
)
print(blockers.head(10))

print("\n" + "="*40)
print("CATEGORY ANALYSIS:")
print("="*40)
category = (
    df["category"]
    .value_counts()
)
print(category)

import os
os.makedirs("report/assets", exist_ok=True)

# Generate Charts
auth.plot(kind="bar")
plt.title("Authentication Methods")
plt.tight_layout()
plt.savefig("report/assets/auth.png")
plt.close()

self_serve.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Self Serve vs Gated")
plt.savefig("report/assets/selfserve.png")
plt.close()

category.plot(kind="bar")
plt.title("Apps by Category")
plt.tight_layout()
plt.savefig("report/assets/category.png")
plt.close()

print("\nGenerated report charts successfully.")

# Summary Dictionary
summary = {
    "total_apps": len(df),
    "oauth_apps": int(auth.get("OAuth2", 0)),
    "api_key_apps": int(auth.get("API Key", 0)),
    "self_serve": int(self_serve.get("Yes", 0)),
    "gated": int(self_serve.get("Gated", 0)),
    "buildable": int(buildable.get("Yes", 0))
}

print("\nSummary Dictionary:")
print(summary)

# Save Summary
with open("output/summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("\nSaved output/summary.json successfully.")