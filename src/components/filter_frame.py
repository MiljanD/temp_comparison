
import tkinter as tk
from tkinter import ttk
from src.core.extract_station import extract_station_id, extract_station_name
from src.untils.extract_temps import extract_temp
from src.untils.chart_creation import create_chart
from src.components.chart_frame import display_chart_on_screen



def generate_chart_by_station_data(station_one, station_two, date_entry):
    if  not station_one.get() or not station_two.get():
        print("Chose both filters.")
    else:
        first_stat_name = extract_station_name(station_one.get())
        second_stat_name = extract_station_name(station_two.get())
        station_names = (first_stat_name[0].capitalize(), second_stat_name[0].capitalize())

        input_date = date_entry.get()

        first_stat_data = extract_temp(station_one.get(), input_date)
        second_stat_data = extract_temp(station_two.get(), input_date)

        create_chart(first_stat_data, second_stat_data, station_names)


def change_to_chart_display(event, window):
    btn = event.widget
    if btn:
        display_chart_on_screen(window)


def show_filters(window):

    station_ids = extract_station_id()

    label_station_one = ttk.Label(window, text="Chose first station ID:")
    label_station_one.grid(column=0, row=0, pady=5, padx=10)
    station_one = ttk.Combobox(window, values=station_ids)
    station_one.grid(column=0, row=1, pady=5, padx=10)

    label_station_two = ttk.Label(window, text="Chose second station ID:")
    label_station_two.grid(column=0, row=2, pady=5, padx=10)
    station_two = ttk.Combobox(window, values=station_ids)
    station_two.grid(column=0, row=3, pady=5, padx=10)

    entry_label = ttk.Label(window, text="Date input (yyyy-mm-dd):")
    entry_label.grid(column=0, row=4, pady=5, padx=10)
    date_entry = tk.Entry(window)
    date_entry.grid(column=0, row=5, pady=5, padx=10)


    selection_button = ttk.Button(window, text="Generate Chart",
                                  command=lambda : generate_chart_by_station_data(station_one, station_two, date_entry))
    selection_button.grid(column=0, row=6, pady=5)

    display_chart = ttk.Button(window, text="Display Chart")
    display_chart.grid(column=0, row=7 , padx=10, pady=10)

    return display_chart






