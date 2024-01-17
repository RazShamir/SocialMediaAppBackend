from fastapi import FastAPI
from routers.postRouter import postRouter
from routers.authRouter import authRouter
from routers.adminRouter import adminRouter

from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(postRouter)
app.include_router(authRouter)
app.include_router(adminRouter)