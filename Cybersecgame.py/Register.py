import customtkinter as ctk
import re 
import sys

user_re=re.compile(r"^[a-zA-Z0-9@_]{4,6}$")
pwd_re=re.compile(r"^(?=.{6,10}$)[a-z]+[A-Z]+[0-9]+[!@#$%^&*]+$")
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
        self.register_btn=ctk.CTkButton(self.register_frame,text="Register",font=("Helvetica",16,"underline"), text_color=TEXT_MUTED)
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
            self.error_label.configure(text="Please enter the detai")
        


    def run(self):
        self.app.mainloop()




class Register_app:

    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Register")
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.configure(fg_color=BG)

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_rowconfigure(0, weight=1)

        self.ui()

    def ui(self):

        self.left = ctk.CTkFrame(self.app, fg_color=PANEL, corner_radius=16)
        self.left.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)

        try:
            from PIL import Image

            img = ctk.CTkImage(Image.open("Banner.jpg"), size=(380, 320))
            img_label = ctk.CTkLabel(self.left, text="", image=img)
            img_label.place(relx=0.5, rely=0.5, anchor="center")

        except Exception:
            img_label = ctk.CTkLabel(self.left, text="image", text_color=TEXT_MUTED, font=("Arial", 20))
            img_label.place(relx=0.5, rely=0.5, anchor="center")

        self.right = ctk.CTkFrame(self.app, fg_color="transparent")
        self.right.grid(row=0, column=1, sticky="nsew", padx=(15, 40), pady=30)

        self.right.grid_columnconfigure(0, weight=1)
        self.right.grid_rowconfigure(0, weight=1)

        self.form = ctk.CTkFrame(self.right, fg_color="transparent")
        self.form.grid(row=0, column=0)

        self.form.grid_columnconfigure(0, weight=1)
        self.form.grid_columnconfigure(1, weight=1)

        self.signin_label = ctk.CTkLabel(self.form, text="Sign In", font=("Helvetica", 12, "bold"), text_color="white")
        self.signin_label.grid(row=0, column=0, sticky="e", padx=(0, 20), pady=(0, 20))

        self.register2_label = ctk.CTkLabel(self.form, text="Register", font=("Helvetica", 12, "bold", "underline"), text_color=PURPLE)
        self.register2_label.grid(row=0, column=1, sticky="w", padx=(20, 0), pady=(0, 20))

        self.dont_label = ctk.CTkLabel(self.form, text="REGISTER NOW", font=("Helvetica", 32, "bold"), text_color="white")
        self.dont_label.grid(row=1, column=0, columnspan=2, pady=(0, 35))

        self.name_entry = ctk.CTkEntry(self.form, placeholder_text="Name", width=190, height=45, fg_color=FIELD, corner_radius=8)
        self.name_entry.grid(row=2, column=0, padx=(0, 10), pady=8)

        self.email_entry = ctk.CTkEntry(self.form, placeholder_text="Email ID", width=190, height=45, fg_color=FIELD, corner_radius=8)
        self.email_entry.grid(row=2, column=1, padx=(10, 0), pady=8)

        self.user_entry = ctk.CTkEntry(self.form, placeholder_text="User ID", width=190, height=45, fg_color=FIELD, corner_radius=8)
        self.user_entry.grid(row=3, column=0, padx=(0, 10), pady=8)

        self.DOB_entry = ctk.CTkEntry(self.form, placeholder_text="Date Of Birth", width=190, height=45, fg_color=FIELD, corner_radius=8)
        self.DOB_entry.grid(row=3, column=1, padx=(10, 0), pady=8)

      

        self.pwd_frame = ctk.CTkFrame(self.form, fg_color="transparent")
        self.pwd_frame.grid(row=4, column=0, padx=(0, 10), pady=8)

        self.pwd_visible = {"on": False}

        self.pwd_entry = ctk.CTkEntry(self.pwd_frame, placeholder_text="Password", width=190, height=45, fg_color=FIELD, corner_radius=8, show="*")
        self.pwd_entry.grid(row=0, column=0)

        self.eye_btn = ctk.CTkButton(self.pwd_frame, text="👓", width=30, height=30, fg_color="transparent", hover_color=FIELD, command=self.toggle_pwd)
        self.eye_btn.place(relx=0.9, rely=0.5, anchor="e")

        self.cnfmpwd_frame = ctk.CTkFrame(self.form, fg_color="transparent")
        self.cnfmpwd_frame.grid(row=4, column=1, padx=(10, 0), pady=8)

        self.cnfmpwd_visible = {"on": False}

        self.cnfmpwd_entry = ctk.CTkEntry(self.cnfmpwd_frame, placeholder_text="Confirm Password", width=190, height=45, fg_color=FIELD, corner_radius=8, show="*")
        self.cnfmpwd_entry.grid(row=0, column=0)

        self.eyecnfm_btn = ctk.CTkButton(self.cnfmpwd_frame, text="👓", width=30, height=30, fg_color="transparent", hover_color=FIELD, command=self.toggle_pwd2)
        self.eyecnfm_btn.place(relx=0.9, rely=0.5, anchor="e")


        self.error_label = ctk.CTkLabel(self.form, text="", text_color="#E44949", font=("Helvetica", 12))
        self.error_label.grid(row=5, column=0, columnspan=2, pady=(4, 0))

   
        self.register_btn = ctk.CTkButton(self.form, text="Register", width=220, height=50, font=("Helvetica", 16, "bold"), fg_color=PURPLE, hover_color=PURPLE_DIM, corner_radius=10, command=self.error_check)
        self.register_btn.grid(row=6, column=0, columnspan=2, pady=(20, 0))


    def toggle_pwd(self):
        self.pwd_visible["on"] = not self.pwd_visible["on"]

        if self.pwd_visible["on"]:
            self.pwd_entry.configure(show="")
            self.eye_btn.configure(text="🕶️")
        else:
            self.pwd_entry.configure(show="*")
            self.eye_btn.configure(text="👓")

    def toggle_pwd2(self):
        self.cnfmpwd_visible["on"] = not self.cnfmpwd_visible["on"]

        if self.cnfmpwd_visible["on"]:
            self.cnfmpwd_entry.configure(show="")
            self.eyecnfm_btn.configure(text="🕶️")
        else:
            self.cnfmpwd_entry.configure(show="*")
            self.eyecnfm_btn.configure(text="👓")

    def error_check(self):
        self.userid = self.user_entry.get().strip()
        self.pwd = self.pwd_entry.get().strip()

        if not self.userid or not self.pwd:
            self.error_label.configure(text="Please enter the details")
        else:
            self.error_label.configure(text="")

    def run(self):
        self.app.mainloop()


loginobj = Register_app()
loginobj.run()
