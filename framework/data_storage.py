```python
import psycopg2
from psycopg2 import sql

class DataStorage:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(
            dbname=db_config['dbname'], 
            user=db_config['user'], 
            password=db_config['password'], 
            host=db_config['host']
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
        query = sql.SQL('SELECT * FROM {}').format(sql.Identifier(table))
        if condition:
            query += sql.SQL(' WHERE {}').format(sql.SQL(condition))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
```