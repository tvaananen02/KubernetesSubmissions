import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

PORT = int(os.environ.get("PORT", "8000"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server started in port {PORT}", flush=True)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Todo app"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)