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

        resources = await client.list_resources()
        print(f"Available resources: {resources}")

        resource_templates = await client.list_resource_templates()
        print(f"Available resource templates: {resource_templates}")

        prompts = await client.list_prompts()
        print(f"Available prompts: {prompts}")

        prompt_result = await client.get_prompt("explain_zundoko_kiyoshi")
        print(f"\nPrompt result:\n{prompt_result}")

        for i in range(5):
            result = await client.call_tool("get_zundoko", {})
            print(f"Result {i+1}: {result.content[0].text}")

        history = await client.read_resource("zundoko://history")
        print(f"\nZundoko History:\n{history}")

        first_zundoko = await client.read_resource("zundoko://history/1")
        print(f"\nFirst Zundoko:\n{first_zundoko}")


if __name__ == "__main__":
    asyncio.run(main())
