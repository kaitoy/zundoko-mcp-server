#!/usr/bin/env python3
"""
HTTP MCP client that connects to the Zundoko MCP server via HTTP
and subscribes to notifications.
"""

import asyncio
from fastmcp import Client


async def handle_message(message):
    """Handle all messages from the server."""
    print(f"Received message: {message}")


async def main():
    async with Client(
        "http://127.0.0.1:8080/mcp",
        message_handler=handle_message
    ) as client:
        for _ in range(5):
            await client.call_tool("get_zundoko", {})


if __name__ == "__main__":
    asyncio.run(main())
