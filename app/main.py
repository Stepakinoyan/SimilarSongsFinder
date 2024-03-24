from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.finder.router import router as finder_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(finder_router)
