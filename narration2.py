import customtkinter as ctk
import tkinter as tk

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    Image = None
    ImageDraw = None
    ImageOps = None

try:
    import pygame
    pygame.mixer.init()
    AUDIO = True
except Exception:
    AUDIO = False

import os

BASE = os.path.dirname(os.path.abspath(__file__))

ctk.set_appearance_mode("dark")

PURPLE, PURPLE_DIM, BG, PANEL, FIELD, TEXT_MUTED = "#B57BFF", "#7A4FCC", "#120B1E", "#1D1330", "#2A1D45", "#9A8FB5"

NARRATOR_SIZE = 160
DELAY = 30

STORY = [
    "Have you ever created an online account? A password is a secret combination of characters used to protect your account and prevent unauthorised access.",
    "GET and POST are HTTP methods that allow devices to communicate with web servers. GET is commonly used to request information, while POST is used to submit information.",
    "A Rail Fence Cipher is a type of transposition cipher. It encrypts a message by arranging its letters in a zigzag pattern and reading them row by row.",
    "A Substitution Cipher encrypts a message by replacing each letter with another letter according to a fixed key. For example, using a shift of three, A becomes D and B becomes E.",
    "Strong passwords help protect online accounts. Use long, unique passwords and avoid predictable information such as birthdays, names, or simple combinations like 123456.",
    "Websites should not store passwords as plain text. Instead, they use password hashing and salting to make stored passwords more secure and difficult to misuse if a database is exposed.",
    "A brute-force attack involves systematically trying different password combinations to guess a password. Longer and less predictable passwords make this approach more difficult.",
    "A dictionary attack uses lists of common words and passwords to guess someone's login credentials. Avoid common passwords such as password123 or football123.",
    "Phishing is a technique where attackers pretend to be trusted people or organisations to trick users into revealing sensitive information. Always check suspicious links and never enter passwords on untrusted websites.",
    "Now we know the difference! GET requests information, POST submits information, encryption helps protect messages, and strong passwords help secure accounts. Understanding these cybersecurity concepts helps us protect our personal information online."
]



def load_image(name):
    if Image is None:
        return None

    try:
        image_path = os.path.join(BASE, name)
        return Image.open(image_path).convert("RGBA")
    except (FileNotFoundError, OSError):
        print(f"Image not found: {name}")
        return None


