
import customtkinter as ctk
import re 
import sys
from tkinter import messagebox

user_re=re.compile(r"^[a-zA-Z0-9@_]{4,6}$")
pwd_re = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
    r"(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*_]{6,10}$"
)
ctk.set_appearance_mode("dark")
PURPLE="#B57BFF"
PURPLE_DIM="#7A4FCC"
BG="#120B1E"
PANEL="#1D1330"
FIELD="#2A1D45"
TEXT_MUTED="#9A8FB5"

class Login_app:
    def __init__(self):
        self.app=ctk.CTk()
        self.app.title("Login")
        self.app.geometry("900x560")
        self.app.minsize(700,460)
        self.app.configure(fg_color=BG)
        self.app.grid_columnconfigure(0,weight=1)
        self.app.grid_columnconfigure(1,weight=1)
        self.app.grid_rowconfigure(0,weight=1)
        self.ui()
    def ui(self):
        self.left=ctk.CTkFrame(self.app,fg_color=PANEL,corner_radius=16)
        self.left.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
        try:
            from PIL import Image
            img=ctk.CTkImage(Image.open("Banner.jpg"),size=(380,320))
            img_label=ctk.CTkLabel(self.left,text="",image=img)
            img_label.place(relx=0.5,rely=0.5,anchor="center")

        except:
            img_label=ctk.CTkLabel(self.left,text="image",text_color=TEXT_MUTED,font=("Arial",20))
            img_label.place(relx=0.5,rely=0.5,anchor="center")

        self.right=ctk.CTkFrame(self.app,fg_color="transparent")
        self.right.grid(row=0,column=1,sticky="nsew",padx=(15,40),pady=30)
        self.form=ctk.CTkFrame(self.right,fg_color="transparent")
        self.form.place(relx=0.5,rely=0.5,anchor="center")

        self.hello_label=ctk.CTkLabel(self.form,text="Hello!",font=("Helvetica",26,"bold"), text_color="white")
        self.hello_label.pack(anchor="w")

        self.wlcm_label=ctk.CTkLabel(self.form,text="Welcome Back",font=("Helvetica",34,"bold"), text_color=PURPLE)
        self.wlcm_label.pack(anchor="w",pady=(0,10))


        self.register_frame = ctk.CTkFrame(self.form, fg_color="transparent")
        self.register_frame.pack(anchor="w", pady=(0, 10))
        
        self.dont_label=ctk.CTkLabel(self.register_frame,text="Don't have an account?",font=("Helvetica",16),text_color=TEXT_MUTED)
        self.dont_label.pack(side="left")
        
        self.register_btn=ctk.CTkButton(self.register_frame,text="Register",font=("Helvetica",16,"underline"), text_color=TEXT_MUTED,fg_color="transparent")
        self.register_btn.pack(padx=5,side="left")

        self.user_entry=ctk.CTkEntry(self.form,placeholder_text="User ID",width=380,height=45,fg_color=FIELD,corner_radius=8)
        self.user_entry.pack(pady=8)

        self.pwd_frame=ctk.CTkFrame(self.form,fg_color="transparent")
        self.pwd_frame.pack(pady=8)
        self.pwd_visible={"on":False}
        self.pwd_entry=ctk.CTkEntry(self.pwd_frame,placeholder_text="Password",width=380,height=45,fg_color=FIELD,corner_radius=8,show="*")
        self.pwd_entry.pack(pady=8)

        self.eye_btn= ctk.CTkButton(self.pwd_frame, text="👓",width=30,height=30, fg_color='transparent',hover_color=FIELD,command=self.toggle_pwd)
        self.eye_btn.place(relx=0.9,rely=0.5,anchor="e")
        
        self.error_label=ctk.CTkLabel(self.form,text="",text_color="#E44949", font=("Helvetica",12) )
        self.error_label.pack(pady=(4,0))
        self.login_btn=ctk.CTkButton(self.form,width=380,height=50,text="LOGIN",text_color="#FFFFFF",font=("Helvetica",16,"bold"),fg_color=PURPLE,corner_radius=10,hover_color=PURPLE_DIM,command=self.error_check)
        self.login_btn.pack(pady=(20,0))
    def toggle_pwd(self):
        self.pwd_visible["on"]= not self.pwd_visible["on"]
        self.pwd_entry.configure(show="" if self.pwd_visible["on"] else "*")
        self.eye_btn.configure(text="🕶️"  if self.pwd_visible["on"] else "👓")

    def error_check(self):
        self.userid=self.user_entry.get().strip()
        self.pwd=self.pwd_entry.get().strip()
        if not self.userid or not self.pwd:
            #self.error_label.configure(text="Please enter the details")
            messagebox.showerror("Details","Please enter the details")
         

        elif not user_re.match(self.userid):
            #self.error_label.configure(text="Username: 4-20 Letters, Numbers or _ / @ only")
            messagebox.showerror("Username","Username: 4-6 Letters, Numbers or _ / @ only") 

        elif not pwd_re.match(self.pwd):
            #self.error_label.configure(text="Password: 6-10 Characters, with a capital alphabet, small alphabet, number and special character") 
            messagebox.showerror("Password","Password: 6-10 Characters, with a capital alphabet, small alphabet, number and special character")


    def run(self):
        self.app.mainloop()

loginobj = Login_app()
loginobj.run()
