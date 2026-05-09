from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()


client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class WebSearch:
    @traceable
    def search(search_term : str):

        response = client.search(
            query= search_term,
            max_results = 5
        )

        for result in response["results"]:
            print("Title:", result["title"])
            print("URL:", result["url"])
            print("Content:", result["content"])
            print("-" * 50)

        return response 

if __name__ == "__main__":
    print(WebSearch.search("latest news"))