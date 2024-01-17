from pydantic import BaseModel

class PostValidator(BaseModel):
    title: str
    content: str

