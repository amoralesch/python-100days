class QuizBrain:
    def __init__(self, questions):
        self.index = 0
        self.score = 0
        self.questions = questions
        self.last_question = None

    def has_more_questions(self):
        return len(self.questions) > self.index

    def next_question(self):
        self.last_question = self.questions[self.index]
        self.index += 1

        return self.last_question

    def answer(self, answer):
        good_answer = self.last_question.answer.lower()

        if good_answer == answer:
            self.score += 1
            print('You got it right!')
        else:
            print(f"That's incorrect, the correct answer was {good_answer}")

        print()

    def total_questions(self):
        return len(self.questions)
