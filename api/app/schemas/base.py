from pydantic import BaseModel


class BaseSchema(BaseModel):
    """All pydantic schemas should use ORM mode"""

    class Config:
        orm_mode = True
