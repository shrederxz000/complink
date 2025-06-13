from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping", tags= ["ping"])
def ping():
    """ping this site"""
    return {"msg": "pong"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)
