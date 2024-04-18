import pandas as pd 
import os,openai
from openai import OpenAI



class GPTClasifier:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("OPENAI_MODEL_NAME")
        

    def _start_instance(self):
        pass

    def _get_prediction(self,query):
        pass