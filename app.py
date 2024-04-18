from fastapi import FastAPI
from pydantic import BaseModel
from config import Config

app = FastAPI()

class Item(BaseModel):
    text: str


@app.get("/info/")
async def read_root():
    return {"message": "Welcome to the EmotionalDetector API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