class StoryPage:

    def __init__(self, complete=None):
        self.complete = complete
        self.muted = False
        self.index = 0
        self.typing = False
        self.after_id = None
        self.ref_image = load_image("reference.png")
        self.ref_ctk_image = None
        self.narrator_image = None

        self.app = ctk.CTk()
        self.app.title("Level 1 Narration")
        self.app.geometry("900x560")
        self.app.minsize(700, 460)
        self.app.configure(fg_color=BG)

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=1)

        self.narration_panel()
        self.middle()
        self.footer()

        self.app.bind("<space>", lambda e: self.next())
        self.app.bind("<Return>", lambda e: self.next())

        self.show_line(0)

    def narration_panel(self):
        self.panel = ctk.CTkFrame(
            self.app,
            fg_color=PANEL,
            corner_radius=15
        )

        self.panel.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=30,
            pady=(30, 10)
        )

        self.panel.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self.panel,
            text="Level 1 Story Explanation",
            font=("Helvetica", 15, "bold"),
            text_color=PURPLE
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(6, 4)
        )

        self.text_label = ctk.CTkLabel(
            self.panel,
            text="",
            font=("Helvetica", 20),
            justify="left",
            anchor="w",
            wraplength=750,
            text_color="white"
        )

        self.text_label.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=25,
            pady=(6, 4)
        )

        self.hint_label = ctk.CTkLabel(
            self.panel,
            text="",
            font=("Times New Roman", 12),
            text_color=TEXT_MUTED
        )

        self.hint_label.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 10)
        )

        for w in (
            self.panel,
            self.text_label,
            self.hint_label,
            self.title_label
        ):
            w.bind("<Button-1>", lambda e: self.next())

        self.panel.bind(
            "<Configure>",
            lambda e: self.text_label.configure(
                wraplength=max(200, e.width - 48)
            )
        )

    def middle(self):
        self.mid_frame = ctk.CTkFrame(
            self.app,
            fg_color="transparent"
        )

        self.mid_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30,
            pady=10
        )

        self.mid_frame.grid_columnconfigure(0, weight=0)
        self.mid_frame.grid_columnconfigure(1, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=2)
        self.mid_frame.grid_rowconfigure(0, weight=1)

        self.narrator = ctk.CTkFrame(
            self.mid_frame,
            width=NARRATOR_SIZE,
            height=NARRATOR_SIZE,
            corner_radius=NARRATOR_SIZE // 2,
            fg_color=FIELD
        )

        self.narrator.grid(
            row=0,
            column=0,
            padx=(2, 8)
        )

        self.narrator.grid_propagate(False)

        self.narrator_image = self.make_narrator_image()

        if self.narrator_image:
            self.narrator_label = ctk.CTkLabel(
                self.narrator,
                text="",
                image=self.narrator_image
            )
        else:
            self.narrator_label = ctk.CTkLabel(
                self.narrator,
                text="Narrator",
                fg_color=TEXT_MUTED,
                font=("Helvetica", 14, "bold")
            )

        self.narrator_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.ref_frame = ctk.CTkFrame(
            self.mid_frame,
            fg_color=PANEL,
            border_width=2,
            border_color=PURPLE,
            corner_radius=10
        )

        self.ref_frame.grid(
            row=0,
            column=2,
            sticky="nsew"
        )

        if self.ref_image:
            self.ref_label = ctk.CTkLabel(
                self.ref_frame,
                text=""
            )

            self.ref_label.place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

            self.ref_frame.bind(
                "<Configure>",
                self.resize_ref
            )

            self.app.after(100, lambda: self.resize_ref(
                type("Event", (), {
                    "width": self.ref_frame.winfo_width(),
                    "height": self.ref_frame.winfo_height()
                })()
            ))

        else:
            self.ref_label = ctk.CTkLabel(
                self.ref_frame,
                text="Image",
                fg_color=TEXT_MUTED,
                font=("Helvetica", 20, "bold")
            )

            self.ref_label.place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

    def footer(self):
        self.footer_frame = ctk.CTkFrame(
            self.app,
            fg_color="transparent"
        )

        self.footer_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=30,
            pady=20
        )

        self.footer_frame.grid_columnconfigure(1, weight=1)

        self.sound_label = ctk.CTkButton(
            self.footer_frame,
            text="🔊",
            command=self.toggle_audio
        )

        self.sound_label.grid(
            row=0,
            column=0
        )

        self.skip_button = ctk.CTkButton(
            self.footer_frame,
            text="COMPLETE",
            font=("Helvetica", 16, "bold"),
            width=150,
            height=50,
            text_color="#FFFFFF",
            fg_color=PURPLE_DIM,
            hover_color=PURPLE_DIM,
            command=self.skip
        )

        self.skip_button.grid(
            row=0,
            column=2,
            sticky="e"
        )

    def make_narrator_image(self):
        img = load_image("narrator.png")

        if img is None:
            return None

        img = ImageOps.fit(
            img,
            (NARRATOR_SIZE, NARRATOR_SIZE)
        )

        mask = Image.new("L", img.size, 0)

        ImageDraw.Draw(mask).ellipse(
            (0, 0, *img.size),
            fill=255
        )

        img.putalpha(mask)

        return ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(NARRATOR_SIZE, NARRATOR_SIZE)
        )

    def resize_ref(self, event):
        if self.ref_image is None:
            return

        box = (
            max(50, event.width - 24),
            max(50, event.height - 24)
        )

        fit_img = ImageOps.contain(
            self.ref_image,
            box
        )

        self.ref_ctk_image = ctk.CTkImage(
            light_image=fit_img,
            dark_image=fit_img,
            size=fit_img.size
        )

        self.ref_label.configure(
            image=self.ref_ctk_image
        )

    def show_line(self, i):
        self.index = i

        if self.after_id:
            self.app.after_cancel(self.after_id)
            self.after_id = None

        self.full_text = STORY[i]
        self.char = 0
        self.typing = True

        self.text_label.configure(text="")

        self.hint_label.configure(
            text=f"{i + 1}/{len(STORY)}"
        )

        self.play_voice(i)
        self.type_animation()

    def type_animation(self):
        self.char += 1

        self.text_label.configure(
            text=self.full_text[:self.char]
        )

        if self.char < len(self.full_text):
            self.after_id = self.app.after(
                DELAY,
                self.type_animation
            )
        else:
            self.after_id = None
            self.end_typing()

    def end_typing(self):
        self.typing = False

        self.text_label.configure(
            text=self.full_text
        )

        last = self.index == len(STORY) - 1

        if last:
            self.skip_button.configure(
                state="normal",
                fg_color=PURPLE
            )

            self.hint_label.configure(
                text=f"{self.index + 1}/{len(STORY)}"
            )

        else:
            self.hint_label.configure(
                text=f"{self.index + 1}/{len(STORY)}   Click To Continue"
            )

    def next(self):
        if self.typing:
            if self.after_id:
                self.app.after_cancel(self.after_id)
                self.after_id = None

            self.end_typing()

        elif self.index < len(STORY) - 1:
            self.show_line(self.index + 1)

    def play_voice(self, i):
        if not AUDIO or self.muted:
            return

        self.path = os.path.join(
            BASE,
            "audio",
            f"LEVEL_1_{i + 1}.mp3"
        )

        if os.path.exists(self.path):
            try:
                pygame.mixer.music.load(self.path)
                pygame.mixer.music.play()
            except Exception as e:
                print("Audio error:", e)

    def toggle_audio(self):
        self.muted = not self.muted

        self.sound_label.configure(
            text="🔇" if self.muted else "🔊"
        )

        if self.muted:
            if AUDIO:
                pygame.mixer.music.stop()
        else:
            self.play_voice(self.index)

    def skip(self):
        if self.after_id:
            self.app.after_cancel(self.after_id)
            self.after_id = None

        if AUDIO:
            pygame.mixer.music.stop()

        if self.complete:
            self.complete()

        self.app.destroy()

    def run(self):
        self.app.mainloop()


storyobj = StoryPage()
storyobj.run()