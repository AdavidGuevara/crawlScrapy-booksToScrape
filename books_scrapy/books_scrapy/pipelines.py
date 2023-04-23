from itemadapter import ItemAdapter
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class BooksScrapyPipeline:
    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = mysql.connector.connect(
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASS"],
            host=os.environ["MYSQL_HOST"],
            database=os.environ["MYSQL_DB"],
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS all_books""")
        self.curr.execute(
            """CREATE TABLE all_books (
            id INT NOT NULL AUTO_INCREMENT,
            title VARCHAR(500) NULL,
            category VARCHAR(100) NULL,
            price VARCHAR(100) NULL,
            PRIMARY KEY (id))"""
        )

    def store_item(self, item):
        self.curr.execute(
            """INSERT INTO all_books (title, category, price) VALUES (%s, %s, %s)""",
            (item["title"][0], item["category"][0], item["price"][0]),
        )
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_item(item)
        return item

    def close_conn(self):
        self.conn.close()
