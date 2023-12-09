from typing import Protocol

class Promptable(Protocol):
    def submitPrompt(self, prompt):
        pass