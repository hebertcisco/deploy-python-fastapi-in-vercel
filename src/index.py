from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from src.DB_Connection import DB_Connection
import logging
from src.dtos.ISayHelloDto import ISayHelloDto
from pymongo.mongo_client import MongoClient


                

                
uri = "mongodb://adminSeed:process.env.DB_PASS@ac-ufuhqvj-shard-00-00.5h6sox3.mongodb.net:27017,ac-ufuhqvj-shard-00-01.5h6sox3.mongodb.net:27017,ac-ufuhqvj-shard-00-02.5h6sox3.mongodb.net:27017/?ssl=true&replicaSet=atlas-1vge86-shard-0&authSource=admin&retryWrites=true&w=majority&appName=ProductsTable"
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():   
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
    except Exception as e:
        print(e)  
                        
               
    
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
