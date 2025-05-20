# Image Processing Pipeline on Kubernetes

This project demonstrates how to build and deploy a containerized image processing pipeline using Kubernetes. Users upload images via an API, which are then processed by background workers and stored in persistent storage.

---

## 🧱 Components

- **API (FastAPI)**: Accepts image uploads
- **Worker (Python)**: Resizes and stores images
- **Storage**: Uses a shared volume (PVC) or optionally S3/MinIO
- **Database (optional)**: For storing metadata (not yet implemented)
- **Queue (optional)**: Redis/RabbitMQ for decoupling (can be added)

---

## 📁 Folder Structure

```
image-pipeline/
├── api/
│   ├── main.py                # FastAPI app for uploads
│   ├── Dockerfile             # Container setup
│   └── requirements.txt       # API dependencies
│
├── worker/
│   ├── worker.py              # Image processor
│   ├── Dockerfile             # Container setup
│   └── requirements.txt       # Worker dependencies
│
├── k8s/
│   ├── api-deployment.yaml
│   ├── worker-deployment.yaml
│   ├── service-api.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── pvc.yaml
│
└── README.md
```

---

## 🚀 Quick Start

### 1. Build Docker Images
```bash
# In /api
docker build -t yourdockerhub/image-api .
# In /worker
docker build -t yourdockerhub/image-worker .
```

### 2. Push to Docker Hub
```bash
docker push yourdockerhub/image-api
docker push yourdockerhub/image-worker
```

### 3. Apply Kubernetes Resources
```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/worker-deployment.yaml
kubectl apply -f k8s/service-api.yaml
```

### 4. Test API Upload
```bash
curl -F "file=@test.jpg" http://localhost:30001/upload/
```

---

## 📦 Future Enhancements
- Add Redis queue between API and worker
- Add database for image metadata
- Add user authentication
- Add Ingress for domain routing
- Add Prometheus/Grafana for monitoring

---

## 🔗 License
MIT License

