from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk import Agent
from google.adk.tools import FunctionTool
import random

from dotenv import load_dotenv
load_dotenv()

# Helper functions for the coordinator
def roll_dice(sides: int = 6) -> str:
    """Roll a dice with specified number of sides."""
    result = random.randint(1, sides)
    return f"🎲 Rolled a {result} on a {sides}-sided dice!"

def is_prime(number: int) -> str:
    """Check if a number is prime."""
    if number < 2:
        return f"{number} is not a prime number."
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number."
    return f"{number} is a prime number!"

# Create remote agents for specialized tasks
general_knowledge_agent = RemoteA2aAgent(
    name="general_knowledge_remote",
    description="Remote agent that answers questions about general knowledge.",
    agent_card=f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}",
)

weather_agent = RemoteA2aAgent(
    name="weather_remote", 
    description="Remote agent that answers questions about weather.",
    agent_card=f"http://localhost:8002/{AGENT_CARD_WELL_KNOWN_PATH}",
)

# Create coordinator agent with tools
coordinator_agent = Agent(
    name="coordinator_agent",
    model="gemini-2.0-flash",
    description=(
        "Smart coordinator agent that can handle basic tasks like rolling dice and checking prime numbers, "
        "and intelligently routes specialized questions to appropriate remote agents."
    ),
    instruction=(
        "You are a helpful coordinator agent. You can:"
        "1. Roll dice and check if numbers are prime using your built-in tools"
        "2. Route general knowledge questions to the general_knowledge_agent"
        "3. Route weather questions to the weather_agent"
        "4. Handle basic math, dice rolling, and prime number checking yourself"
        "When users ask about general knowledge (history, science, facts), connect to general_knowledge_agent."
        "When users ask about weather, connect to weather_agent."
        "For dice rolling and prime numbers, use your own tools."
    ),
    tools=[
        FunctionTool(roll_dice),
        FunctionTool(is_prime)
    ],
    sub_agents=[general_knowledge_agent, weather_agent]
)

# Export the coordinator as the main agent
root_agent = coordinator_agent
