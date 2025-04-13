from sanic import Sanic
from sanic.response import json
from sanic.exceptions import SanicException
import asyncio
import logging
from websocket import create_connection

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Sanic("AsyncApp")

@app.route("/")
async def hello_world(request):
    return json({"message": "Hello, world!"})

@app.route("/async")
async def async_example(request):
    logging.info("Received request at /async")
    await asyncio.sleep(6)  # Simulate an asynchronous operation
    logging.info("Finished processing request at /async")
    return json({"message": "This is an asynchronous response!"})

# Background task example
async def background_task():
    while True:
        logging.info("Background task is running...")
        await asyncio.sleep(5)  # Simulate periodic work

@app.route("/error")
async def error_route(request):
    raise SanicException("This is a custom error!", status_code=400)

@app.exception(SanicException)
async def handle_sanic_exception(request, exception):
    return json({"error": str(exception)}, status=exception.status_code)

@app.websocket("/ws")
async def websocket_handler(request, ws):
    data = await ws.recv()  # Wait for a single message from the client
    await ws.send(f"Echo: {data}")  # Echo the message back to the client

# Add the background task to the app
app.add_task(background_task())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
