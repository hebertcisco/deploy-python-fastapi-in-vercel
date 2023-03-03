from fastapi import FastAPI

from api.dtos.ISayHelloDto import ISayHelloDto

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

    
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
