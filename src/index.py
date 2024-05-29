from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import get_client
from src.db import client_ping
import threading
import logging
from src.dtos.ISayHelloDto import ISayHelloDto
import time
import asyncio


conn = None                
def createDbConnection():
  conn = get_client()
  return conn
                
app = FastAPI()

x = threading.Thread(target=createDbConnection)

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

@app.get("/tasks")
async def get_tasks():
    client = get_client()
    tasks_collection = client['sample_mflix.comments']
    tasks = list(tasks_collection.find({}).limit(25))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks
