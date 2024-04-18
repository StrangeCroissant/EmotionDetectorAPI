import dotenv,os

dotenv.load_dotenv()

class Config:
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    EMOTION_MODEL = os.getenv("EMOTION_MODEL")
    EMOTIONS = {
        "4_emotions": ["happy", "sad", "angry", "neutral"],
        "8_emotions": ["happy", "sad", "angry", "neutral", "surprised", "scared", "disgusted", "contempt"],
        "goEmotions": [
            "admiration",
            "amusement",
            "anger",
            "annoyance",
            "approval",
            "caring",
            "confusion",
            "curiosity",
            "desire",
            "disappointment",
            "disapproval",
            "disgust",
            "embarrassment",
            "excitement",
            "fear",
            "gratitude",
            "grief",
            "joy",
            "love",
            "nervousness",
            "optimism",
            "pride",
            "realization",
            "relief",
            "remorse",
            "sadness",
            "surprise",
            "neutral"
        ]
    }