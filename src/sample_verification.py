import pandas as pd

try:
    df = pd.read_csv("output/results.csv")
    
    if len(df) == 0:
        print("No results have been processed yet. Please wait for the main pipeline to start saving results.")
    else:
        sample_size = min(20, len(df))
        sample = df.sample(sample_size, random_state=42)

        sample.to_csv(
            "output/verification_sample.csv",
            index=False
        )

        print(f"Sampled {sample_size} apps for verification:")
        print(sample[["app_name"]])
except FileNotFoundError:
    print("Error: 'output/results.csv' not found. The main pipeline needs to process at least one app before this script can run.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
