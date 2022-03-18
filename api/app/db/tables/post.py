from sqlalchemy.sql import func
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Text

from app.db.tables.base import Base


class Post(Base):
    """Reddit post information from AITA"""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    reddit_id = Column(String(6), unique=True, nullable=False)
    title = Column(String(255), nullable=False, unique=True)
    label = Column(String(255), nullable=False, unique=True)
    text = Column(Text(), nullable=False, unique=True)
    ts = Column(DateTime, default=func.now())
