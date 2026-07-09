import json
import pandas as pd
import os

def generate():
    # Load data
    summary = json.load(open("output/summary.json"))
    verification = json.load(open("output/verification_summary.json"))
    df = pd.read_csv("output/results.csv")

    # Take only 10 rows
    sample = df.head(10)

    # Convert to HTML
    table = sample.to_html(
        index=False,
        classes="table"
    )

    # Create HTML content
    html = f"""<!DOCTYPE html>
<html>
<head>
<title>AI Product Ops Assignment</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<h1>
AI Product Ops Research Agent
</h1>

<h2>Summary</h2>
<ul>
<li>Total Apps : {summary['total_apps']}</li>
<li>OAuth Apps : {summary['oauth_apps']}</li>
<li>Self Serve : {summary['self_serve']}</li>
<li>Buildable : {summary['buildable']}</li>
</ul>

<h2>Verification</h2>
<ul>
<li>Sample Size : {verification['sample_size']}</li>
<li>Accuracy : {verification['accuracy']}%</li>
</ul>

<h2>Sample Results</h2>
{table}

<h2>Charts</h2>
<img src="auth.png">
<img src="category.png">
<img src="selfserve.png">

</body>
</html>
"""

    # Save
    os.makedirs("report", exist_ok=True)
    with open("report/index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print("report/index.html generated successfully.")

if __name__ == "__main__":
    generate()
