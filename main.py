from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"hello": name}
