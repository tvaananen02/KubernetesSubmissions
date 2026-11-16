import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

PORT = int(os.environ.get("PORT", "8000"))
LOG_FILE = os.environ.get("LOG_FILE", "/usr/src/app/files/log.txt")
COUNTER_FILE = os.environ.get("COUNTER_FILE", "/usr/src/app/files/pingpong.txt")

def last_log_line():
    try:
        with open(LOG_FILE) as f:
            lines = f.read().splitlines()
        return lines[-1] if lines else "No log yet"
    except FileNotFoundError:
        return "No log yet"

def pingpong_count():
    try:
        with open(COUNTER_FILE) as f:
            return int(f.read().strip() or 0)
    except FileNotFoundError:
        return 0

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def status():
    return f"{last_log_line()}.\nPing / Pongs: {pingpong_count()}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)