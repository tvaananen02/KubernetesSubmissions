import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

PORT = int(os.environ.get("PORT", "8000"))
COUNTER_FILE = os.environ.get("COUNTER_FILE", "/usr/src/app/files/pingpong.txt")

def read_counter():
    try:
        with open(COUNTER_FILE) as f:
            return int(f.read().strip() or 0)
    except FileNotFoundError:
        return 0

def write_counter(value):
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))


counter = read_counter()  # continue from the saved value after a restart

app = FastAPI()

@app.get("/pingpong", response_class=PlainTextResponse)
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    write_counter(counter)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)