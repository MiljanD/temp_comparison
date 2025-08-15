import numpy as np
import pandas as pd
from pathlib import Path



def generate_data_path(stat_id):
    current_wd_path = Path(__file__).parent
    src_path= current_wd_path.parent
    data_folder = "/data/temp_data/"
    zero_count = 5
    file_prefix = "TG_STAID"
    file_suffix = None

    if int(stat_id) < 10:
        file_suffix = f"{zero_count * "0"}" + stat_id + ".txt"
    elif int(stat_id) > 99:
        file_suffix = f"{(zero_count -2) * "0"}" + stat_id + ".txt"
    else:
        file_suffix = f"{(zero_count - 1) * "0"}" + stat_id + ".txt"

    filename = file_prefix + file_suffix

    data_path = Path(f"{src_path}{data_folder}{filename}")

    return data_path


def extract_temp(stat_id, input_date):

    data_path = generate_data_path(stat_id)

    df = pd.read_csv(data_path, skiprows=20, parse_dates=["    DATE"])
    df.rename(columns=lambda  x: x.strip(), inplace=True)

    df["TG0"] = df["TG"].mask(df["TG"] == -9999, np.nan)
    df["TEMP"] = df["TG0"] * 0.1

    dates = []
    temps = []
    msg = None
    filtered = df.loc[df["DATE"] == input_date]

    if not filtered.empty:
        idx = filtered.index[0]
        working_df = df[idx: idx + 10]

        for index, row in working_df.iterrows():
            current_date = str(row["DATE"])[:10]
            current_temp = round(row["TEMP"], 1)
            dates.append(current_date)
            temps.append(current_temp)
            msg = "Success"
    else:
        msg = f"{input_date} is not valid for station with ID {stat_id}"

    return {"message": msg, "dates" :dates, "temps": temps}
