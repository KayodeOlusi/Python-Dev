# Quiz using class

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is my age?\n(a) 23\n(b) 13\n(c) 54\n\n",
    "What is my job?\n(a) Painter\n(b) Brick\n(c) Python\n\n",
    "What is my name?\n(a) George\n(b) Yoki\n(c) Spear\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)

        if answer == question.answer:
            score += 1
    print("Score is" + str(score))

print(run_test(questions))