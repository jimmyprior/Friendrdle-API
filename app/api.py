from fastapi import FastAPI

from .models import (
    NewGameSchema, 
    GameResultsSchema
)

from .database import (
    db_get_game,
    db_add_results,
    db_create_game
)

app = FastAPI(debug=True)


@app.get("/")
async def hello():
    return {"yes" : "please"}


@app.post("/create", tags=["game"])
async def create_game(data : NewGameSchema):
    """
    create a new game 
    ->
    {
        "code" : game-id
    }
    """
    game_id = db_create_game(data.word, data.guesses)
    return {"gameID" : game_id}


@app.get("/{game_id}", tags=["game"])
async def get_game(game_id : str):
    """
    Get the game data 
    ->
    {
        word : str,
        leaderboard : [
            name : {
                sucess : bool,
                attempts : int,
                time : int,
            }
        ],

    }
    
    """
    return db_get_game(game_id)


@app.post("/{game_id}/finished", tags=["game"])
async def update_game(game_id : str, data : GameResultsSchema):
    """
    Add results to the game
    ->
    maybe return leaderboard? 
    {
        leaderboard : [
            name : {
                sucess : bool,
                attempts : int,
                time : int,
            }
        ],
    }
    """
    db_add_results(game_id, *data)
    return db_get_game(game_id)

