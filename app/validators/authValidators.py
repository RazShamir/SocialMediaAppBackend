

from pydantic import BaseModel

class UserSignUpForm(BaseModel):
    email: str
    password:str


class UserSignInForm(BaseModel):
    email: str
    password:str    