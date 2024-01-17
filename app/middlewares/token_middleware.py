
from fastapi import Request,HTTPException
from utils.state import RequestStateManager
from utils.tokens import Tokens

def extract_token(request: Request):
    stateManager = RequestStateManager(request)
    authHeader = request.headers.get("authorization")
    if not authHeader:
        raise HTTPException(status_code=401, detail="Unauthorized request, missing token")
    try:
        token = authHeader.split("Bearer ")[1]
        tokens = Tokens()
        user = tokens.decode(token) # { id, email }
        stateManager.setUser(user)
    except:
        raise HTTPException(status_code=401, detail="Unauthorized request, missing token")
    return stateManager.getUser()