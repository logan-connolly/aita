from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """All pydantic schemas should use ORM mode"""

    model_config = ConfigDict(from_attributes=True)
