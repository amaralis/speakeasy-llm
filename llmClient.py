from openai import OpenAI
from systemMessages import messages
from configs import configs

def submitPrompt(prompt="Reply with 'There must be a bug in your code. I didn't get any prompt.'"):
    
    # Tested with Llama 2 7B q5_0 ggml by TheBloke using LM Studio with "Default LM Studio Windows" config

    client = OpenAI(base_url=configs["localUrl"], api_key="not-needed")

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
    print("Type: ", type(completion.choices[0].message.content))
    return completion.choices[0].message.content