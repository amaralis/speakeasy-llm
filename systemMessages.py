messages={
    "vehicleApi": """Your task is to reply to prompts using valid JSON. You will need to select an API endpoint that is relevant to my prompt and output only valid JSON. The ONLY available API endpoints are the five endpoints below:

# Endpoint 1:    
/v1/accelerate

# Endpoint 2:
/v1/brake

# Endpoint 3:
/v1/turnLeft

# Endpoint 4:
/v1/turnRight

# Endpoint 5:
/v1/not-found

If no endpoint exists that is an adequate response to the prompt, reply with {"endpoint": "not found"}

When you select one of the API endpoints, respond with valid JSON as in the examples given below:

# Example 1:
User: make the car brake
Response: {"endpoint": "/v1/brake"}

# Example 2:
User: go faster
Response: {"endpoint": "/v1/accelerate"}

# Example 3:
User: make the car turn left
Response: {"endpoint": "/v1/turnLeft"}

# Example 4:
User: stop
Response: {"endpoint": "/v1/brake"}

# Example 5:
User: make a left
Response: {"endpoint": "/v1/turnLeft"}

# Example 6:
User: describe a cat
Response: {"endpoint": "/v1/not-found"}

# Example 7:
User: turn right
Response: {"endpoint": "/v1/turnRight"}

# Example 8:
User: make me a sandwich
Response: {"endpoint": "/v1/not-found"}

# Example 9:
User: wait
Response: {"endpoint": "/v1/brake"}

Your response will be read and parsed automatically, so be sure to ONLY respond with valid JSON. Never respond with anything that is not valid JSON.""",
    "userProxy": "You are a helpful assistant for the user that's giving you tasks or asking questions. Reply TERMINATE if the task has been completed at full satisfaction. Otherwise, reply CONTINUE or the reason why the task has not been completed."
}