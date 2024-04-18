from fastapi import FastAPI
from pydantic import BaseModel

from helpers.trainer import SentimentTrainer

app = FastAPI()

class Item(BaseModel):
    text: str

def get_model():

    return SentimentTrainer(
        train_path="data/train.csv",
        valid_path="data/valid.csv",
        test_path="data/test.csv",
        emotion="anger",
        pretrained_model="bert-base-uncased",
        seq_len=300,
        batch_size=32,
        num_train_epochs=10,
        lr=5e-5
    )

def train():
    model = get_model()
    model.tokenize_and_encode()

@app.post("/classify/")
async def classify_text(item: Item):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
