from fastapi import FastAPI

from controllers.base import api_router
from database import Base, engine

app = FastAPI(debug=True)

app.include_router(api_router)



Base.metadata.create_all(bind=engine)