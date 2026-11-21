import customtkinter as ctk

ctk.set_appearance_mode("dark")

PURPLE, PURPLE_DIM, BG, PANEL, FIELD, TEXT_MUTED = "#B57BFF", "#7A4FCC", "#120B1E", "#1D1330", "#2A1D45", "#9A8FB5"

class Profile:
    def __init__(self, master=None):
        self.app = master if master else ctk.CTk()
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.title("Settings")
        self.app.configure(fg_color=BG)
        self.ui()

    def ui(self):
        self.app.grid_columnconfigure(0,weight=1)

        self.title_label = ctk.CTkButton(self.app, text="Profile Page", font=("Helvetica", 16, "bold"), fg_color=PANEL, text_color="white", hover=False, height=40, width=220)
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(30, 20))

        
        
        self.faces = ctk.CTkButton(self.app, text="Faces", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color=PANEL, width=280, height=42, corner_radius=8)
        self.faces.grid(row=1, column=0, columnspan=3, pady=(30, 20))
        
        
        self.bags = ctk.CTkButton(self.app, text="Bags", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color=PANEL, width=280, height=42, corner_radius=8)
        self.bags.grid(row=3, column=0, columnspan=3, pady=(30, 20))
        
        self.outfit = ctk.CTkButton(self.app, text="Outfits", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color=PANEL, width=280, height=42, corner_radius=8)
        self.outfit.grid(row=5, column=0, columnspan=3, pady=(30, 20))
        
        self.logout = ctk.CTkButton(self.app, text="Log Out", font=("Helvetica", 14, "bold"), fg_color=FIELD, hover_color=PANEL, width=280, height=42, corner_radius=8)
        self.logout.grid(row=7, column=0, columnspan=3, pady=(30, 20))
        
        
        
        self.back_btn = ctk.CTkButton(self.app, text="BACK", font=("Helvetica", 12, "bold"), fg_color=PANEL, hover_color=FIELD, width=80, height=35)
        self.back_btn.grid(row=8, column=0, columnspan=3, pady=(30, 20))
 
    def run(self):
      self.app.mainloop()


if __name__ == "__main__":
    profile= Profile()
    profile.run()