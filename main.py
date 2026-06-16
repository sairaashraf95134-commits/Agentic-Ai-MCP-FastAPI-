from fastapi import FastAPI
from pydantic import BaseModel

from agent.assistant import assistant_agent

app = FastAPI(
    title="Agentic AI MCP Project",
    description="FastAPI + LangGraph + MCP",
    version="1.0"
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "Agentic MCP Project Running"
    }


@app.post("/ask")
def ask_agent(
        request: QueryRequest
):

    try:

        response = assistant_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.query
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": "123"
                }
            }
        )

        final_answer = response[
            "messages"
        ][-1].content

        return {
            "success": True,
            "query": request.query,
            "response": final_answer
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }