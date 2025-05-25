from pydantic import BaseModel
from typing import Literal

class Transport(BaseModel):
    """
    Klasa Transport

        Atrybuty:
            -typ: str Dozwolone wartości: 'samolot', 'bus', 'we wlasnym zakresie'
            -koszt: int
    """

    typ: Literal["samolot","bus","we wlasnym zakresie"]
    koszt: int
