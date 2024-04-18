from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import Config
from controllers.jwt_token import verify_token
from pydantic import BaseModel
from models.openai_gpt35 import GPTClasifier

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class EmotionModel(BaseModel):
    model_name: str

class Query(BaseModel):
    text: str

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

async def get_inference_openai():
    cls = GPTClasifier()
    return cls

# @app.get("/info/")
# async def read_root(user: str = Depends(get_current_user)):
#     return {"message": "Welcome to the EmotionalDetector API"}
@app.get("/info/")
async def read_root():
    return {"message": "Welcome to the EmotionalDetector API"}


print(Config.EMOTION_MODEL)
@app.post("/label-selction/")
async def label_selection(emotion_model: EmotionModel):
    if emotion_model.model not in Config.EMOTIONS:
        raise HTTPException(status_code=404, detail="Model not found")
    
    Config.EMOTIN_MODEL = emotion_model.model 
    return {"message": f"Emotion model set to {Config.EMOTION_MODEL}"}


@app.post("/inference-openai/")
async def inference_openai(query: Query):
    cls = await get_inference_openai()

    response = cls._get_prediction(query.text,verbosity=True)
    
    return {
        "response":response.content,
        "labels-selection":Config.EMOTION_MODEL}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
