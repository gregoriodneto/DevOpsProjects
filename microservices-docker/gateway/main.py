from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/go")
def call_go():
    res = requests.get("http://go-service:8080")
    return { "go-service": res.text }

@app.get("/python")
def call_python():
    res = requests.get("http://python-service:5000")
    return { "python-service": res.text }