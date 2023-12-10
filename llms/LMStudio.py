from openai import OpenAI
from utils.systemMessages import messages

class LMStudio:
    prompt: str
    
    def submitPrompt(self, prompt="Reply with 'There must be a bug in your code. I didn't get any prompt.'"):
    
    # Tested with Llama 2 7B q5_0 ggml by TheBloke using LM Studio with "Default LM Studio Windows" config

        client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")

        completion = client.chat.completions.create(
            model="local-model", 
            messages=[
                {
                    "role": "system",
                    "content": messages["basicAssistant"]
                    },
                {
                    "role": "user", 
                    "content": prompt
                    }
            ],
            temperature=0
        )

        print("Message from LLM: ", completion.choices[0].message.content)
        
        return completion.choices[0].message.content
        