# About

Personal project for natural speech with Large Language Models. Will possibly update it as the open source technology evolves and the capabilities of local LLMs improve.

# Requirements
## Python >=3.9 && <3.12
## LM Studio

LM Studio is an application that lets you download LLMs and prompt them via local server, using an API similar to that of OpenAI. Works completely offline, no connection to the exterior. Get it at [https://lmstudio.ai](https://lmstudio.ai). I suggest the Llama-2-7B model to get started.

## Chocolatey (for Windows)

`pip install ffmpeg-python`

# How to use

1. Install LM Studio
2. Select the server tab `<->` and use port `8080` for talking to the LLM. If you need to use another port, change the `base_url` in `llms/LMStudio` accordingly.
3. Create virtual environment
    Currently, advised method is to use venv. Documentation for VS Code [here](https://code.visualstudio.com/docs/python/environments)
4. Install and upgrade wheel: `pip install --upgrade wheel`
5. Install ffmpeg: `pip install ffmpeg-python`
6. [Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 
7. Install dependencies: `$ pip install -r requirements.txt`
8. Import the `startPrompting()` function from `speakeasyLlm.py`
    `from speakeasy import startPrompting`
9. Press space bar to start recording your message, and again to stop recording. Wait for the LLM's response.

### Customization

If you want to use a different LLM API or method of communication with the model, you need to have a class that implements the `Promptable` Protocol.

1. `from protocols.promptable import Promptable`
2. Define the method `submitPrompt(prompt)`, where `prompt` is the string that will be sent to the LLM. ***This method must also return the LLM's response as a string.***
