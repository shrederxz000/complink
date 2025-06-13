from fastapi import FastAPI
import uvicorn

app = Fastapi()

@app.get("/")
def ping():
    return {"msg": "pong"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)
