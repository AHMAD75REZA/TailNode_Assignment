# database.py
from pymongo import MongoClient
from config import MONGODB_CONNECTION_STRING

def connect_to_mongodb():
    client = MongoClient(MONGODB_CONNECTION_STRING)
    return client

def insert_user_data(user_data, db):
    users_collection = db['users']
    users_collection.insert_one(user_data)

def insert_post_data(post_data, user_id, db):
    posts_collection = db[f'user_{user_id}_posts']
    posts_collection.insert_one(post_data)
