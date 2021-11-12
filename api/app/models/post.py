from orm import DateTime, Model, String, Text
from sqlalchemy.sql import func

from app.db.database import models


class Post(Model):
    tablename = "posts"
    registry = models
    fields = {
        "id": String(primary_key=True, max_length=6, unique=True),
        "title": String(max_length=255),
        "label": String(max_length=255),
        "text": Text(),
        "ts": DateTime(default=func.now()),
    }
