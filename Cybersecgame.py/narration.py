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
