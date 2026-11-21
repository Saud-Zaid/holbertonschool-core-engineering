#!/usr/bin/env python3
"""Minimal WebSocket client that sends one message and prints the reply."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket URI, send text once, and return the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return str(response)


async def main() -> None:
    """Run the demo WebSocket client."""
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
