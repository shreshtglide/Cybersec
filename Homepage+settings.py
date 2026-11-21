
import customtkinter as ctk

ctk.set_appearance_mode("dark")

PURPLE, PURPLE_DIM, BG, PANEL, FIELD, TEXT_MUTED = "#B57BFF", "#7A4FCC", "#120B1E", "#1D1330", "#2A1D45", "#9A8FB5"

class HomepageApp:
    def __init__(self, master=None):
        self.app = master if master else ctk.CTk()
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.title("Homepage")
        self.app.configure(fg_color=BG)
        self.ui()

    def ui(self):
        self.header = ctk.CTkFrame(self.app, fg_color="transparent")
        self.header.pack(fill="x", padx=30, pady=(20, 10))

        self.title_btn = ctk.CTkButton(self.header, text="HOME PAGE", font=("Helvetica", 16, "bold"), fg_color=PANEL, text_color="white", hover=False, height=40, width=200)
        self.title_btn.pack(side="left", expand=True, anchor="center")

        self.icon_frame = ctk.CTkFrame(self.header, fg_color="transparent")
        self.icon_frame.pack(side="right")

        self.settings_btn = ctk.CTkButton(self.icon_frame, text="⚙️", width=40, height=40, fg_color=PANEL, hover_color=FIELD, font=("Helvetica", 18))
        self.settings_btn.pack(side="left", padx=5)

        self.profile_btn = ctk.CTkButton(self.icon_frame, text="👤", width=40, height=40, fg_color=PANEL, hover_color=FIELD, font=("Helvetica", 18))
        self.profile_btn.pack(side="left", padx=5)

        self.content = ctk.CTkFrame(self.app, fg_color="transparent")
        self.content.pack(expand=True, fill="both", padx=40, pady=20)

        self.explore_btn = ctk.CTkButton(self.content, text="Explore More", font=("Helvetica", 14, "bold"), fg_color=FIELD, text_color="white", hover_color=PURPLE_DIM, height=45, width=180)
        self.explore_btn.pack(pady=(10, 30))

        self.levels_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.levels_frame.pack(pady=20)

        for i in range(1, 5):
            btn = ctk.CTkButton(self.levels_frame, text=f"LEVEL {i}", font=("Helvetica", 14, "bold"), fg_color=PANEL, hover_color=PURPLE_DIM, width=130, height=50, corner_radius=8)
            btn.grid(row=0, column=i-1, padx=12, pady=10)

        self.quiz_btn = ctk.CTkButton(self.content, text="FINAL QUIZ", font=("Helvetica", 20, "bold"), fg_color=PURPLE, hover_color=PURPLE_DIM, text_color="white", width=320, height=60, corner_radius=10)
        self.quiz_btn.pack(pady=(30, 10))


    def run(self):
        self.app.mainloop()


class SettingsApp:
    def __init__(self, master=None):
        self.app = master if master else ctk.CTk()
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.title("Settings")
        self.app.configure(fg_color=BG)
        self.ui()

    def ui(self):
        self.title_label = ctk.CTkButton(self.app, text="SETTINGS", font=("Helvetica", 16, "bold"), fg_color=PANEL, text_color="white", hover=False, height=40, width=220)
        self.title_label.pack(pady=(30, 20))

        self.form = ctk.CTkFrame(self.app, fg_color="transparent")
        self.form.pack(expand=True)

        self.bg_music_frame = ctk.CTkFrame(self.form, fg_color="transparent")
        self.bg_music_frame.pack(pady=12)

        self.music_label = ctk.CTkLabel(self.bg_music_frame, text="Background Music", font=("Helvetica", 14, "bold"), text_color="white", width=180, anchor="w")
        self.music_label.pack(side="left", padx=10)

        self.music_switch = ctk.CTkSwitch(self.bg_music_frame, text="", progress_color=PURPLE, button_color="white", button_hover_color=TEXT_MUTED)
        self.music_switch.pack(side="left")

        self.dark_mode_frame = ctk.CTkFrame(self.form, fg_color="transparent")
        self.dark_mode_frame.pack(pady=12)

        self.dark_label = ctk.CTkLabel(self.dark_mode_frame, text="Dark Mode", font=("Helvetica", 14, "bold"), text_color="white", width=180, anchor="w")
        self.dark_label.pack(side="left", padx=10)

        self.dark_switch = ctk.CTkSwitch(self.dark_mode_frame, text="", progress_color=PURPLE, button_color="white", button_hover_color=TEXT_MUTED, )
        self.dark_switch.select()
        self.dark_switch.pack(side="left")

        self.privacy_btn = ctk.CTkButton(self.form, text="Privacy Policy", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color=PANEL, width=280, height=42, corner_radius=8)
        self.privacy_btn.pack(pady=12)

        self.logout_btn = ctk.CTkButton(self.form, text="Log Out", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color="#E44949", width=280, height=42, corner_radius=8)
        self.logout_btn.pack(pady=12)

        self.back_btn = ctk.CTkButton(self.app, text="BACK", font=("Helvetica", 12, "bold"), fg_color=PANEL, hover_color=FIELD, width=80, height=35)
        self.back_btn.pack(side="bottom", anchor="w", padx=30, pady=30)

    def toggle_theme(self):
        ctk.set_appearance_mode("dark" if self.dark_switch.get() == 1 else "light")

 
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    home = HomepageApp()
    home.run()
    settings= SettingsApp()
    settings.run()
