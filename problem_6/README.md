To design and deploy a multi-container application using Docker Compose by creating an 
application service and a dependent database/Redis service, configuring service 
dependencies, networks, and volumes, and verifying inter-container communication.

# Docker Compose with Redis – Data Persistence Demonstration

This project demonstrates:
- Running a Python application with Redis using **Docker Compose**
- Service orchestration with multiple containers
- **Data persistence** using Docker volumes
- Verification of container lifecycle behavior

---

## Step 1: Install and Start Docker Services

### Install Docker and Docker Compose
Open the terminal and install required Docker services.

```bash
sudo apt install docker-compose docker.io -y
```

### Start Docker Service

```bash
sudo systemctl start docker
```

---

## Step 2: Set Up Project Directory

Create a project directory and navigate into it.

```bash
mkdir ques8
cd ques8
```

---

## Step 3: Create the Application File (`app.py`)

### Create Python File

```bash
gedit app.py
```

### Code for `app.py`

```python
import redis

# Connect to the Redis host named 'redis' on standard port 6379
result = redis.Redis(host='redis', port=6379)

# Increment the 'count' key (initializes to 1 if it doesn't exist)
result.incr('count')

# Print the result
print('Count ', result.get('count').decode())
```

Save and close the file.

---

## Step 4: Create the Dockerfile

### Create Dockerfile  
(**Filename must be exactly `Dockerfile` or `dockerfile`**)

```bash
gedit dockerfile
```

### Content of `dockerfile`

```dockerfile
FROM python:3.10
RUN pip install redis
COPY app.py .
CMD ["python", "app.py"]
```

---

## Step 5: Create Docker Compose File (`docker-compose.yml`)

### Create Compose File

```bash
gedit docker-compose.yml
```

### Content of `docker-compose.yml`

```yaml
services:
  app:
    build: .
    depends_on:
      - redis

  redis:
    image: redis
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

This configuration:
- Builds the Python app image
- Runs a Redis container
- Uses a **named volume** (`redis-data`) for persistent storage

---

## Step 6: Build and Run the Application

Build images and start the containers:

```bash
sudo docker-compose up --build
```

### Expected Output

```text
Count 1
```

This confirms:
- Redis is running
- The counter key was created and incremented

---

## Step 7: Verify Data Persistence

### Stop Containers
Stop the running containers using:

```text
Ctrl + C
```

### Restart Containers

```bash
sudo docker-compose up --build
```

### Expected Output

```text
Count 2
```

This confirms that the **Redis volume persisted data** between container restarts.

---

## Step 8: Verify Running Containers (Optional)

In a new terminal tab, check active containers:

```bash
sudo docker ps
```

---

## Final Outcome

- Python application successfully connected to Redis
- Redis data persisted using Docker volumes
- Docker Compose orchestrated multi-container setup
- Stateful behavior verified across container restarts

---

## Project Structure

```text
ques8/
├── app.py
├── dockerfile
├── docker-compose.yml
└── README.md
```
