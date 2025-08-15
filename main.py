
import tkinter as tk
from src.components.filter_frame import show_filters, change_to_chart_display
from src.components.chart_frame import show_body_frame




def init():

    window = tk.Tk()

    window.geometry("1080x720")
    window.title("Temperature Comparison")

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    window.rowconfigure(0, weight=1)

    filters_frame = tk.Frame(window)
    filters_frame.grid(row=0, column=0, sticky="nsew")

    display_on_screen = show_filters(filters_frame)
    frame = show_body_frame(window)

    display_on_screen.bind("<Button-1>", lambda event: change_to_chart_display(event, frame))

    window.mainloop()



init()