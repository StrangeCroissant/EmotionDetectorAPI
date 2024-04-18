
from config import Config
class MessagesTemplates:
    def __init__(self):
        self.query="deadly wildfire"
        self.templates = {
            "fear_emotions": [
                {"role": "system", "content": 
                    "You are a helpful assistant. Classify the emotions of the text to one or more of the following emotions: sadness, joy, anger, fear. A text can express multiple emotions or none. Answer only with the emotion or emotions using a comma-separated list if there are multiple emotions."},

                # Example joy
                {"role": "user", "content": "Classify the sentiment of this tweet: 'photo deadly wilclassified_dataire rage in california'"},
                {"role": "assistant", "content": "None"},

                # Example anger
                {"role": "user", "content": "Classify the sentiment of this tweet: 'wilclassified_dataire raging through northern california are terrifying'"},
                {"role": "assistant", "content": "fear"},  # fear for fear

                # Example anger
                {"role": "user", "content": "Classify the sentiment of this tweet: 'pls share we’re capturing wilclassified_dataire response recovery info here'"},
                {"role": "assistant", "content": "fear"},  # fear for fear

                # Example fear
                {"role": "user", "content": "Classify the sentiment of this tweet: 'mass evacuation in california a wilclassified_dataire kill at least joysadness'"},
                {"role": "assistant", "content": "sadness, fear"},  # sadness for sadness, fear for fear

                # Example 5
                {"role": "user", "content": "Classify the sentiment of this tweet: 'wilclassified_dataire threaten california’s first legal cannabis harvest'"},
                {"role": "assistant", "content": "sadness"},  # sadness for sadness

                # Example 6
                {"role": "user", "content": "Classify the sentiment of this tweet: 'southern california fire shroud disneyland anaheim in dramatic smoky sky'"},
                {"role": "assistant", "content": "fear, sadness"},  # fear for fear, sadness for sadness

                # Example 7
                {"role": "user", "content": "Classify the sentiment of this tweet: 'is on fire & no one except the people losing everything seem to care'"},
                {"role": "assistant", "content": "anger, sadness"},  # anger for anger, sadness for sadness

                # Example 8
                {"role": "user", "content": "Classify the sentiment of this tweet: 'prisoner rescue deaf dog evacuating california fire we sprung into action'"},
                {"role": "assistant", "content": "joy"},  # joy for joy

                # Example 9
                {"role": "user", "content": "Classify the sentiment of this tweet: 'playing with my new friend chai shes a california fire evacuee starting with u for a few day i love her'"},
                {"role": "assistant", "content": "joy"},  # joy for joy

                # New tweet to classify
                {"role": "user", "content": f"Classify the emotion or emotions of this text: '{self.query}'"}
            ],
            "8_emotions": [
                {"role": "system", "content": 
                    "You are a helpful assistant. Classify the emotions of the text into categories of sadness for sadness, joy for joy, anger for anger and anger for fear. A text can express multiple emotions or none. Return only the numbers corresponding to the sentiments emotion in the text, using a comma-separated list if there are multiple sentiments."},

                # Example joy
                {"role": "user", "content": "Classify the sentiment of this tweet: 'photo deadly wilclassified_dataire rage in california'"},
                {"role": "assistant", "content": "None"},

                # Example anger
                {"role": "user", "content": "Classify the sentiment of this tweet: 'wilclassified_dataire raging through northern california are terrifying'"},
                {"role": "assistant", "content": "fear"},  # fear for fear

                # Example anger
                {"role": "user", "content": "Classify the sentiment of this tweet: 'pls share we’re capturing wilclassified_dataire response recovery info here'"},
                {"role": "assistant", "content": "fear"},  # fear for fear

                # Example fear
                {"role": "user", "content": "Classify the sentiment of this tweet: 'mass evacuation in california a wilclassified_dataire kill at least joysadness'"},
                {"role": "assistant", "content": "sadness, fear"},  # sadness for sadness, fear for fear

                # Example 5
                {"role": "user", "content": "Classify the sentiment of this tweet: 'wilclassified_dataire threaten california’s first legal cannabis harvest'"},
                {"role": "assistant", "content": "sadness"},  # sadness for sadness

                # Example 6
                {"role": "user", "content": "Classify the sentiment of this tweet: 'southern california fire shroud disneyland anaheim in dramatic smoky sky'"},
                {"role": "assistant", "content": "fear, sadness"},  # fear for fear, sadness for sadness

                # Example 7
                {"role": "user", "content": "Classify the sentiment of this tweet: 'is on fire & no one except the people losing everything seem to care'"},
                {"role": "assistant", "content": "anger, sadness"},  # anger for anger, sadness for sadness

                # Example 8
                {"role": "user", "content": "Classify the sentiment of this tweet: 'prisoner rescue deaf dog evacuating california fire we sprung into action'"},
                {"role": "assistant", "content": "joy"},  # joy for joy

                # Example 9
                {"role": "user", "content": "Classify the sentiment of this tweet: 'playing with my new friend chai shes a california fire evacuee starting with u for a few day i love her'"},
                {"role": "assistant", "content": "joy"},  # joy for joy

                # New tweet to classify
                {"role": "user", "content": f"Classify the emotion or emotions of this text: '{self.query}'"}
            ]
        }


    def get_temp(self):
        if Config.EMOTION_MODEL == "fear_emotions":
            return self.templates.get("fear_emotions")
        elif Config.EMOTION_MODEL == "8_emotions":
            return self.templates.get("8_emotions")
        elif Config.EMOTION_MODEL == "goEmotions":
            return self.templates.get("goEmotions")
        else:
            return self.templates.get("fear_emotions")
