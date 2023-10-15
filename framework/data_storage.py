```python
import psycopg2
from psycopg2 import sql

class DataStorage:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def store_data(self, table, data):
        columns = data.keys()
        values = [data[column] for column in columns]
        insert = sql.SQL('INSERT INTO {} ({}) VALUES ({})').format(
            sql.Identifier(table),
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.SQL(',').join(map(sql.Placeholder, columns))
        )
        self.cursor.execute(insert, data)
        self.conn.commit()

    def retrieve_data(self, table, condition=None):
        select = sql.SQL('SELECT * FROM {}').format(sql.Identifier(table))
        if condition:
            select += sql.SQL(' WHERE {}').format(sql.SQL(condition))
        self.cursor.execute(select)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
```