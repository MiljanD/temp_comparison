
from src.core.database import connect_to_db
from pathlib import Path
import pandas as pd



def write_in_stations(stat_id, stat_name, ct_code):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = ("INSERT INTO station_information (stat_id, stat_name, country_code) "
             "VALUES (%s, %s, %s)")
    cursor.execute(query, (stat_id, stat_name, ct_code))
    connection.commit()
    cursor.close()


def populate_stations():
    cd_path = Path(__file__).parent
    data_path = Path(f"{cd_path.parent}/data/stations.txt")

    df = pd.read_csv(data_path, skiprows=16)

    for index, row in df[:100].iterrows():
        stat_id = row["STAID"]
        stat_name = row["STANAME                                 "].strip()
        ct_code = row["CN"]

        write_in_stations(stat_id, stat_name, ct_code)






if __name__ == "__main__":
    populate_stations()