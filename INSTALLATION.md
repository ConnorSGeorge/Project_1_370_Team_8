# Installation and Running Guide for Sanic App

## Prerequisites
- Ensure you have Docker installed on your Linux system. You can install Docker by following the official [Docker installation guide](https://docs.docker.com/get-docker/).

## Steps to Build and Run the Application

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Project_1_370_Team_8
   ```

2. **Build the Docker Image**
   Run the following command to build the Docker image:
   ```bash
   docker build -t sanic-app .
   ```

3. **Run the Docker Container**
   Start the application by running the container:
   ```bash
   docker run -p 8000:8000 sanic-app
   ```

4. **Access the Application**
   Open your browser or use a tool like `curl` to access the application at:
   ```
   http://localhost:8000
   ```

   You should see a JSON response:
   ```json
   {"message": "Hello, world!"}
   ```
