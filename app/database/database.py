import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGO_URL = os.getenv('MONGO_URL')

client = MongoClient(MONGO_URL, server_api=ServerApi('1'))
