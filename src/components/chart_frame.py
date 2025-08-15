import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path


def show_body_frame(window):
    frame = tk.Frame(window)
    frame.grid(row=0, column=1, sticky="nsew")

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    return frame



def display_chart_on_screen(frame):
    chart_path = Path("src/charts/act_chart.png")
    image = Image.open(chart_path)
    image = image.resize((800, 600))
    bg_image = ImageTk.PhotoImage(image)

    chart_label = tk.Label(frame, image=bg_image)
    chart_label.image = bg_image

    chart_label.grid(row=0, column=0, sticky="nsew")




