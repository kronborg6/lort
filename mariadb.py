import os
import mysql.connector as database
# Connect to MariaDB Platform
try:
    conn = database.connect(
        user="admin",
        password="lort",
        host="localhost",
        database="test"
    )
    cur = conn.cursor()

    def create_table():
        try:
            statement = "CREATE TABLE IF NOT EXISTS table1 (ID INT NOT NULL AUTO_INCREMENT, send_time DATETIME, receive_time DATETIME, PRIMARY KEY(ID));"
            cur.execute(statement)
            conn.commit()
            print("ADD DATABASE TABLE")
        except database.Error as e:
            print(f"Error adding entry to database: {e}")
    def drop_table():
        try:
            statement = "DROP TABLE IF EXISTS table1"
            cur.execute(statement)
            conn.commit()
            print("DROPPE TABLE")
        except database.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

except database.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

# Get Cursor
drop_table()
create_table()