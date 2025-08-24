# Agent-to-Agent (A2A) Project Documentation

## Project Overview

This project demonstrates a multi-agent system using the Agent Development Kit (ADK). It consists of a coordinator agent that intelligently routes tasks to specialized remote agents. The coordinator can handle basic tasks like rolling dice and checking for prime numbers, while more complex queries are delegated to a general knowledge agent or a weather agent.

## Project Structure

The project is organized as follows:

-   `main.py`: The main entry point of the project.
-   `requirements.txt`: A list of Python dependencies required for the project.
-   `a2a_root/`: This directory contains the core logic for the agents.
    -   `agent.py`: This file defines the coordinator agent, which is the main agent of the project. It also defines the tools that the coordinator agent can use.
    -   `general_knowledge_agent/`: This directory contains the general knowledge agent.
        -   `agent.py`: This file defines the general knowledge agent, which is a remote agent that can answer questions about general knowledge.
    -   `weather_agent/`: This directory contains the weather agent.
        -   `agent.py`: This file defines the weather agent, which is a remote agent that can answer questions about the weather.

## Agents

### 1. Coordinator Agent

-   **Name:** `coordinator_agent`
-   **Description:** A smart coordinator agent that can handle basic tasks like rolling dice and checking prime numbers, and intelligently routes specialized questions to appropriate remote agents.
-   **Tools:**
    -   `roll_dice(sides: int = 6) -> str`: Rolls a dice with a specified number of sides.
    -   `is_prime(number: int) -> str`: Checks if a number is prime.
-   **Sub-Agents:**
    -   `general_knowledge_agent`: A remote agent that answers questions about general knowledge.
    -   `weather_agent`: A remote agent that answers questions about the weather.

### 2. General Knowledge Agent

-   **Name:** `general_knowledge_agent`
-   **Description:** An agent to answer questions about general knowledge.
-   **Instructions:** "You are a helpful agent who can answer user questions about general knowledge."

### 3. Weather Agent

-   **Name:** `weather_agent`
-   **Description:** An agent to answer questions about weather.
-   **Tools:**
    -   `get_weather(city: str) -> str`: Returns the weather for a given city.
-   **Instructions:** "You are a helpful agent who can answer user questions about weather."

## How to Run

To run the agents, you need to start each agent in a separate terminal.

1.  **Start the General Knowledge Agent:**
    ```bash
    uv run a2a_root/general_knowledge_agent/agent.py
    ```
    This will run the agent and it will be available at `http://localhost:8001/general_knowledge_agent` with agent card location `http://localhost:8001/.well-known/agent.json`


2.  **Start the Weather Agent:**
    ```bash
    uv run a2a_root/weather_agent/agent.py
    ```
    this will run the agent and it will be available at `http://localhost:8002/weather_agent` with agent card location `http://localhost:8002/.well-known/agent.json`

3.  **Start the Coordinator Agent:**
    The coordinator agent is not served as a separate endpoint, but it is used in the `agent.py` file of the `a2a_root` directory.
    TO run the coordinator agent, you need to start th run the command `adk web` from the root directory of the project 
    
    This will launch the coordinator agent and it will be available at `http://localhost:8000 with a2a_root as agent.  