from fastapi import APIRouter, Depends, HTTPException, Request, Response
from validators.adminValidators import AdminUserNameUpdateForm,AdminPasswordUpdateForm
import bcrypt
from database import db
from models import User
from utils.passwords import PasswordEncoder
from utils.tokens import Tokens
from middlewares.admin_middleware import admin_validated

adminRouter = APIRouter(
    prefix="/admin",
    dependencies=[Depends(admin_validated)],
    tags=["admin"],
)

@adminRouter.delete("/delete-user/{id}")
def deleteUser(id: int):
    deleted_user, affected_rows = db.delete(User, User.id == id)
    if affected_rows < 1:
        return Response(f"Something was wrong, couldn't find user id: {id}")
    else:
        return {
            "message": "User deleted",
            "data": deleted_user
        }

@adminRouter.put("/update-username/{id}")
def updateUserName(id: int, data: AdminUserNameUpdateForm):
    updated_user, affected_rows =  db.update(User, User.id == id, {User.username: data.username}) 
    if affected_rows < 1:
        return Response(f"There was a problem updating user {id}'s username")
    else:
        return {
            "message": "User updated",
            "data": updated_user 
        }
    

@adminRouter.put("/update-password/{id}")
def updateUserPassword(id: int, data: AdminPasswordUpdateForm):
    pwEncoder = PasswordEncoder()
    encoded = pwEncoder.encodePassword(data.password)
    updated_user, affected_rows =  db.update(User, User.id == id, {User.password: encoded}) 
    if affected_rows < 1:
        return Response(f"There was a problem updating user {id}'s username")
    else:
        return {
            "message": "User updated",
            "data": updated_user 
        }    