# html is for escape or unescape certain symbol codes
import html


class QuizBrain:
    # Constructor
    def __init__(self, q_list):
        # Basic information to use
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Method to check if there are remaining questions
    def still_has_questions(self):
        # Compare the amount of questions passed and the total of questions
        return self.question_number < len(self.question_list)

    # Method to get the next question of the list
    def next_question(self):
        # The question number will indicate the current question
        self.current_question = self.question_list[self.question_number]
        # We got the next question, add one to the question number
        self.question_number += 1
        # Unescape all the symbol codes in the question gotten from the API
        question_text = html.unescape(self.current_question.text)
        # Return the text
        return f"Q.{self.question_number}: {question_text} (True/False)"

    # Method to check the user's answer and the correct answer
    def check_answer(self, user_answer):
        # Get the answer of the current question
        correct_answer = self.current_question.answer
        # Compare answers converted into lowercase
        if user_answer.lower() == correct_answer.lower():
            # If the user's answer is correct, add one to the score
            self.score += 1
            # Indicate the user answered correctly
            return True
        else:
            # Indicate the user answered incorrectly
            return False
