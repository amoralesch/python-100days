from question_model import Question


class QuizBrain:
    def __init__(self, questions):
        self.index = 0
        self.score = 0
        self.questions = questions
        self.last_question = None

    def has_more_questions(self) -> bool:
        return len(self.questions) > self.index

    def next_question(self) -> Question:
        self.last_question = self.questions[self.index]
        self.index += 1

        return self.last_question

    def answer(self, answer: str) -> bool:
        good_answer = self.last_question.answer.lower()

        if good_answer == answer:
            self.score += 1

            return True
        else:
            return False

    def total_questions(self) -> int:
        return len(self.questions)
