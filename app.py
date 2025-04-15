from sanic import Sanic
from sanic.response import json
from sanic.exceptions import SanicException
import asyncio
import logging
from websocket import create_connection
from pymongo import MongoClient

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


# Initialize MongoDB client
client = MongoClient('mongodb://mongo:27017')
db = client.storedb
orders_collection = db.orders

# Sample data for populating the database
users_data = [
    {"id": "1", "name": "John Doe", "email": "john.doe@example.com"},
    {"id": "2", "name": "Jane Smith", "email": "jane.smith@example.com"},
    {"id": "3", "name": "Alice Johnson", "email": "alice.johnson@example.com"}
]
orders_data = [
    {"order_id": "101", "user_id": "1", "product_id": "1001", "quantity": 1},
    {"order_id": "102", "user_id": "2", "product_id": "1002", "quantity": 2},
    {"order_id": "103", "user_id": "3", "product_id": "1003", "quantity": 1},
    {"order_id": "104", "user_id": "1", "product_id": "1003", "quantity": 3}
]
products_data = [
    {"id": "1001", "name": "Laptop", "price": 1200},
    {"id": "1002", "name": "Smartphone", "price": 800},
    {"id": "1003", "name": "Tablet", "price": 600}
]

# Populate the database during app startup
users_collection = db.users
users_collection.delete_many({})
users_collection.insert_many(users_data)

orders_collection = db.orders
orders_collection.delete_many({})
orders_collection.insert_many(orders_data)

products_collection = db.products
products_collection.delete_many({})
products_collection.insert_many(products_data)
logging.info("Database populated successfully!")

@app.route('/orders', methods=['GET'])
async def get_orders(request):
    # Fetch all orders from the collection
    orders = list(orders_collection.find({}, {"_id": 0}))
    return json(orders)


# Add the background task to the app
app.add_task(background_task())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
