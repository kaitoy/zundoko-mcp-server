#!/usr/bin/env python3
"""
HTTP MCP client that connects to the Zundoko MCP server via HTTP
and subscribes to notifications.
"""

import asyncio
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult
from fastmcp.client.logging import LogMessage
from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext
from openai import AsyncOpenAI


async def handle_message(message):
    """Handle all messages from the server."""
    print(f"Received message: {message}")


async def log_handler(message: LogMessage):
    """Handle log messages from the server."""
    print(f"Received Log: {message}")


kiyoshi_answered = False


async def sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    """Handle sampling requests from the server using OpenAI."""
    message_content = messages[0].content.text

    response = await AsyncOpenAI().responses.create(
        model="gpt-5-nano",
        input=message_content,
        max_output_tokens=params.maxTokens or 5120,
        temperature=params.temperature or 1.0,
    )

    return response.output_text


async def elicitation_handler(message: str, response_type: type, params, context):
    """Handle elicitation requests from the server."""
    global kiyoshi_answered

    user_input = input(f"{message}: ")
    kiyoshi_answered = True
    return ElicitResult(action="accept", content=response_type(value=user_input))


async def main():
    async with Client(
        "http://127.0.0.1:8080/mcp",
        message_handler=handle_message,
        log_handler=log_handler,
        elicitation_handler=elicitation_handler,
        sampling_handler=sampling_handler
    ) as client:
        print("Starting Zundoko Kiyoshi...\n")

        while True:
            if kiyoshi_answered:
                break

            try:
                await client.call_tool("get_zundoko", {})
                kiyoshi_check_result = await client.call_tool("check_kiyoshi", {})
                print(f"Kiyoshi check result: {kiyoshi_check_result}")
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                break

        await client.call_tool("reset_zundoko_kiyoshi", {})


if __name__ == "__main__":
    asyncio.run(main())
