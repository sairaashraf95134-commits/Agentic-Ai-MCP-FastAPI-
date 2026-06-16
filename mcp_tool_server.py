from fastmcp import FastMCP

from tools.email_tool import (
    send_email
)

from tools.search_tool import (
    internet_search
)

from tools.math_tool import (
    add,
    subtract,
    multiply,
    divide
)

mcp = FastMCP(
    "Agentic MCP Server"
)


@mcp.tool()
def send_email_tool(
        to: str,
        subject: str,
        body: str
):
    """
    Send email
    """

    return send_email(
        to,
        subject,
        body
    )


@mcp.tool()
def internet_search_tool(
        query: str
):
    """
    Search internet
    """

    return internet_search(
        query
    )


@mcp.tool()
def add_tool(
        a: int,
        b: int
):
    """
    Add numbers
    """

    return add(
        a,
        b
    )


@mcp.tool()
def subtract_tool(
        a: int,
        b: int
):
    """
    Subtract numbers
    """

    return subtract(
        a,
        b
    )


@mcp.tool()
def multiply_tool(
        a: int,
        b: int
):
    """
    Multiply numbers
    """

    return multiply(
        a,
        b
    )


@mcp.tool()
def divide_tool(
        a: int,
        b: int
):
    """
    Divide numbers
    """

    return divide(
        a,
        b
    )


if __name__ == "__main__":

    mcp.run(
        transport="http",
        port=8000
    )