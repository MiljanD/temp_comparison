import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="dm3004^mk2606",
        database="stations"
    )

    return connection