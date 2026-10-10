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
app=ctk.CTk()
app.title("Login")
app.geometry("900x560")
app.minsize(700,460)
app.configure(fg_color=BG)
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_rowconfigure(0,weight=1)
left=ctk.CTkFrame(app,fg_color=PANEL,corner_radius=16)
left.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
try:
    from PIL import Image
    img=ctk.CTkImage(Image.open("Banner.jpg"),size=(380,320))
    img_label=ctk.CTkLabel(left,text="",image=img)
    img_label.place(relx=0.5,rely=0.5,anchor="center")

except:
    img_label=ctk.CTkLabel(left,text="image",text_color=TEXT_MUTED,font=("Arial",20))
    img_label.place(relx=0.5,rely=0.5,anchor="center")

right=ctk.CTkFrame(app,fg_color="transparent")
right.grid(row=0,column=1,sticky="nsew",padx=(15,40),pady=30)
form=ctk.CTkFrame(right,fg_color="transparent")
form.place(relx=0.5,rely=0.5,anchor="center")

hello_label=ctk.CTkLabel(form,text="Hello!",font=("Helvetica",26,"bold"), text_color="white")
hello_label.pack(anchor="w")

wlcm_label=ctk.CTkLabel(form,text="Welcome Back",font=("Helvetica",34,"bold"), text_color=PURPLE)
wlcm_label.pack(anchor="w",pady=(0,10))


register_frame = ctk.CTkFrame(form, fg_color="transparent")
register_frame.pack(anchor="w", pady=(0, 10))
dont_label=ctk.CTkLabel(register_frame,text="Don't have an account?",font=("Helvetica",16),text_color=TEXT_MUTED)
dont_label.pack(side="left")
register_btn=ctk.CTkButton(register_frame,text="Register",font=("Helvetica",16,"underline"), text_color=TEXT_MUTED)
register_btn.pack(padx=5,side="left")

user_entry=ctk.CTkEntry(form,placeholder_text="User ID",width=380,height=45,fg_color=FIELD,corner_radius=8)
user_entry.pack(pady=8)

pwd_frame=ctk.CTkFrame(form,fg_color="transparent")
pwd_frame.pack(pady=8)
pwd_visible={"on":False}
pwd_entry=ctk.CTkEntry(pwd_frame,placeholder_text="Password",width=380,height=45,fg_color=FIELD,corner_radius=8,show="*")
pwd_entry.pack(pady=8)

def toggle_pwd():
    pwd_visible["on"]= not pwd_visible["on"]



app.mainloop()