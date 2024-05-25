from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGUI:
    # Constructor
    def __init__(self, quiz_brain: QuizBrain):
        # --- Create all the interface ---
        # Get the Quiz Functionality
        self.quiz = quiz_brain
        # Basic configurations
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.window.resizable(width=False, height=False)
        # Upper score label
        self.text_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
        self.text_score.grid(row=0, column=1, sticky="nsew")
        # Main canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_canvas = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"),
                                                   fill="black", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, command=self.true_answer, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, command=self.false_answer, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        # Show the first question
        self.get_question()
        # Maintain the window
        self.window.mainloop()

    # Method to get the next question
    def get_question(self):
        # It means we change the showing question
        self.canvas.config(bg="white")
        # Check if there are questions left
        if self.quiz.still_has_questions():
            # Show the score
            self.text_score.config(text=f"Score: {self.quiz.score}")
            # Get the next question
            q_text = self.quiz.next_question()
            # Show the next question
            self.canvas.itemconfig(self.text_canvas, text=q_text)
        # If there are no questions left
        else:
            # Indicate it to the user
            self.canvas.itemconfig(self.text_canvas, text="There are no more questions")
            # Disable the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Method for the True Button
    def true_answer(self):
        # Check the answer
        result = self.quiz.check_answer("True")
        # Indicate the result to the user
        self.give_response(result)

    # Method for the False Button
    def false_answer(self):
        # Check the answer
        result = self.quiz.check_answer("False")
        # Indicate the result to the user
        self.give_response(result)

    # Method to indicate to the user if they answered correctly or not
    def give_response(self, result):
        # It is correct
        if result:
            # Change background color to green
            self.canvas.config(bg="green")
        # It is wrong
        else:
            # Change background color to red
            self.canvas.config(bg="red")
        # Wait milliseconds and change to the question
        self.window.after(900, func=self.get_question)
