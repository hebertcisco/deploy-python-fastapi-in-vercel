from pymongo import MongoClient
import os

db = None

def get_mongo_client():
    global db
    if db is None:
        uri = os.environ.get('MONGODB_ATLAS_URI')
        db = MongoClient(uri, appname="devrel.content.vercel")['TaskDB']
    return db

def get_collection(collection_name):
    if db is None:
        get_mongo_client()

