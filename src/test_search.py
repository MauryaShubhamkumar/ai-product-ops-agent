from search_agent import SearchAgent

apps = [
    "Salesforce",
    "Slack",
    "Stripe",
    "Shopify"
]

agent = SearchAgent()

for app in apps:
    print("="*60)
    print(app)
    print("="*60)
    results = agent.search_docs(app)
    for r in results:
        print(r["title"])
        print(r["link"])
        print()
