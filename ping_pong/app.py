import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

PORT = int(os.environ.get("PORT", "8000"))
counter = 0  
app = FastAPI()

@app.get("/pingpong", response_class=PlainTextResponse)
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)