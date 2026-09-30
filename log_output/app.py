import asyncio
import os
import uuid
from contextlib import asynccontextmanager
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI

PORT = int(os.environ.get("PORT", "8000"))
random_string = str(uuid.uuid4())  # created once at startup, kept in memory

def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

async def log_forever():
    while True:
        print(f"{timestamp()}: {random_string}", flush=True)
        await asyncio.sleep(5)

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(log_forever())  # logging runs alongside the web server
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def status():
    return {"timestamp": timestamp(), "random_string": random_string}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)