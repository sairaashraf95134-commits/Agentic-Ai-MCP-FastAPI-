import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain.agents import create_agent

from langgraph.checkpoint.memory import (
    InMemorySaver
)

from agent.wrappers import (
    ALL_TOOLS
)

load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_retries=2,
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


memory = InMemorySaver()


assistant_agent = create_agent(
    model=llm,
    tools=ALL_TOOLS,
    checkpointer=memory,
    system_prompt="""
You are a helpful AI assistant.

You have access to:

1. Internet Search Tool
2. Email Tool
3. Add Tool
4. Subtract Tool
5. Multiply Tool
6. Divide Tool

Always use tools whenever required.

If user asks mathematical calculations,
use math tools.

If user asks web search,
use internet search tool.

If user asks email,
use email tool.
"""
)


if __name__ == "__main__":

    while True:

        user_input = input("\nAsk MCP Agent (type 'exit' to stop): ")

        if user_input.lower() == "exit":
            break

        response = assistant_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": "123"
                }
            }
        )

        print("\nResponse:\n")
        print(response["messages"][-1].content)