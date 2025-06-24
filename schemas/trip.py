from pydantic import BaseModel

from models.country_type import Country


class TripCreate(BaseModel):
    title: str
    country: Country
    description: str

class TripGet(BaseModel):
    title: str
    country: Country
    description: str

    class Config:
        from_attributes = True

