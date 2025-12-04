from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API de trading táctica funcionando 🚀"}

@app.get("/ping")
def ping():
    return {"pong": True}
