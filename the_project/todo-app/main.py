import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

PORT = int(os.environ.get("PORT", "8000"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server started in port {PORT}", flush=True)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
      <head><title>Todo app</title></head>
      <body>
        <h1>Todo app</h1>
        <p>Hello from Kubernetes!</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)