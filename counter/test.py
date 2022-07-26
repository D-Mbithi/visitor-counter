import os
import unittest
import pathlib

from dotenv import load_dotenv

from settings import SQLALCHEMY_DATABASE_URI
env_dir = pathlib.Path(__file__).parents[1]
load_dotenv(os.path.join(env_dir, ".env"))

from counter.models import Counter
from application import db
from application import create_app as create_app_base
from utils.test_db import TestDB


class CounterTest(unittest.TestCase):
    def create_app(self):
        return create_app_base(
            SQLALCHEMY_DATABASE_URI = self.db_uri,
            TESTING = True,
            SECRET_KEY='mytestsecretkey'
        )

    def setUp(self):
        self.test_db = TestDB
        self.db_uri = self.test_db.createdb()
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()
        with self.app_factory.app_context():
            db.create_all()

    def tearDown(self):
        with self.app_factory.app_context():
            db.drop_all()
        self.test_db.destroydb()

    def test_count(self):
        response = self.app.get('/')
        assert '1' in str(response.data)
