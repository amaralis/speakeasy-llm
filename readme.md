# About

Personal project for natural speech with Large Language Models. Will possibly update it as the open source technology evolves and the capabilities of local LLMs improve.

# Requirements
- Python >=3.9 && <3.12
- LM Studio

LM Studio is an application that lets you download LLMs and prompt them via local server, using an API similar to that of OpenAI. Works completely offline, no connection to the exterior. Get it at [https://lmstudio.ai](https://lmstudio.ai). I suggest the Llama-2-7B model to get started.

- Windows (tested on Windows 10)

# How to use

1. Install LM Studio
2. Select the server tab `<->` and use port `8080` for talking to the LLM. If you need to use another port, change the `base_url` in `llms/LMStudio` accordingly.
3. [Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
4. Change directory into the cloned one
5. Create virtual environment (if on VS Code, tick the option to install requirements and skip step 7)
    Currently, advised method is to use venv. Documentation for VS Code [here](https://code.visualstudio.com/docs/python/environments)
7. Install dependencies: `$ pip install -r requirements.txt`
8. Import the `startPrompting()` function from `speakeasyLlm.py`
    `from speakeasy import startPrompting`
9. Call the `startPrompting()` function with the prompt string as argument
10. Press space bar to start recording your message, and again to stop recording. Wait for the LLM's response.

## In case of errors, exceptions or other shenanigans

1. Clone the repository again
2. Change directory into the cloned folder
3. Install `wheel`: `pip install --upgrade wheel`
4. Install `ffmpeg-python`: `pip install ffmpeg-python`
5. Create virtual environment
6. Install dependencies, making sure nothing is cached and everything is redownloaded: `pip install --no-cache-dir --ignore-installed -r requirements.txt`
7. Import the `startPrompting()` function from `speakeasyLlm.py`
    `from speakeasy import startPrompting`
8. Call the `startPrompting()` function with the prompt string as argument
9. Press space bar to start recording your message, and again to stop recording. Wait for the LLM's response.

# Customization

If you want to use a different LLM API or method of communication with the model, you need to have a class that implements the `Promptable` Protocol.

1. `from protocols.promptable import Promptable`
2. Define the method `submitPrompt(prompt)`, where `prompt` is the string that will be sent to the LLM. ***This method must also return the LLM's response as a string.***
