from web_search import WebSearch
from dotenv import load_dotenv
from typing import Dict, Callable
from openai import OpenAI
from langsmith import traceable
import json 

load_dotenv()
client = OpenAI()


AVAILABLE_TOOLS = {
        "web_search" : WebSearch.search
}

TOOL_DESCRIPTIONS = """
        web_search : Use for internet/web search queries
        """


class Orchestration:

    @classmethod
    @traceable(name = "tool-selection")
    def pick_tool(cls, user_query : str) -> Dict:

        agent_action = f"""
                    Given the following task, suggest the right tool from the ones available, as a JSON object
                    (with no additional text, introduction or explanations)
                    
                    Dictionary of Available tools :
                    {TOOL_DESCRIPTIONS}

                    User task : 
                    {user_query}
                    
                    Expected Response Format :
                    {{"task : {user_query}, suggested_tool : tool_name}}
                    """
        response = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [
                {"role" : "user", "content" : agent_action}
            ]
        )


        response = response.choices[0].message.content
        return json.loads(response)

    @classmethod
    @traceable(name = "tool-execution")    
    def execute_tool(cls, tool_response: Dict):

        tool_name = tool_response["suggested_tool"]
        search_query = tool_response["task"]

        if tool_name not in AVAILABLE_TOOLS:
            raise ValueError(f"Unknown tool: {tool_name}")

        selected_tool = AVAILABLE_TOOLS[tool_name]

        return selected_tool(search_query)


if __name__ == "__main__":

    tool_selection = Orchestration.pick_tool(user_query = "history of bitcoin")
    print(tool_selection)
    print(Orchestration.execute_tool(tool_selection))