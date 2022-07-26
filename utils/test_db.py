import os
from flask_sqlalchemy import SQLAlchemy

from settings import DB_NAME


class TestDB:
    def __init__(self):
        self.db_name =os.environ['DB_NAME'] + "_test"
        self.db_host =os.environ['DB_HOST']
        self.db_root_password = os.environ['ROOT_DB_PASSWORD']

        if self.db_root_password:
            self.db_user = 'postgres'
            self.db_password = self.db_root_password
        else:
            self.db_user = 'postgres'
            self.db_password = self.db_password
        self.db_uri = f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432'

    def createdb(self):
        if self.db_root_password:
            engine = SQLAlchemy.create_engine(self.db_uri)
            conn = engine.connect()
            conn.execute("COMMIT")
            conn.execute(f"CREATE DATABASE {self.db_name}")
            conn.close()

        return f"{self.db_uri}/{self.db_name}"

    def destroydb(self):
        if self.db_root_password:
            engine = SQLAlchemy.create_engine(self.db_uri)
            conn = engine.connect()
            conn.execute("COMMIT")
            conn.execute(f"DROP DATABASE {self.db_name}")
            conn.close()
