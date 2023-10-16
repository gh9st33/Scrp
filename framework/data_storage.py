```python
import psycopg2
from psycopg2 import pool

class DataStorage:
    def __init__(self, minconn, maxconn, host, database, user, password, port):
        self.minconn = minconn
        self.maxconn = maxconn
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.conn_pool = None

    def create_conn_pool(self):
        self.conn_pool = psycopg2.pool.SimpleConnectionPool(self.minconn, self.maxconn,
                                                            host=self.host,
                                                            database=self.database,
                                                            user=self.user,
                                                            password=self.password,
                                                            port=self.port)

    def get_conn(self):
        if self.conn_pool:
            return self.conn_pool.getconn()
        else:
            raise Exception("Connection pool is not initialized")

    def release_conn(self, conn):
        if self.conn_pool:
            self.conn_pool.putconn(conn)
        else:
            raise Exception("Connection pool is not initialized")

    def close_all_conn(self):
        if self.conn_pool:
            self.conn_pool.closeall()
        else:
            raise Exception("Connection pool is not initialized")

    def save_data(self, data):
        conn = self.get_conn()
        cursor = conn.cursor()

        # Assuming data is a dictionary with keys matching the column names in the database
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))

        query = f"INSERT INTO scraped_data ({columns}) VALUES ({values})"

        try:
            cursor.execute(query, list(data.values()))
            conn.commit()
        except Exception as e:
            print(f"Failed to insert data into database. Error: {e}")
        finally:
            cursor.close()
            self.release_conn(conn)
```