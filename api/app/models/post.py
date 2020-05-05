from orm import Model, Integer, String, Text

from app.db.database import database, metadata


class Post(Model):
    __tablename__ = "posts"
    __database__ = database
    __metadata__ = metadata

    id = Integer(primary_key=True)
    post_id = Integer(unique=True)
    label = String(max_length=255, unique=True)
    text = Text()
