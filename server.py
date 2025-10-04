#!/usr/bin/env python3
"""
Zundoko MCP Server

A sample Model Context Protocol (MCP) server using fastmcp that provides
a tool to randomly return "Zun" or "Doko" text.
"""

import random
from fastmcp import FastMCP

mcp = FastMCP("Zundoko Server")

@mcp.tool
def get_zundoko() -> str:
    """
    Returns either "Zun" or "Doko" randomly.

    Returns:
        str: Either "Zun" or "Doko"
    """
    choices = ["Zun", "Doko"]
    return random.choice(choices)

if __name__ == "__main__":
    mcp.run()
