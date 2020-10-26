from databases import Database
from sqlalchemy import create_engine, MetaData

from app.core.config import settings


metadata = MetaData()
database = Database(settings.URI)
