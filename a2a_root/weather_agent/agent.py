# STEP 0 - load environment variables
from dotenv import load_dotenv

load_dotenv()
import os 
import requests
weatherAPIKey = str(os.getenv('weatherAPIKey'))

# STEP 1 - Import libraries
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk import Agent
from google.adk.tools import FunctionTool

def get_temperature(city: str) -> dict:
    """Gets the current temperature for a given city.

    Args:
        city (str): The name of the city (e.g., 'San Francisco').

    Returns:
        dict: A dictionary containing the temperature data or an error message.
    """
    print("Entered the method / function get_temperature");
    weatherAPIUrl = "http://api.weatherapi.com/v1/current.json?key=" + weatherAPIKey + "&q=" + city;
    print(weatherAPIUrl)
    response = requests.get(weatherAPIUrl)
    data = response.json()
    print(data)
    return data

# def get_weather(city: str) -> str:
#     return f"It's always sunny in {city}"

# STEP 2 - Create the agent 
root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about weather."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about weather."
    ),
    tools=[FunctionTool(get_temperature)]
)
# STEP 3 - Make your agent A2A-compatible
# The to_a2a() function will even auto-generate an agent card in-memory behind-the-scenes by extracting skills, capabilities, and metadata from the ADK agent
# so that the well-known agent card is made available when the agent endpoint is served using uvicorn.
# The to_a2a() function will return a FastAPI app instance, which you can then serve using uvicorn.
a2a_app = to_a2a(root_agent, port=8002)

# STEP 4 - Serve the agent using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(a2a_app, host="0.0.0.0", port=8002)

# agent card url : http://localhost:8002/.well-known/agent.json
# The agent card is a JSON file that contains metadata about the agent, such as its name, description, and supported capabilities.
# The agent card is used by the A2A platform to discover and interact with the agent.
# {"capabilities":{},"defaultInputModes":["text/plain"],"defaultOutputModes":["text/plain"],"description":"Agent to answer questions about general knowledge.","name":"hello_world_agent","preferredTransport":"JSONRPC","protocolVersion":"0.3.0","skills":[{"description":"Agent to answer questions about general knowledge. I am a helpful agent who can answer user questions about general knowledge.","id":"hello_world_agent","name":"model","tags":["llm"]}],"supportsAuthenticatedExtendedCard":false,"url":"http://localhost:8001","version":"0.0.1"}