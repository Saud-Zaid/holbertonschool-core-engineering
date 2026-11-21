#!/usr/bin/env python3
"""WebSocket server that validates incoming messages before responding."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def handle_client(websocket) -> None:
    """Receive messages from a client, validate them, and send a reply."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main() -> None:
    """Start the validation WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(handle_client, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
