import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGO_URL = os.getenv('MONGO_URL')

client = MongoClient(MONGO_URL, server_api=ServerApi('1'))

def get_active_props(dfs_book):
    leage_coll = client['props'][dfs_book]
    active_props = leage_coll.find({'active': True})
    return list(active_props)
