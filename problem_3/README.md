Create a simple web application (HTML or Python Flask).Write a Dockerfile, build a Docker 
image, and run the container so the application is accessible on a browser using port 
mapping.
 Using Docker commands, perform the following operations:
● List images and containers
● Stop a running container
● Remove a container and image
Demonstrate commands like: docker ps, docker stop, docker rm, docker rmi.
Simple Web Application Dockerization and Docker Operations

This project demonstrates:
- Creating a simple HTML web application
- Dockerizing the application using Nginx
- Running and verifying the container
- Performing basic Docker operations (images & containers management)

---

## Question 4: Create a Simple Web Application and Dockerize

### Step 1: Create Project Directory
Create a new folder and navigate into it.

```bash
mkdir appDocker
cd appDocker
```

---

### Step 2: Create HTML File
Create and edit the `index.html` file.

```bash
gedit index.html
```

Add the following content:

```html
<h1>Hello from Docker</h1>
```

Save and close the file.

---

### Step 3: Create Dockerfile
Create and edit the Dockerfile.  
**Note:** The filename must start with a capital **D**.

```bash
gedit Dockerfile
```

Add the following content:

```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html
```

Save and close the file.

---

### Step 4: Verify Docker Installation and Service

Check if Docker is installed:

```bash
docker --version
```

If Docker is not installed or not running, install and start it:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

---

### Step 5: Build the Docker Image
Build the Docker image using the current directory.

```bash
sudo docker build -t html-app:1.0 .
```

**Note:**  
- Image names must be lowercase  
- Use `sudo` if permission is denied

---

### Step 6: Run the Docker Container
Run the container in detached mode and map ports.

```bash
sudo docker run -d -p 8080:80 html-app:1.0
```

- Local port: **8080**
- Container port: **80**

---

### Step 7: Verify in Browser
Open a web browser and navigate to:

```
http://localhost:8080
```

You should see:

```
Hello from Docker
```

---

## Question 5: Docker Operations

### Step 1: List Docker Images
Display all available Docker images.

```bash
sudo docker images
```

---

### Step 2: List Running Containers
Check currently running containers.

```bash
sudo docker ps
```

To view all containers (including stopped ones):

```bash
sudo docker ps -a
```

---

### Step 3: Stop the Running Container
Stop the container using its **Container ID**.

```bash
sudo docker stop <CONTAINER_ID>
```

**Example:**

```bash
sudo docker stop b5b081bf87e2
```

---

### Step 4: Remove the Container
Delete the stopped container.

```bash
sudo docker rm <CONTAINER_ID>
```

---

### Step 5: Remove the Docker Image
Delete the Docker image created earlier.

```bash
sudo docker rmi html-app:1.0
```

---

## Final Outcome

- Created a simple HTML web application
- Dockerized the application using Nginx
- Built and ran a Docker container successfully
- Verified application access through a browser
- Performed essential Docker image and container management operations

---

## Project Structure

```text
appDocker/
├── index.html
├── Dockerfile
└── README.md
```
