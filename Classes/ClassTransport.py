from pydantic import BaseModel
from typing import Literal

class Transport(BaseModel):
    typ: Literal["samolot","bus","we wlasnym zakresie"]
    koszt: int
