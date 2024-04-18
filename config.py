import dotenv,os

dotenv.load_dotenv()

class Config:
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
    SECTER_KEY = os.getenv("SECTER_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))