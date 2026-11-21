import customtkinter as ctk

ctk.set_appearance_mode("dark")

PURPLE, PURPLE_DIM, BG, PANEL, FIELD, TEXT_MUTED = "#B57BFF", "#7A4FCC", "#120B1E", "#1D1330", "#2A1D45", "#9A8FB5"

class QuizApp:
    def __init__(self, master=None):
        self.app = master if master else ctk.CTk()
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.title("Quiz Game")
        self.app.configure(fg_color=BG)
        self.correct_option = "OPTION A"
        self.ui_question()

  

    def ui_question(self):
  
        
        self.container = ctk.CTkFrame(self.app, fg_color="transparent")
        self.container.pack(expand=True)

        self.question_box = ctk.CTkButton(self.container, text="QUIZ QUESTION 2", font=("Helvetica", 22, "bold"), fg_color="#D9D9D9", text_color="black", hover=False, width=440, height=160, corner_radius=8)
        self.question_box.pack(pady=(0, 15))

        self.options_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.options_frame.pack()

        options = [("OPTION A", 0, 0), ("OPTION B", 0, 1), ("OPTION C", 1, 0), ("OPTION D", 1, 1)]
        for text, row, col in options:
            btn = ctk.CTkButton(self.options_frame, text=text, font=("Helvetica", 14, "bold"), fg_color="black", hover_color=PURPLE_DIM, text_color="white", width=210, height=50, corner_radius=4, command=lambda t=text: self.check_answer(t))
            btn.grid(row=row, column=col, padx=8, pady=8)

    def check_answer(self, selected_option):
        if selected_option == self.correct_option:
            self.ui_correct()
        else:
            self.ui_wrong()

    def ui_correct(self):
       
        
        self.card = ctk.CTkFrame(self.app, fg_color=BG, width=460, height=320, corner_radius=12)
        self.card.pack(expand=True)

        self.msg_label = ctk.CTkLabel(self.card, text="You  Have Completed the\nQuestion successfully!\nHere Is your reward:", font=("Helvetica", 18, "bold"), text_color="white")
        self.msg_label.pack(pady=(40, 15))

        self.xp_label = ctk.CTkLabel(self.card, text="-- XP", font=("Helvetica", 16, "bold"), text_color="white")
        self.xp_label.pack(pady=(0, 15))

        self.dollar_btn = ctk.CTkButton(self.card, text="💲", font=("Helvetica", 28), fg_color="transparent", border_color="white", border_width=2, hover_color=FIELD, width=140, height=45, corner_radius=25, command=self.ui_question)
        self.dollar_btn.pack(pady=(0, 30))

    def ui_wrong(self):
        
        
        self.card = ctk.CTkFrame(self.app, fg_color="black", width=460, height=320, corner_radius=12)
        self.card.pack(expand=True)

        self.msg_label = ctk.CTkLabel(self.card, text="You  Have Not Completed\nthe Question successfully\nTry Again Next Time:", font=("Helvetica", 18, "bold"), text_color="white")
        self.msg_label.pack(pady=(40, 15))

        self.xp_label = ctk.CTkLabel(self.card, text="-- XP", font=("Helvetica", 16, "bold"), text_color="white")
        self.xp_label.pack(pady=(0, 15))

        self.sad_btn = ctk.CTkButton(self.card, text="🙁", font=("Helvetica", 36), fg_color="transparent", hover_color=FIELD, width=70, height=70, corner_radius=35, command=self.ui_question)
        self.sad_btn.pack(pady=(0, 30))

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()