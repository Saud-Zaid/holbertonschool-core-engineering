#!/usr/bin/env python3
"""WebSocket server that broadcasts incoming messages to all clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message: str) -> None:
    """Send a formatted message to all currently connected clients."""
    payload = f"B:{message}"
    for client in list(connected_clients):
        try:
            await client.send(payload)
        except ConnectionClosed:
            connected_clients.discard(client)


async def handle_client(websocket) -> None:
    """Register a client, broadcast its messages, and remove on disconnect."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main() -> None:
    """Start the broadcast WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(handle_client, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
