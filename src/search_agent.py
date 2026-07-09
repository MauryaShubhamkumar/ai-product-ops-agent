import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")


class SearchAgent:

    def search(self, app_name):
        url = "https://google.serper.dev/search"

        payload = {
            "q": f"{app_name} official developer api documentation"
        }

        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }

        for attempt in range(3):
            try:
                response = requests.post(
                    url,
                    headers=headers,
                    json=payload
                )
                response.raise_for_status()
                data = response.json()
                return data.get("organic", [])[:3]
            except Exception as e:
                print(f"Serper search failed (attempt {attempt + 1}/3): {e}. Retrying in 2 seconds...")
                time.sleep(2)

        raise Exception("Search Failed after 3 attempts")
