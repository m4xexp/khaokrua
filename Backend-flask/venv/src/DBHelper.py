import psycopg2
import psycopg2.extras

class DBHelper:

    def __init__(self):
        self.host = "ec2-18-206-103-49.compute-1.amazonaws.com"
        self.user = "iciomjkjkvxskd"
        self.password = "adea728b625eec99b3a1e7cd196acc8399dc1989771831f82f75ff89b7242022"
        self.db = "d77l258vu2ou21"

    def __connect__(self):
        self.con = psycopg2.connect(host=self.host, user=self.user, password=self.password, dbname=self.db)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        columns = []
        for desc in self.cur.description:
            columns.append(desc.name)
        columns = tuple(columns)
        self.__disconnect__()
        return data, columns

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()
