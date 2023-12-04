# Example: reuse your existing OpenAI setup
import openai

client = openai.OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")

# completion = client.chat.completions.create(model="local-model", messages=[
#   {"role": "system", "content": "Your task is to output valid JSON. You will need to select an API endpoint that is relevant to my prompt and output only valid JSON. The ONLY available API endpoints are the five endpoints below:\n/v1/accelerate\n/v1/brake\n/v1/turnLeft\n/v1/turnRight\nnot found\n\nIf no endpoint exists that is an adequate response to the prompt, reply with {\"endpoint\": \"not found\"}\n\nWhen you select one of the API endpoints, respond with valid JSON as in the response examples given below:\n\n# Example 1:\nUser: make the car brake\nResponse: {\"endpoint\": \"/v1/brake\"}\n\n# Example 2:\nUser: make the car go faster\nResponse: {\"endpoint\": \"/v1/accelerate\"}\n\n# Example 3:\nUser: make the car turn left\nResponse: {\"endpoint\": \"/v1/turnLeft\"}\n\n# Example 4:\nUser: stop\nResponse: {\"endpoint\": \"/v1/brake\"}\n\n# Example 5:\nUser: make a left\nResponse: {\"endpoint\": \"/v1/turnLeft\"}\n\n# Example 6:\nUser: go right\nResponse: {\"endpoint\": \"/v1/turnRight\"}\nYour response will be read and parsed automatically, so be sure to ONLY respond with valid JSON. Never respond with anything that is not valid JSON. The prompt to which you must respond with valid JSON is as follows:\n\n"},
#   {"role": "user", "content": "let's turn to the right here"}
#   ],
#   temperature=0
# )

# completion = client.chat.completions.create(model="local-model", messages=[    {"role": "system", "content": "You are a helpful assistant. Answer questions to the best of your abilities. Never give legal, financial, or medical advice."},    {"role": "user", "content": "Hello. How are you?"}  ],  temperature=0)

completion = client.chat.completions.create(model="local-model", messages=[    {"role": "system", "content": "You are a helpful coding assistant. Answer questions to the best of your abilities. Never give legal, financial, or medical advice."},    {"role": "user", "content": "Please write a python function that lets me record audio while the spacebar key is pressed and outputs the recording to a file named newsample.wav."}  ],  temperature=0)

print(completion.choices[0].message)

