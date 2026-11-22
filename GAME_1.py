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
        options_flipped = [
                    ("Ethernet: Indirect or setup-related cause. While Ethernet does not cause WiFi drops itself, plugging in a cable can disable the PC WiFi adapter or cause a fallback or conflict if the cable is loose or unplugged mid-session. In a quiz context, it represents the fix someone tries after WiFi keeps dropping.", 0, 0),
                    ("Many people on the phone: Bandwidth, router overload, or interference. If on the phone means people streaming video, gaming, or making WiFi or VoIP calls over the same network, heavy traffic and device congestion can strain an overloaded or older router, causing brief disconnects or timeouts. Standard cellular calls will not affect home WiFi.", 0, 1),
                    ("Router is too far: Weak or unstable wireless signal. As distance increases, especially through walls, floors, or appliances, the radio signal weakens and suffers more interference, causing packet loss and sudden WiFi dropouts.", 1, 0),
                    ("Network adapter problem: Hardware, driver, or power management drops. A loose or failing WiFi card or antenna, a buggy driver update, overheating, or operating system power-saving features that shut off the wireless radio can cause the PC to abruptly lose its WiFi connection.", 1, 1)
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
