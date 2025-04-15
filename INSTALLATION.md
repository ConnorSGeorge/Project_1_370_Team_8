# Installation and Running Guide for Sanic App

## Prerequisites
- Ensure you have Docker installed on your Linux system as. You can install Docker by following the official [Docker installation guide](https://docs.docker.com/get-docker/).
- Install the Docker Compose plugin for your docker installation with the following commands:
  
  ```bash
  sudo apt-get update
  sudo apt-get install docker-compose-plugin
  ```

## Steps to Build and Run the Application

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Project_1_370_Team_8
   ```

2. **Build & Run the Application:**
   Run the following command to build and run the Docker containers as one application:
   ```bash
   docker compose up
   ```

3. **Access the Application:**
   Open your browser or use a tool like `curl` to access the application at:
   ```
   http://localhost:8000
   ```

   You should see a JSON response:
   ```json
   {"message": "Hello, world!"}
   ```
