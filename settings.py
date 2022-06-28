import os

DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_PORT = 5432
DB_NAME = os.environ['DB_NAME']
SECRET_KEY = os.getenv('SECRET_KEY')

DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQL_DATABASE_URI = DB_URI
