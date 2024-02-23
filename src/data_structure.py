from pydantic import BaseModel

class StartupsIn(BaseModel):
    rd: float
    administration: float
    marketing: float
    state: str

class StartupsOut(BaseModel):
    profit: float

class AdsIn(BaseModel):
    gender: str
    age: int
    estimatedSalary: float

class AdsOut(BaseModel):
    purchased: str