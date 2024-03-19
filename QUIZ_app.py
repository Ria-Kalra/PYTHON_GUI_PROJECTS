import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "correct_answer": 0
            },
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Bronte", "Charlotte Bronte", "Louisa May Alcott"],
                "correct_answer": 0
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": ["Ag", "Au", "Cu", "Fe"],
                "correct_answer": 1
            },
        ]
        self.current_question_index = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.geometry("400x300")

        self.question_label = tk.Label(self.window, text="", font=("Helvetica", 14, "bold"), wraplength=300)
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = ttk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question_button = ttk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.pack(pady=10)

        # Add some color and animation to the buttons
        self.apply_button_styles()

    def apply_button_styles(self):
        # Define a color scheme
        background_color = "#4CAF50"  # Green
        hover_color = "#45a049"  # Darker Green
        text_color = "white"

        # Apply styles to the option buttons
        for button in self.option_buttons:
            button.configure(style="TButton", background=background_color, foreground=text_color)
            button.bind("<Enter>", lambda event, h=button: h.configure(background=hover_color))
            button.bind("<Leave>", lambda event, h=button: h.configure(background=background_color))

        # Apply styles to the "Next Question" button
        self.next_question_button.configure(style="TButton", background=background_color, foreground=text_color)
        self.next_question_button.bind("<Enter>", lambda event, h=self.next_question_button: h.configure(background=hover_color))
        self.next_question_button.bind("<Leave>", lambda event, h=self.next_question_button: h.configure(background=background_color))

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]
        if selected_option == correct_answer_index:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect!")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)}")
            self.window.quit()
        else:
            self.load_question()
            self.apply_button_styles()

quiz_app = QuizApp()
quiz_app.start_quiz()
