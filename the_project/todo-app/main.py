import os
import threading
import time
import urllib.request
from contextlib import asynccontextmanager
import uvicorn
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

PORT = int(os.environ.get("PORT", "8000"))
IMAGE_DIR = os.environ.get("IMAGE_DIR", "/usr/src/app/files")
IMAGE_URL = os.environ.get("IMAGE_URL", "https://picsum.photos/1200")
MAX_AGE = int(os.environ.get("IMAGE_MAX_AGE", "600"))  # seconds, 600 = 10 minutes
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")
TODOS = [
    "Learn Kubernetes",
    "Finish the course project",
    "Learn to love K3D",
]
fetch_lock = threading.Lock()

def image_age():
    try:
        return time.time() - os.path.getmtime(IMAGE_PATH)
    except FileNotFoundError:
        return None

def fetch_image():
    if not fetch_lock.acquire(blocking=False):
        return  # another request is already downloading
    try:
        os.makedirs(IMAGE_DIR, exist_ok=True)
        tmp_path = IMAGE_PATH + ".tmp"
        with urllib.request.urlopen(IMAGE_URL, timeout=10) as response, open(tmp_path, "wb") as f:
            f.write(response.read())
        os.replace(tmp_path, IMAGE_PATH)  # swap in the new image in one step
        print("Fetched a new image", flush=True)
    finally:
        fetch_lock.release()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server started in port {PORT}", flush=True)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
def root():
    todo_items = "\n".join(f"<li>{todo}</li>" for todo in TODOS)
    return f"""
    <!DOCTYPE html>
    <html>
      <head><title>Todo app</title></head>
      <body>
        <h1>Todo app</h1>
        <img src="/image" alt="Random image" style="max-width: 600px;">

        <form>
          <input type="text" name="todo" maxlength="140" placeholder="New todo (max 140 characters)">
          <button type="button">Send</button>
        </form>

        <ul>
          {todo_items}
        </ul>
      </body>
    </html>
    """

@app.get("/image")
def image(background_tasks: BackgroundTasks):
    age = image_age()
    if age is None:
        fetch_image()  # no image yet: download it now
    elif age > MAX_AGE:
        background_tasks.add_task(fetch_image)  # serve the old one once more, refresh after
    if not os.path.exists(IMAGE_PATH):
        return PlainTextResponse("Image not available", status_code=503)
    return FileResponse(IMAGE_PATH, media_type="image/jpeg", headers={"Cache-Control": "no-store"})

@app.get("/shutdown", response_class=PlainTextResponse)
def shutdown(background_tasks: BackgroundTasks):
    background_tasks.add_task(os._exit, 1)  # for testing: kill the container after responding
    return "Shutting down"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)