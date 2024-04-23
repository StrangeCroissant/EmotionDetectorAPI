import pandas as pd 
import os,openai
from openai import OpenAI
from config import Config 
from helpers.templates import MessagesTemplates

class GPTClasifier:
    def __init__(self,api_key,emotion_model=Config.EMOTION_MODEL):
        self.model_name = os.getenv("OPENAI_MODEL_NAME")
        self.emotion_model = emotion_model
        self.client = openai.OpenAI(api_key=api_key)

    def _set_emotions(self):
        """
        Select clasification labels 

        """

        pass
    

    def _start_instance(self):
        
        # get template based on emotion selection
        templates = MessagesTemplates()
        messages = templates.get_temp()
        # log model and emotion model
        print(f"Model {self.model_name} paired with {Config.EMOTION_MODEL}")
        return messages 


    def _get_prediction(self,query,verbosity=False):

        messages = self._start_instance()

        messages[-1] = {"role": "user", "content": f"Classify the sentiment of this tweet: '{query}'"}

        # Call the Chat Completions API with the updated messages
        response = self.client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
            temperature=0.1,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1.15
        )
        
        if verbosity:
            print(response)
        clasification_results = response.choices[0].message 
        return clasification_results
