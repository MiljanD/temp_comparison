
import matplotlib.pyplot as plt
from pathlib import Path


def create_chart(first_station_data, second_station_data, names):

    status_list = [first_station_data["message"], second_station_data["message"]]
    failed_status = [status for status in status_list if status != "Success"]

    if failed_status:
        print(failed_status)
    else:
        x_axis = first_station_data["dates"]

        y_ax_first_stat_data = first_station_data["temps"]
        y_ax_second_stat_data = second_station_data["temps"]


        plt.plot(x_axis, y_ax_first_stat_data, label=names[0], marker="o", color="blue")
        plt.plot(x_axis, y_ax_second_stat_data, label=names[1], marker="s", color="green")

        plt.xlabel("Dates")
        plt.ylabel("Measured Temperatures")
        plt.title("Temperature Comparison")

        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        current_wd = Path(__file__).parent
        active_chart_path = Path(f"{current_wd.parent}/charts/act_chart.png")

        plt.savefig(active_chart_path, dpi=300, bbox_inches="tight")
        plt.close()



