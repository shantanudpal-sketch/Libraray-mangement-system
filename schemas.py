
from pydantic import BaseModel, Field, ConfigDict


# Schema for creating a new book
class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)


# Schema for updating an existing book
class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    author: str | None = Field(default=None, min_length=1, max_length=100)

    model_config = ConfigDict(extra="forbid")


# Schema for returning book details
class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
