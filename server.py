#!/usr/bin/env python3
"""
Zundoko MCP Server

A sample Model Context Protocol (MCP) server using fastmcp that provides
a tool to randomly return "Zun" or "Doko" text.
"""

import random
from fastmcp import FastMCP, Context

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

@mcp.resource("zundoko://history/{index}")
def get_zundoko_from_history(index: int) -> str:
    """
    Returns a specific zundoko from history by index.

    Args:
        index: The index of the zundoko call (1-based)

    Returns:
        str: The zundoko value at the specified index
    """
    if index < 1 or index > len(zundoko_history):
        raise ValueError(f"Invalid index: {index}")
    return zundoko_history[index - 1]

@mcp.prompt
def explain_zundoko_kiyoshi() -> str:
    """
    Explains how to do Zundoko Kiyoshi.

    Returns:
        str: Explanation of the Zundoko Kiyoshi
    """
    return """
1. Randomly output either "Zun" or "Doko"
2. Continue until you get the sequence "Zun Zun Zun Zun Doko" (four "Zun"s followed by one "Doko")
3. When this sequence appears, output "Ki-yo-shi!" and end the program
"""

@mcp.tool
async def get_zundoko(ctx: Context) -> str:
    """
    Returns either "Zun" or "Doko" randomly.

    Returns:
        str: Either "Zun" or "Doko"
    """
    choices = ["Zun", "Doko"]
    result = random.choice(choices)
    zundoko_history.append(result)
    await ctx.session.send_resource_list_changed()
    
    history_count = len(zundoko_history)
    await ctx.info(
        f"Zundoko history now contains {history_count} item(s)",
        extra={"count": history_count, "latest": result}
    )
    
    return result

if __name__ == "__main__":
    mcp.run()
