from pydantic import (
    conlist, 
    ConstrainedStr, 
    conint,
    BaseModel
)

from typing import Optional

MAX_GUESSES = 30
MAX_WORD_LENGTH = 6
MAX_NAME_LENGTH = 20


class Word(ConstrainedStr):
    min_length : int = 1
    max_length : int = MAX_WORD_LENGTH


class Name(ConstrainedStr):
    min_length : int = 2
    max_length : int = MAX_NAME_LENGTH


class GameResultsSchema(BaseModel):
    """
    schema for submitting game results 
    
    completed (whether it was completed or not)
    guesses : Guesses 
    name : str
    time : number of seconds it took
    """
    completed : bool
    guesses : conlist(item_type= Word, min_items=1, max_items=MAX_GUESSES)
    attempts : conint(ge=1, lt=MAX_GUESSES)
    name : Optional[Name] = None
    time : int
    


class NewGameSchema(BaseModel):
    """
    schema for creating a new game
    """
    word : Word
    guesses : conint(ge=1, lt=MAX_GUESSES)
    
