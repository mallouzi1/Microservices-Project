# Microservices Hands-On Project

This project demonstrates a basic microservice architecture with three services:
- **User Service** (port 5001)
- **Product Service** (port 5002)
- **Order Service** (port 5003)

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Project

```bash
docker-compose up --build
```

### Example Requests

- **Register a user**:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username": "alice", "password": "secret"}' \
http://localhost:5001/register
```

- **Add a product**:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"id": "p1", "name": "Notebook"}' \
http://localhost:5002/products
```

- **Place an order**:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username": "alice", "product_id": "p1"}' \
http://localhost:5003/order
```
