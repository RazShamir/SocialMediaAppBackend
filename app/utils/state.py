


from fastapi import Request


class RequestStateManager:
    def __init__(self, request: Request):
        self.request = request


    def get(self, key: str):
        return self.request.state._state.__getitem__(key)
    
    def set(self, key: str, value):
        return self.request.state._state.__setitem__(key, value)
    

    def getUser(self):
        return self.get("user")
    
    def setUser(self, user):
        return self.set("user", user)