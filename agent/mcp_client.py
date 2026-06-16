import asyncio

from fastmcp import Client


client = Client(
    "http://localhost:8000/mcp"
)


async def call_mcp_tool(
        tool_name: str,
        **kwargs
):
    """
    Call MCP Tool
    """

    async with client:

        result = await client.call_tool(
            tool_name,
            kwargs
        )

        return result


async def get_all_tools():
    """
    List all available MCP tools
    """

    async with client:

        tools = await client.list_tools()

        return tools


if __name__ == "__main__":

    tools = asyncio.run(
        get_all_tools()
    )

    print("\nAvailable Tools:\n")

    for tool in tools:
        print(tool.name)