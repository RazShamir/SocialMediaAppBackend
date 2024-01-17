from fastapi import APIRouter, Depends, HTTPException, Request
from validators.authValidators import UserSignUpForm,UserSignInForm
from sqlalchemy.orm import joinedload
from database import db
from models import User,Role
from utils.passwords import PasswordEncoder
from utils.tokens import Tokens
from utils.state import RequestStateManager
from middlewares.token_middleware import extract_token



authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@authRouter.post("/sign-up")
def signUp(signUpForm: UserSignUpForm):
    userExists = db.query(User).filter(User.email == signUpForm.email).first()
    if userExists:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    pwEncoder = PasswordEncoder()

    user = User()
    user.email = signUpForm.email

    user.roles.append(db.get(Role, 1))
    user.password = pwEncoder.encodePassword(signUpForm.password)
    db.save(user)
    user = db.query(User).filter(User.email == signUpForm.email).first()
    return user


@authRouter.post("/sign-in")
def signIn(signInForm: UserSignInForm):
    user: User = db.query(User).filter(User.email == signInForm.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User with this email does not exist")
    
    pwEncoder = PasswordEncoder()

    if not pwEncoder.comparePassword(signInForm.password, user.password):
        raise HTTPException(status_code=403, detail="Passwords do not match")

    tokens = Tokens() 
    token = tokens.encode({ "id": user.id, "email": user.email })
    return {
        "access_token": token
    }

@authRouter.get("/personal-info", dependencies=[Depends(extract_token)])
def personalInfo(request: Request):
    stateManager = RequestStateManager(request)
    user = stateManager.getUser()
    user: User = (db.query(User)
                  .filter(User.email == user["email"])
                 # .options(joinedload(User.roles))
                  .first())
    return user



            
# Authenticated Routes