from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str= Field(description="Blog title")
    content: str= Field(description="Blog content")

class BlogState(TypedDict):
    topic: str
    blog: Blog
    language: str

