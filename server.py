#!/usr/bin/env python3
"""
Zundoko MCP Server

A sample Model Context Protocol (MCP) server using fastmcp that provides
a tool to randomly return "Zun" or "Doko" text.
"""

import random
from fastmcp import FastMCP

mcp = FastMCP("Zundoko Server")

zundoko_history: list[str] = []

@mcp.resource(
    "zundoko://history",
    mime_type="application/json",
    annotations={"readOnlyHint": True, "idempotentHint": True}
)
def get_history() -> list[str]:
    """
    Returns the history of zundoko calls.

    Returns:
        list[str]: History of all zundoko calls
    """
    return zundoko_history

@mcp.tool
def get_zundoko() -> str:
    """
    Returns either "Zun" or "Doko" randomly.

    Returns:
        str: Either "Zun" or "Doko"
    """
    choices = ["Zun", "Doko"]
    result = random.choice(choices)
    zundoko_history.append(result)
    return result

if __name__ == "__main__":
    mcp.run()
