# crud.py

from sqlalchemy.orm import Session
from sqlalchemy import select, join
import models, schemas

def get_player(db: Session, player_id: int):
    stmt = (
        select(
            models.Player.id,
            models.Player.name,
            models.Player.team_id,
            models.Team.name.label("team_name")
        )
        .select_from(join(models.Player, models.Team, models.Player.team_id == models.Team.id))
        .where(models.Player.id == player_id)
    )
    result = db.execute(stmt).first()
    return result

def get_players(db: Session, skip: int = 0, limit: int = 10):
    stmt = (
        select(
            models.Player.id,
            models.Player.name,
            models.Player.team_id,
            models.Team.name.label("team_name")
        )
        .select_from(join(models.Player, models.Team, models.Player.team_id == models.Team.id))
        .offset(skip)
        .limit(limit)
    )
    results = db.execute(stmt).fetchall()
    return results

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
