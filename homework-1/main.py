"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def fill_table_from_csv(table_name, file_name):
    conn = psycopg2.connect(
        dbname="north",
        user="postgres",
        password="159357",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            query = f"INSERT INTO {table_name} ({','.join(header)}) VALUES ({','.join(["%s"]*len(row))})"
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    fill_table_from_csv("employees", "north_data/employees_data.csv")
    fill_table_from_csv("customers", "north_data/customers_data.csv")
    fill_table_from_csv("orders", "north_data/orders_data.csv")


if __name__ == "__main__":
    main()
