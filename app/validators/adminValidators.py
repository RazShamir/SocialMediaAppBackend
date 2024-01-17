from pydantic import BaseModel

class AdminUserNameUpdateForm(BaseModel):
    username: str


class AdminPasswordUpdateForm(BaseModel):
    password: str
