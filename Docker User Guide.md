# Docker User Guide
A detailed user guide on how to run the container with Docker.

---

### Prerequisites
Install Docker on the host machine. You can install Docker from the official Docker website (https://www.docker.com/).

### Steps to Run the Container
First, open a terminal and then please execute the following command line.

#### Step 1. Pull the Docker Image
Pull my Docker image (elainahaha/my-senao-api:latest) from Docker hub.
```
docker pull elainahaha/my-senao-api:latest
```

#### Step 2. Run the Container
Run the container.
```
docker run -p <host-port>:<container-port> --name <container-name> -d elainahaha/my-senao-api:latest
```
Replace <host-port> with the port number on the host machine you want to map to the container, 
<container-port> with the port number used by the application in the container, 
and <container-name> with a desired name for the container.

For example:
```
docker run -p 5000:5000 --name test -d elainahaha/my-senao-api:latest
```

#### Step 3. Access the Application
Once the container is running, you can access the application by visiting `http://localhost:<host-port>` in your web browser. 
For example, if you mapped the container's port 5000 to the host's port 5000, you would access it at `http://localhost:5000`.

### Additional Commands
- Stop the Container  
  If you want to stop a running container, use this command:
  ```
  docker stop <container-name>
  ```

- Restart the Container  
  If you want to restart a stopped container, use this command:
  ```
  docker restart <container-name>
  ```

 The above instructions are basic guidelines to run this API in Docker container. 
 In addition, using Docker Desktop is another way to manage containers by providing a straightforward GUI.
