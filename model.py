from pydantic import BaseModel
from typing import Optional
from enum import Enum

class User_Create(BaseModel):
    name : str
    email : str

class User_Response(BaseModel):
    id : int
    name : str
    email : str

class User_Update(BaseModel):
    name : str
    email : str

class User_Patch(BaseModel):
    name : Optional[str]  = None
    email : Optional[None] = None

class Fitness_Type(str,Enum):
    RUNNING = "Running"
    JOGGING = "Jogging"
    WALKING = "Walking"

class Create_Fitness(BaseModel):
    type : Fitness_Type
    dist : float
    time : float

class Update_Fitness(BaseModel):
    type : Fitness_Type
    dist : float
    time : float

class Patch_Fitness(BaseModel):
    type : Optional[Fitness_Type] = None
    dist : Optional[float] = None
    time : Optional[float] = None

class LeaderBoard(BaseModel):
    name : str
    type : Fitness_Type
    dist : float
    time : float
    speed : float