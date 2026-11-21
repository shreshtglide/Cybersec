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
            text="A kid is playing games and his pc keeps losing wi-fi connection and is frustrated because he's at the final level and close to winning.",
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
            ("Ethernet", 0, 0),
            ("Multiple Devices Connected", 0, 1),
            ("Router Too Far", 1, 0),
            ("A Problem With The Network Adapter", 1, 1)
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
                
            )
       
            btn._text_label.configure(wraplength=230, justify="center")
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

  

    

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()
