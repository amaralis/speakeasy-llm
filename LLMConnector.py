from protocols.promptable import Promptable
    
class LLMConnector:
    promptable: Promptable

    def __init__(self, promptable: Promptable):
        self.promptable = promptable

    def sendPrompt(self, promptable: Promptable, prompt):
        return promptable.submitPrompt(prompt)