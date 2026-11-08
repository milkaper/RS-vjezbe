from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"poruka": "Dobrodošli"}

@app.get("/status")
def status_sustava():
    return {"status": "aktivan", "verzija": "1.0"}