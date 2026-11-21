#!/usr/bin/env python3
"""WebSocket server that handles multiple clients with unicast responses."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def handle_client(websocket) -> None:
    """Register a client, reply only to that client with U:, and clean up."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main() -> None:
    """Start the unicast WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(handle_client, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
