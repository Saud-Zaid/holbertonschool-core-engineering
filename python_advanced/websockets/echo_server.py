#!/usr/bin/env python3
"""Minimal WebSocket echo server listening on 127.0.0.1:8765."""

import asyncio
import websockets


async def connection_handler(websocket) -> None:
    """Echo each incoming text message back to the sender."""
    async for message in websocket:
        await websocket.send(message)


async def main() -> None:
    """Start the WebSocket echo server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
