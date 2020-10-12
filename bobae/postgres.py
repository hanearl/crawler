import psycopg2


class PostgresWrapper:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

        self.conn = self.__get_conn()
        self.cursor = self.conn.cursor()

    def __get_conn(self):
        conn_string = "host='{}' dbname ='{}' user='{}' password='{}'".format(
            self.host, self.dbname, self.user, self.password
        )
        return psycopg2.connect(conn_string)

    def insert(self, query):
        self.cursor.execute(query)

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fatchall()