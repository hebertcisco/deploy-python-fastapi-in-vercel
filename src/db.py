from pymongo import MongoClient
import os
client = None

def get_client():
        global client
        uri = "mongodb://"+os.environ["USER"]+":"+os.environ["DB_PASS"]+"@ac-ufuhqvj-shard-00-00.5h6sox3.mongodb.net:27017,ac-ufuhqvj-shard-00-01.5h6sox3.mongodb.net:27017,ac-ufuhqvj-shard-00-02.5h6sox3.mongodb.net:27017/?ssl=true&replicaSet=atlas-1vge86-shard-0&authSource=admin&retryWrites=true&w=majority&appName=ProductsTable"
        # Create a new client and connect to the server
        client = MongoClient(uri)
        return client




# Send a ping to confirm a successful connection      
def client_ping(client):
        try:
                client.admin.command('ping')
                return {"message":"Successful Ping"}
        except Exception as e:
                return {"message":"Failed"}
                

