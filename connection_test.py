from langsmith import traceable
from dotenv import load_dotenv
import os 

load_dotenv()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "sid-connection-test"

@traceable
def sample_function(a : int, b : int) -> int:
    return a + b 


print(sample_function(10, 11))
