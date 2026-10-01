import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

PORT = int(os.environ.get("PORT", "8000"))
LOG_FILE = os.environ.get("LOG_FILE", "/usr/src/app/files/log.txt")
app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def status():
    try:
        with open(LOG_FILE) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return "No log yet"
    return lines[-1] if lines else "Nothing logged yet"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)