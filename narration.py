import customtkinter as ctk
import tkinter as tk
try:
    from PIL import Image,ImageDraw,ImageOps

except ImportError:
    Image=None

try:
    import pygame
    pygame.mixer.init()
    AUDIO=True

except Exception:
    AUDIO=False

import os
BASE=os.path.dirname(os.path.abspath(__file__))

ctk.set_appearance_mode("dark")

PURPLE, PURPLE_DIM, BG, PANEL, FIELD, TEXT_MUTED = "#B57BFF", "#7A4FCC", "#120B1E", "#1D1330", "#2A1D45", "#9A8FB5"



NARRATOR_SIZE=160
DELAY=30
STORY=[" Have you ever connected your phone or laptop to Wi-Fi? Wi-Fi is a wireless technology that allows devices to connect to a router using radio waves instead of cables.","The Internet is a worldwide network connecting computers, servers, and devices. It lets us browse websites, watch videos, play online games, and communicate with people around the world."," Wi-Fi connects your device to a router, while the Internet connects networks worldwide. You can be connected to Wi-Fi even when your Internet service is down","Ethernet is a technology that connects devices to a network using physical cables. Unlike Wi-Fi, it provides a wired connection and is commonly used for computers, gaming consoles, and office networks","RJ45 is the common name for the eight-position connector used with Ethernet cables. It plugs into Ethernet ports on devices such as routers, computers, and network switches."," Wi-Fi offers convenience and mobility, while Ethernet often provides a more stable connection with lower latency. Both can provide Internet access, depending on how the network is configured.","Speaker: Devices on an IP network use IP addresses to send information to the right destination. IPv4 is the older version, while IPv6 provides a much larger address space for more connected devices.","Protect your Wi-Fi by using strong passwords and modern security such as WPA2 or WPA3. Keep your router updated, and never share your password with people you don't trust.","Cybersecurity professionals use tools such as Wifite to assess wireless network security in authorized environments. Testing should only be performed on networks you own or have explicit permission to assess.","Now we know the difference! Wi-Fi connects devices wirelessly, Ethernet connects them through cables, RJ45 is the common Ethernet connector, and the Internet connects networks around the world. Understanding these technologies helps us build reliable and secure networks."]



def load_image(name):
    if Image is None:
        return None
    try:
        return Image.open(os.path.join(BASE,name).convert("RGBA"))

    except (FileNotFoundError,OSError):
        return None
    
class StoryPage:
    def __init__(self,complete=None):
        self.complete=complete
        self.muted=False
        self.index=0
        self.typing=False
        self.after_id=None
        self.ref_pil=load_image("reference.png")
        self.ref_image=None

        self.app=ctk.CTK()
        self.app.title("Level 1 Narration")
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.title("Quiz Game")
        self.app.configure(fg_color=BG)
        self.app.grid_columnconfigure(0,weight=1)
        self.app.grid_rowconfigure(1,weight=1)
        self.narration_panel()
        self.middle()
        self.footer()
        self.app.bind("<space>",lambda e:self.next())
        self.app.bind("<Return>",lambda e:self.next())
        self.show_line(0)
    def narration_panel(self):
        self.panel=ctk.CTkFrame(self.app,fg_color=PANEL,corner_radius=15)
        self.panel.grid(row=0,column=0,sticky="ew",padx=30,pady=(30,10))
        self.panel.grid_configure(0,weight=1)
        self.title_label=ctk.CTkLabel(self.panel,text="Level 1 Story Explanation",font=("Helvetica",15,"bold",PURPLE))
        self.title_label.grid(row=0,column=0,sticky="w",padx=25,pady=(6,4))

        self.text_label=ctk.CTkLabel(self.panel,text="",font=("Helvetica",20),justify="left",anchor="w",wraplength=750,text_color="white")
        self.text_label.grid(row=1,column=0,sticky="ew",padx=25,pady=(6,4))

        self.hint_label=ctk.CTkLabel(self.panel,text="",font=("Times New Roman",12),text_color=TEXT_MUTED)
        self.hint_label.grid(row=2,column=0,sticky="ew",padx=25,pady=(0,10))

        for w in (self.panel,self.text_label,self.hint_label,self.title_label):
            w.bind("<Button-1>",lambda e:self.next())
        self.panel.bind("<Configure>",lambda e:self.text_label.configure(wraplength=max(200,e.width-48)))
    

    def middle(self):
        self.mid_frame=ctk.CTkFrame(self.app,fg_color="transparent")
        self.mid_frame.grid(row=1,column=0,stock="nsew",padx=30,pady=10)
        self.mid_frame.grid_columnconfigure(0,weight=0)
        self.mid_frame.grid_columnconfigure(1,weight=1)
        self.mid_frame.grid_columnconfigure(2,weight=2)
        self.mid_frame.grid_rowconfigure(0,weight=1)

        self.narrator=ctk.CTkFrame(self.mid_frame,width=NARRATOR_SIZE,height=NARRATOR_SIZE,corner_radius=NARRATOR_SIZE//2,fg_color=FIELD)

        self.narrator.grid(row=0,column=0,padx=(2,8))

        self.narrator_image=self.make_narrator_image()

        if self.narrator_image:
            self.narrator_label=ctk.CTkLabel(self.narrator_frame,fg_color=TEXT_MUTED,text="Narrator",image=self.narrator_image,font=("Helvetica",14,"bold"))

            self.narrator_label.place(relx=0.5,rely=1,anchor="s")
          
        else:
            self.narrator_label=ctk.CTkLabel(self.narrator_frame,fg_color=TEXT_MUTED,text="Narrator",font=("Helvetica",14,"bold"))

            self.narrator_label.place(relx=0.5,rely=0.5,anchor="center")
          
            self.ref_frame=ctk.CTkFrame(self.mid_frame,fg_color=PANEL,border_width=2,border_color=PURPLE,corner_radius=10)

            
