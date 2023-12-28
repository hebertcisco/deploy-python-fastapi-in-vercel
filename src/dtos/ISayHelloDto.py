from pydantic import BaseModel

class ISayHelloDto(BaseModel):
    message: str