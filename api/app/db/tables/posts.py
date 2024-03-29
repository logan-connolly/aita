import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, String, Text

from app.db.tables.base import Base


class Post(Base):
    """Reddit post information from AITA"""

    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    label = Column(String(255), nullable=False)
    text = Column(Text(), nullable=False)
    ts = Column(DateTime, default=func.now())

    @staticmethod
    def generate_post_id(reddit_id: str) -> uuid.UUID:
        return uuid.uuid5(uuid.NAMESPACE_URL, f"/posts/{reddit_id}")
