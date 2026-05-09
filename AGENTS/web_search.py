from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()


client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@traceable
def search(search_term : str):

    response = client.search(
        query="Latest News",
        max_results=5
    )

    for result in response["results"]:
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"])
        print("-" * 50)

    return response 

print(search("latest news"))