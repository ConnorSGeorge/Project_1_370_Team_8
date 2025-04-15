# Using the Features of the Sanic Application via Docker

This guide explains how to use and test all the features of the Sanic application (`app.py`) when running it through Docker.

## Prerequisites

1. Ensure Docker is installed on your system, as well as the . You can install Docker by following the official [Docker installation guide](https://docs.docker.com/get-docker/).
2. Ensure that your MongoDB service is running, with an already populated version of the storedb from class
3. Run the command to start the MongoDB service and build the Docker image for the application:
4. 
   ```bash
   docker compose up
   ```
   The application will now be accessible at `http://localhost:8000`.

---

## 1. Test the Root Route (`/`)

### Description:
The root route returns a simple JSON response.

### Steps:
1. Open a browser or use `curl` to send a GET request:
   ```bash
   curl http://localhost:8000/
   ```
2. Expected Response:
   ```json
   {
       "message": "Hello, world!"
   }
   ```

---

## 2. Test the Asynchronous Route (`/async`)

### Description:
The `/async` route demonstrates asynchronous behavior by simulating a delay.

### Steps:
1. Send a GET request to the `/async` route:
   ```bash
   curl http://localhost:8000/async
   ```
2. Expected Behavior:
   - The server logs will show:
     ```
     Received request at /async
     Finished processing request at /async
     ```
   - The response will be:
     ```json
     {
         "message": "This is an asynchronous response!"
     }
     ```

---

## 3. Observe the Background Task

### Description:
A background task runs every 5 seconds, logging a message.

### Steps:
1. Start the Docker container as described above.
2. Observe the server logs. Every 5 seconds, you should see:
   ```
   Background task is running...
   ```

---

## 4. Test the Error Route (`/error`)

### Description:
The `/error` route raises a custom error to demonstrate error handling.

### Steps:
1. Send a GET request to the `/error` route:
   ```bash
   curl http://localhost:8000/error
   ```
2. Expected Response:
   ```json
   {
       "error": "This is a custom error!"
   }
   ```
3. The server logs will show the error being handled.

---

## 5. Test the WebSocket Route (`/ws`) Using `wscat`

### Description:
The `/ws` route demonstrates WebSocket support by allowing real-time, bidirectional communication between the client and the server.

### Steps:
1. Open a terminal inside the running Docker container:
   ```bash
   docker exec -it <container_id> /bin/bash
   ```
   Replace `<container_id>` with the ID of the running container. You can find it using:
   ```bash
   docker ps
   ```

2. Use `wscat` to connect to the WebSocket endpoint:
   ```bash
   wscat -c ws://127.0.0.1:8000/ws
   ```

3. Send a message to the server:
   ```
   Hello, server!
   ```

4. Expected Behavior:
   - The server will echo the message back to the client.
   - For example:
     ```
     > Hello, server!
     < Echo: Hello, server!
     ```

## 6. Test the MongoDB Example Route (`/orders`), similar to class exercises

### Description:
The `/orders` route demonstrates an asynchronous connection to a MongoDB server running in a container using docker compose.
The output will be all of the orders from the storedb database we used for demos in class.

### Steps:
1. Send a GET request to the `/orders` route:
   ```bash
   curl http://localhost:8000/orders
   ```
2. Expected Response:
   ```json
   [
       {"order_id": "101", "user_id": "1", "product_id": "1001", "quantity": 1},
       {"order_id": "102", "user_id": "2", "product_id": "1002", "quantity": 2},
       {"order_id": "103", "user_id": "3", "product_id": "1003", "quantity": 1},
       {"order_id": "104", "user_id": "1", "product_id": "1003", "quantity": 3}
   ]
   ```
