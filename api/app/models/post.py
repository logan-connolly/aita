from orm import Model, String, Text

from app.db.database import database, metadata


class Post(Model):
    __tablename__ = "posts"
    __database__ = database
    __metadata__ = metadata

    id = String(primary_key=True, max_length=6, unique=True)
    title = String(max_length=255)
    label = String(max_length=255)
    text = Text()
