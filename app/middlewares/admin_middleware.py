


from fastapi import Depends,HTTPException
from middlewares.token_middleware import extract_token
from models import User
from database import db


def admin_validated(user = Depends(extract_token)):
    user: User = (db.query(User)
                  .filter(User.email == user["email"])
                 # .options(joinedload(User.roles))
                  .first())
    for role in user.roles:
        if role.id == 2: # admin
            return True
    raise HTTPException(status_code=403, detail="Access denied")    