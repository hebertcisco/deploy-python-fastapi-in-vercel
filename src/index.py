from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.DB_Connection import DB_Connection
import threading
import logging
from src.dtos.ISayHelloDto import ISayHelloDto


                
def createDbConnection():
  connection = DbConnection()
  return connection
                
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
    conn = x.start()
    return conn.ping()
