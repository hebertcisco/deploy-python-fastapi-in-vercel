from pymongo.mongo_client import MongoClient
import os

class DB_Connection:
        def __init__(self):
                
                uri = os.environ["MONGODB_URI"]

                # Create a new client and connect to the server
                self.client = MongoClient(uri)
                
                # Send a ping to confirm a successful connection
                
        def ping(self):
                try:
                    self.client.admin.command('ping')
                    return {"message":"Successful Ping"}
                except Exception as e:
                    return {"message":"Failed"}
                

