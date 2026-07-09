import os
import json
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_page_text(url):
    response = requests.get(
        url,
        timeout=20,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    response.raise_for_status()
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )
    return soup.get_text(
        separator="\n",
        strip=True
    )[:25000]


class ResearchAgent:

    def research(self, app_name, search_results):
        doc_text = ""
        doc_url = ""
        
        # Try downloading page content from the search results links
        if search_results and len(search_results) > 0:
            for result in search_results:
                link = result.get("link")
                if link:
                    try:
                        print(f"\nDownloading page content for {app_name} from: {link}")
                        doc_text = get_page_text(link)
                        doc_url = link
                        if doc_text and len(doc_text.strip()) > 100:
                            break
                    except Exception as e:
                        print(f"Failed to download {link}: {e}. Trying next search result...")

        # Fallback to search snippets if downloading failed
        if not doc_text or len(doc_text.strip()) <= 100:
            print(f"Fallback to organic search snippets for {app_name}.")
            doc_text = json.dumps(search_results, indent=2)
            doc_url = search_results[0].get("link") if search_results else ""

        prompt = f"""
You are an API research analyst.

Use ONLY the provided documentation text or search snippets.

Do not guess.

If information is unavailable, write "Unknown".

Research this application:
App Name: {app_name}

Documentation Text:
{doc_text}

Return ONLY valid JSON.

Schema:

{{
"category":"",
"description":"",
"authentication":"",
"self_serve":"",
"api_surface":"",
"mcp":"",
"buildable":"",
"blocker":"",
"evidence":""
}}
"""

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

                text = response.text.strip()
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

                parsed_data = json.loads(text)
                # Overwrite empty evidence field with the official document URL
                if doc_url and (not parsed_data.get("evidence") or parsed_data.get("evidence") == "Unknown"):
                    parsed_data["evidence"] = doc_url
                return parsed_data
            except Exception as e:
                print(f"Gemini call failed (attempt {attempt + 1}/3): {e}. Retrying in 3 seconds...")
                time.sleep(3)

        raise Exception("Gemini failed after 3 attempts")
