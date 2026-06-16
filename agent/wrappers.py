import json
import asyncio

from langchain.tools import BaseTool

from agent.mcp_client import (
    call_mcp_tool
)

from agent.schemas import (
    EmailInput,
    SearchInput,
    AddInput,
    SubtractInput,
    MultiplyInput,
    DivideInput
)


class MCPTool(BaseTool):

    name: str

    description: str

    mcp_tool_name: str

    class Config:
        arbitrary_types_allowed = True

    def _run(
            self,
            **kwargs
    ):

        print(
            f"\nCalling MCP Tool: {self.mcp_tool_name}"
        )

        result = asyncio.run(
            call_mcp_tool(
                self.mcp_tool_name,
                **kwargs
            )
        )

        return str(result)

    async def _arun(
            self,
            tool_input: str
    ):

        params = json.loads(
            tool_input
        )

        result = await call_mcp_tool(
            self.mcp_tool_name,
            **params
        )

        return str(result)


send_email_tool = MCPTool(
    name="send_email",
    description="""
    Send Email.
    Requires:
    to,
    subject,
    body
    """,
    mcp_tool_name="send_email_tool",
    args_schema=EmailInput
)


search_tool = MCPTool(
    name="internet_search",
    description="""
Search the internet using SerpAPI.
Use this tool whenever the user asks for:
- latest news
- current events
- weather
- sports results
- factual information
- recent updates

Input: search query string
Output: top search results with title, link and snippet.
""",
    mcp_tool_name="internet_search_tool",
    args_schema=SearchInput
)


add_tool = MCPTool(
    name="add_numbers",
    description="""
    Add two numbers.
    Requires:
    a,
    b
    """,
    mcp_tool_name="add_tool",
    args_schema=AddInput
)


subtract_tool = MCPTool(
    name="subtract_numbers",
    description="""
    Subtract two numbers.
    Requires:
    a,
    b
    """,
    mcp_tool_name="subtract_tool",
    args_schema=SubtractInput
)


multiply_tool = MCPTool(
    name="multiply_numbers",
    description="""
    Multiply two numbers.
    Requires:
    a,
    b
    """,
    mcp_tool_name="multiply_tool",
    args_schema=MultiplyInput
)


divide_tool = MCPTool(
    name="divide_numbers",
    description="""
    Divide two numbers.
    Requires:
    a,
    b
    """,
    mcp_tool_name="divide_tool",
    args_schema=DivideInput
)


ALL_TOOLS = [
    send_email_tool,
    search_tool,
    add_tool,
    subtract_tool,
    multiply_tool,
    divide_tool
]