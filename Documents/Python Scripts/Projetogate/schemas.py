# schemas.py

from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    team_id: int

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int
    team_name: str  # Adicione este campo

    class Config:
        orm_mode = True

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True
