import os
from langchain_ollama import ChatOllama
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
from langchainhub import Client

API_KEY = "apikey"

llm = ChatOllama(
    model="nemotron-3-nano:30b-cloud",
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {API_KEY}"
        }
    },
    temperature=0,
)

tools = [DuckDuckGoSearchRun()]
template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

To use a tool, please use the exact format:
Thought: I need to use a tool to find information.
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)

When you have the final answer, use this format:
Thought: I now have the full information for the report.
Final Answer: [Your structured report here]

STRICT REPORT STRUCTURE FOR FINAL ANSWER:
- Title
- Category
- Description
- Framework Mapping (MITRE ATT&CK and/or STRIDE)
- IOCs
- Detailed Vulnerability Info
- Mitigation
- Detection

Begin!

Question: {input}
Thought: {agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)










agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
    max_iterations=5,
    early_stopping_method="generate"
)


task = (
    "Search for the latest cybersecurity breaches, ransomware, and zero-day exploits "
    "from the last 30 days. Provide a structured report for the most significant ones."
)

try:
    print("--- Starting Cyber Intelligence Gathering ---")
    response = agent_executor.invoke({"input": task})
    print("\n\nFINAL REPORT:\n")
    print(response["output"])
except Exception as e:
    print(f"An error occurred: {e}")
