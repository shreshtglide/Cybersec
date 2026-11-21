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
        self.correct_option = "B. Wi-Fi connects devices wirelessly, while Ethernet uses physical cables."
        self.ui_question()

    def clear_screen(self):
        for widget in self.app.winfo_children():
            widget.destroy()

    def ui_question(self):
        self.clear_screen()

        self.container = ctk.CTkFrame(self.app, fg_color="transparent")
        self.container.pack(expand=True)

       
        self.question_box = ctk.CTkButton(
            self.container,
            text="What is the main difference between Wi-Fi and Ethernet?",
            font=("Helvetica", 22, "bold"),
            fg_color="#D9D9D9",
            text_color="black",
            hover=False,
            width=536,
            height=150,
            corner_radius=8
        )
        self.question_box._text_label.configure(wraplength=480, justify="center")
        self.question_box.pack(pady=(0, 16))

        self.options_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.options_frame.pack(fill="x")

     
        self.options_frame.grid_columnconfigure((0, 1), weight=1, uniform="options_col")

        options = [
            ("A. Wi-Fi uses cables, while Ethernet uses radio waves.", 0, 0),
            ("B. Wi-Fi connects devices wirelessly, while Ethernet uses physical cables.", 0, 1),
            ("C. Wi-Fi is only used for phones, while Ethernet is only used for computers.", 1, 0),
            ("D. Wi-Fi and Ethernet are exactly the same.", 1, 1)
        ]

        for text, row, col in options:
            btn = ctk.CTkButton(
                self.options_frame,
                text=text,
                font=("Helvetica", 14, "bold"),
                fg_color="black",
                hover_color=PURPLE_DIM,
                text_color="white",
                width=260,
                height=75,
                corner_radius=6,
                command=lambda t=text: self.check_answer(t)
            )
       
            btn._text_label.configure(wraplength=230, justify="center")
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

    def check_answer(self, selected_option):
        if selected_option == self.correct_option:
            self.ui_correct()
        else:
            self.ui_wrong()

    def ui_correct(self):
        self.clear_screen()

        self.card = ctk.CTkFrame(self.app, fg_color=PANEL, width=460, height=320, corner_radius=12)
        self.card.pack_propagate(False)
        self.card.pack(expand=True)

        self.msg_label = ctk.CTkLabel(
            self.card,
            text="You Have Completed the\nQuestion successfully!\nHere is your reward:",
            font=("Helvetica", 18, "bold"),
            text_color="white"
        )
        self.msg_label.pack(pady=(45, 15))

        self.xp_label = ctk.CTkLabel(self.card, text="-- XP", font=("Helvetica", 16, "bold"), text_color=PURPLE)
        self.xp_label.pack(pady=(0, 20))

        self.dollar_btn = ctk.CTkButton(
            self.card,
            text="💲",
            font=("Helvetica", 28),
            fg_color="transparent",
            border_color="white",
            border_width=2,
            hover_color=FIELD,
            width=140,
            height=45,
            corner_radius=25,
            command=self.ui_question
        )
        self.dollar_btn.pack(pady=(0, 30))

    def ui_wrong(self):
        self.clear_screen()

        self.card = ctk.CTkFrame(self.app, fg_color="black", width=460, height=320, corner_radius=12)
        self.card.pack_propagate(False)
        self.card.pack(expand=True)

        self.msg_label = ctk.CTkLabel(
            self.card,
            text="You Have Not Completed\nthe Question successfully\nTry Again Next Time:",
            font=("Helvetica", 18, "bold"),
            text_color="white"
        )
        self.msg_label.pack(pady=(45, 15))

        self.xp_label = ctk.CTkLabel(self.card, text="-- XP", font=("Helvetica", 16, "bold"), text_color=TEXT_MUTED)
        self.xp_label.pack(pady=(0, 20))

        self.sad_btn = ctk.CTkButton(
            self.card,
            text="🙁",
            font=("Helvetica", 36),
            fg_color="transparent",
            hover_color=FIELD,
            width=70,
            height=70,
            corner_radius=35,
            command=self.ui_question
        )
        self.sad_btn.pack(pady=(0, 30))

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()