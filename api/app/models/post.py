import orm
from sqlalchemy.sql import func

from app.db.database import models


class Post(orm.Model):
    """Post Model that shall be stored to DB"""

    tablename = "posts"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "reddit_id": orm.String(max_length=6, unique=True),
        "title": orm.String(max_length=255),
        "label": orm.String(max_length=255),
        "text": orm.Text(),
        "ts": orm.DateTime(default=func.now()),
    }
