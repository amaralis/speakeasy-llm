from openai import OpenAI
from systemMessages import messages
from prompt import prompt
from configs import configs

# Codellama-instruct LLM has yielded the best results so far

client = OpenAI(base_url=configs["localUrl"], api_key="not-needed")

completion = client.chat.completions.create(
    model="local-model", 
    messages=[
        {
            "role": "system", 
            "content": messages["vehicleApi"]},
        {
            "role": "user", 
            "content": prompt
            }
    ],
    temperature=0
)

print(completion.choices[0].message)