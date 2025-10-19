#!/usr/bin/env python3
"""
Simple MCP client to connect to the Zundoko MCP server and call the zundoko tool.
"""

import asyncio
from fastmcp import Client


async def main():
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        result = await client.call_tool("get_zundoko", {})
        print(f"Result: {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
