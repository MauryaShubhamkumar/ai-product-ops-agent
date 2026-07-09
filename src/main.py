import pandas as pd
import time
import os
from tqdm import tqdm

from search_agent import SearchAgent
from research_agent import ResearchAgent

search = SearchAgent()
research = ResearchAgent()

apps = pd.read_csv("data/apps.csv")

results = []

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

for _, row in tqdm(apps.iterrows(), total=len(apps)):
    try:
        search_results = search.search(row["app_name"])
        data = research.research(
            row["app_name"],
            search_results
        )
        data["app_name"] = row["app_name"]
        data["website"] = row["website"]
        results.append(data)
    except Exception as e:
        print(f"\nError researching {row['app_name']}: {e}")
        results.append({
            "app_name": row["app_name"],
            "website": row["website"],
            "category": "Unknown",
            "description": "Unknown",
            "authentication": "Unknown",
            "self_serve": "Unknown",
            "api_surface": "Unknown",
            "mcp": "Unknown",
            "buildable": "Unknown",
            "blocker": "Unknown",
            "evidence": "Unknown",
            "error": str(e)
        })
    
    # Save incrementally to make results visible in real-time
    pd.DataFrame(results).to_csv(
        "output/results.csv",
        index=False
    )
    
    # Rate limit control: Gemini free tier allows 15 RPM
    time.sleep(4)

print("Done")