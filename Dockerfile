# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages, including a WebSocket library
RUN pip install --no-cache-dir sanic websocket-client

# Install additional dependencies for MongoDB
RUN pip install --no-cache-dir pymongo

# Node.js and npm installation for wscat
RUN apt-get update && apt-get install -y nodejs npm && \
    npm install -g wscat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
