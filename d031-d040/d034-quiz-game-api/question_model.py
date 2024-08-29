import html


class Question:
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer

    def prompt(self) -> str:
        return html.unescape(self.text)
