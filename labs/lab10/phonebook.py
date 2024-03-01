import psycopg2
import csv

def read_csv(path):
    with open(path, 'r') as file:
        return [row for row in csv.DictReader(file)]

datacsv = read_csv("pb.csv")

con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="parolSHAPAARS1K", port=5432)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    user_name VARCHAR(255),
    phone_number VARCHAR(255)
);
""")

cur.execute(cur.mogrify("""INSERT INTO PhoneBook (user_name, phone_number) VALUES
(%s, %s)
""", (input(), input())))


def insert_data_to_postgres(connection, table_name, data):
    cursor = connection.cursor()
    placeholders = ', '.join(['%s'] * len(data[0]))
    columns = ', '.join(data[0].keys())
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    for row in data:
        cursor.execute(insert_query, list(row.values()))

    connection.commit()
    cursor.close()

insert_data_to_postgres(con, "PhoneBook", datacsv)

con.commit()
cur.close()
con.close()
# asd asd asd asd asd