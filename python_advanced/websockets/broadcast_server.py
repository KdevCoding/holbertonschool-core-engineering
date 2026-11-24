#!/usr/bin/env python3
"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve,broadcast

CLIENTS = set()

async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            broadcast(CLIENTS, f"B:{message}")
    finally:
        CLIENTS.discard(websocket)

async def main():
    server = await serve(handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
