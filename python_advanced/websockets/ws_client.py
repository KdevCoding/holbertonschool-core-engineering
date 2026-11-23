#!/usr/bin/env python3
"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://127.0.0.1:8765") as websocket:
        await websocket.send("Hello")
        message = await websocket.recv()
        print(message, end="")


if __name__ == "__main__":
    asyncio.run(hello())
