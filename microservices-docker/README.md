# 🐳 Projeto de Microserviços com Docker

Este é um projeto base de microserviços com Docker Compose que integra:

- ✅ Python (Flask) + MongoDB
- ✅ Go (API simples)
- ✅ Gateway (FastAPI)
- ✅ MongoDB com volume persistente

---

## 📦 Estrutura

```bash
microservicos/
├── docker-compose.yml
├── python-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── go-service/
│   ├── main.go
│   └── Dockerfile
├── gateway/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
└── data/
    └── db/ (persistência)
```

## 🚀 Como subir o projeto
1. Build e start dos containers:
```bash
docker compose up --build
```

2. Acessar os endpoints:
- GET /python: http://localhost:8000/python
- GET /go: http://localhost:8000/go

## 🛠️ Tecnologias
- Docker & Docker Compose
- MongoDB
- Flask
- Go
- FastAPI

## 🔒 Volumes
Os dados do MongoDB são persistidos no volume mongo-data.

## 📌 Observações
- Os serviços estão conectados via rede Docker interna (rede-micro).
- O gateway age como API Gateway, redirecionando chamadas para os serviços Go e Python.
- O projeto pode ser expandido com mais serviços futuramente.