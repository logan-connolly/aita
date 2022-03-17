from databases import Database
from orm import ModelRegistry
from sqlalchemy import MetaData

from app.core.config import settings

metadata = MetaData()
database = Database(url=settings.uri)
models = ModelRegistry(database=database)
