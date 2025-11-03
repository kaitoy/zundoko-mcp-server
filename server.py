#!/usr/bin/env python3
"""
Zundoko MCP Server

A sample Model Context Protocol (MCP) server using fastmcp that provides
a tool to randomly return "Zun" or "Doko" text.
"""

import random
from datetime import datetime
from fastmcp import FastMCP, Context
from fastmcp.exceptions import NotFoundError, ToolError
from fastmcp.resources import TextResource
from fastmcp.server.elicitation import (
    AcceptedElicitation,
    DeclinedElicitation,
    CancelledElicitation,
)

mcp = FastMCP("Zundoko Server")

zundoko_history: list[str] = []
kiyoshi: TextResource = None

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

@mcp.resource("zundoko://kiyoshi")
def get_kiyoshi() -> str:
    """
    Returns the kiyoshi resource if it has been created.

    Returns:
        str: The kiyoshi message with timestamp
    """
    if kiyoshi is None:
        raise NotFoundError("Kiyoshi has not been achieved yet")
    return kiyoshi.text

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
async def reset_zundoko_kiyoshi(ctx: Context) -> str:
    """
    Resets the zundoko history and removes kiyoshi.

    Returns:
        str: Confirmation message
    """
    zundoko_history.clear()
    global kiyoshi
    kiyoshi = None

    await ctx.session.send_resource_list_changed()
    await ctx.info("Reset Zundoko Kiyoshi.")

    return "Reset complete"

@mcp.tool
async def get_zundoko(ctx: Context) -> str:
    """
    Returns either "Zun" or "Doko" randomly.

    Returns:
        str: Either "Zun" or "Doko"
    """
    if kiyoshi:
        raise ToolError("The show is over.")

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

@mcp.tool
async def check_kiyoshi(ctx: Context) -> str:
    """
    Checks if the zundoko history matches the winning pattern (Zun Zun Zun Zun Doko)
    and elicits "Ki-yo-shi!" from the user if it does.

    Returns:
        str: Status message indicating whether the pattern was found and elicitation result
    """
    global kiyoshi

    history_count = len(zundoko_history)

    if history_count < 5:
        return f"History has only {history_count} item(s), need at least 5 to check for the pattern."

    if zundoko_history[-5:] == ["Zun", "Zun", "Zun", "Zun", "Doko"]:
        elicit_result = await ctx.elicit(
            "It's time to say Ki-yo-shi!",
            response_type=str
        )

        match elicit_result:
            case AcceptedElicitation(data=response):
                if "Ki-yo-shi!" == response:
                    kiyoshi = TextResource(
                        uri="zundoko://kiyoshi",
                        name="Ki-yo-shi!",
                        text=f"Ki-yo-shi! at {datetime.now().isoformat()}",
                    )
                    await ctx.session.send_resource_list_changed()
                    await ctx.info("Zundoko Kiyoshi completed.")
                    return "Perfect!'"
                else:
                    zundoko_history.clear()
                    await ctx.warning(f"User said '{response}', but the correct answer is 'Ki-yo-shi!'")
                    return f"Pattern found! But you said '{response}' instead of 'Ki-yo-shi!'"
            case DeclinedElicitation():
                zundoko_history.clear()
                await ctx.warning("User declined to say Ki-yo-shi!")
                return "Pattern found! You declined to say 'Ki-yo-shi!'"
            case CancelledElicitation():
                zundoko_history.clear()
                await ctx.info("Ki-yo-shi! cancelled.")
                return "Pattern found! You cancelled Ki-yo-shi!"
    else:
        return f"Pattern not found. Last 5 items: {zundoko_history[-5:]}"

if __name__ == "__main__":
    mcp.run()
