# Example: reuse your existing OpenAI setup
import openai, systemMessages
from prompt import prompt
# use codellama instruct
client = openai.OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")

completion = client.chat.completions.create(
    model="local-model", 
    messages=[
        {
            "role": "system", 
            "content": systemMessages.messages["vehicleApi"]},
        {
            "role": "user", 
            "content": prompt
            }
    ],
    temperature=0
)

print(completion.choices[0].message)

