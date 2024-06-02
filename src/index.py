from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import get_mongo_client
from src.dtos.ISayHelloDto import ISayHelloDto
import time
from bson import ObjectId
from pymongo.operations import SearchIndexModel

#comment
conn = None                
def createDbConnection():
  conn = get_client()
  return conn
                
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

def set_search_atlas_index():

    try:
        client = get_mongo_client()
        tasks_collection = client.get_collection('tasks')
        search_index_model = SearchIndexModel(
            definition={
                "mappings": {
                    "dynamic": True
                },
            },
            name="default",
        )
        result = tasks_collection.create_search_index(model=search_index_model)
        print(result)
    except Exception as e:
        print(e)


set_search_atlas_index()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
  
@app.get("/ping")
async def ping():
    conn = createDbConnection()
    return client_ping(conn)

#test
@app.get("/api/tasks")
async def get_tasks():
    client = get_mongo_client()
    tasks_collection = client.get_collection('tasks')
    tasks = list(tasks_collection.find({}).limit(25))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks
