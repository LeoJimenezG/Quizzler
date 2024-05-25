from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizGUI

# Put all the questions objects in a List
# each object will have a text (question) and an answer
question_bank = []
for question in question_data:
    # Get the question from the data
    question_text = question["question"]
    # Get the answer from the data
    question_answer = question["correct_answer"]
    # Create a Question object with a text and an answer
    new_question = Question(question_text, question_answer)
    # Append it to the list
    question_bank.append(new_question)

# Create the QuizBrain object (all functionality)
quiz = QuizBrain(question_bank)
# Create the QuizGUI object (the Graphic User Interface)
quiz_gui = QuizGUI(quiz)
# Final messages
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
