# main.py

from fastapi import FastAPI
from models import Base
from database import engine
from routers import players, teams

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router, prefix="/players", tags=["players"])
app.include_router(teams.router, prefix="/teams", tags=["teams"])
