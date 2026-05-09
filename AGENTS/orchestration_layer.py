from web_search import WebSearch
from dotenv import load_dotenv
from typing import Dict
from openai import OpenAI
from langsmith import traceable

load_dotenv()
client = OpenAI()

class Orchestration:
    @classmethod
    @traceable(name = "tool-selection")
    def pick_tool(cls, user_query : str) -> Dict:

        agent_action = f"""
                    Given the following task, suggest the right tool from the ones available, as a JSON object
                    (with no additional text, introduction or explanations)
                    
                    Available tools :
                    {WebSearch.search} : for web search tasks

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


        return response.choices[0].message.content


tool_selection = Orchestration.pick_tool(user_query = "I want to search for the term 'bitcoin'")
print(tool_selection)