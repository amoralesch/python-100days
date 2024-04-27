class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def prompt(self):
        return self.text
