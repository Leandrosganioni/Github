# routers/players.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

@router.get("/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return schemas.Player(**db_player._asdict())

@router.get("/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return [schemas.Player(**player._asdict()) for player in players]
