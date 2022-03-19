import uuid

import replit
from fastapi import HTTPException

from .config import database_url


db = replit.database.Database(database_url)


def db_get_game(game_id : str):
    """
    get the data about a game
    """
    try:
        return db[game_id]
    except KeyError:
        raise HTTPException(404, f"{game_id} is not a valid gameID")
    


def db_add_results(game_id : str, completed : bool, guesses : int, name : str, time : int):
    """
    add results about a game
    """
    db_get_game(game_id)["results"].append({
        "completed" : completed,
        "guesses" : guesses,
        "name" : name,
        "time" : time
    })
    

def db_create_game(word : str, guesses : int) -> str:
    """
    create a new game 
    """
    
    game_id = str(uuid.uuid4())
    
    db[game_id] = {
        "word" : word,
        "guesses" : guesses,
        "results" : []
    }
    
    return game_id

