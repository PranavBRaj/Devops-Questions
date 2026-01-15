# Docker + Kubernetes (Minikube) Deployment – Simple HTML App

This project demonstrates a **basic MLOps-style workflow** using **Docker, Nginx, and Kubernetes (Minikube)**.  
A simple HTML page is containerized using Docker and deployed to a Kubernetes cluster.

---

## Phase 1: Project Initialization & File Creation

### Create Project Directory
Create a workspace directory and navigate into it.

```bash
mkdir mlops
cd mlops
```

### Create HTML File
Create a simple HTML file to be served by Nginx.

```bash
gedit html.html
```

Add the following content, save, and close:

```html
<h1>Hello from Docker</h1>
```

### Create Dockerfile
Create a Dockerfile to define image build instructions.

```bash
gedit Dockerfile
```

Add the following content:

```dockerfile
FROM nginx:latest
COPY html.html /usr/share/nginx/html/index.html
```

**Note:**  
The destination path ensures Nginx serves your custom HTML file as the default page.

---

## Phase 2: Build Docker Image

### Build Docker Image
Build the Docker image with a version tag.

```bash
docker build -t app:1.0 .
```

### Verify Image Creation
Check if the image was created successfully.

```bash
docker images
```

---

## Phase 3: Kubernetes Environment (Minikube)

### Start Minikube
Initialize the Kubernetes cluster using the Docker driver.

```bash
minikube start --driver=docker
```

**Note:**  
Ensure **Minikube** and **kubectl** are installed before running this command.

---

## Phase 4: Deployment Configuration

### Create Deployment YAML
Create a Kubernetes deployment configuration file.

```bash
gedit app.yaml
```

Add the following configuration:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      containers:
      - name: app
        image: app:1.0
        imagePullPolicy: Never
        ports:
        - containerPort: 80
```

**Important:**  
`imagePullPolicy: Never` ensures Kubernetes uses the **local Docker image** instead of pulling from Docker Hub.

### Load Image into Minikube
Explicitly load the local Docker image into Minikube.

```bash
minikube image load app:1.0
```

---

## Phase 5: Deploy and Expose Application

### Apply Deployment Configuration
Deploy the application to the Kubernetes cluster.

```bash
kubectl apply -f app.yaml
```

### Verify Pod Status
Check if the pod is running.

```bash
kubectl get pods
```

### Expose the Deployment
Expose the deployment using a NodePort service.

```bash
kubectl expose deployment app-deploy --type=NodePort --port=80
```

### Get Service URL
Retrieve the URL to access the application.

```bash
minikube service app-deploy --url
```

### Verify in Browser
Copy the generated URL (e.g., `http://127.0.0.1:xxxxx`)  
Paste it into a web browser to see:

```
Hello from Docker
```

---

## Phase 6: Scaling the Application

### Scale Deployment
Increase the number of replicas to 3.

```bash
kubectl scale deployment app-deploy --replicas=3
```

### Verify Scaling
Check pod status to confirm 3 running instances.

```bash
kubectl get pods
```

---

## Final Outcome

- Created a Dockerized HTML application
- Built and tagged a Docker image
- Deployed the container to Kubernetes using Minikube
- Exposed the service externally
- Successfully scaled the application pods

---

## Project Structure

```text
mlops/
├── html.html
├── Dockerfile
├── app.yaml
└── README.md
```
