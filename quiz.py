#QUIZ APPLICATIONS
#@CODEAPLHA

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_answer):
        new_question = Question(question, options, correct_answer)
        self.questions.append(new_question)

    def take_quiz(self):
        for question in self.questions:
            print(question.question)
            for index, option in enumerate(question.options, start=1):
                print(f"{index}. {option}")

            user_answer = input("Enter the number of your answer: ")
            if user_answer.isnumeric():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.options):
                    user_answer -= 1  # Adjust for 0-based index
                    if question.is_correct(user_answer):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print(f"Wrong. The correct answer was {question.correct_answer + 1}.\n")
                else:
                    print("Invalid input. Please select a valid option.\n")
            else:
                print("Invalid input. Please enter a number.\n")

    def display_score(self):
        total_questions = len(self.questions)
        print(f"Your score: {self.score}/{total_questions}")

if __name__ == "__main__":
    quiz = Quiz()

    # Add questions to the quiz
    quiz.add_question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 2)
    quiz.add_question("What is 7 * 8?", ["42", "56", "64", "72"], 1)
    quiz.add_question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 1)

    # Take the quiz
    print("Welcome to the Quiz Application!")
    quiz.take_quiz()

    # Display the final score
    quiz.display_score()




