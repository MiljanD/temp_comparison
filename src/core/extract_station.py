from src.core.database import connect_to_db


def extract_station_id():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT stat_id FROM station_information")
    connection.commit()

    results = cursor.fetchall()
    station_ids = []
    for result in results:
        station_ids.append(result[0])

    cursor.close()

    return station_ids


def extract_station_name(stat_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT stat_name FROM station_information WHERE stat_id=%s", stat_id)
    connection.commit()

    result = cursor.fetchone()

    cursor.close()

    return result


