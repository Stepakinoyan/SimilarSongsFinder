from typing import List, Optional

from pydantic import BaseModel


class Artist(BaseModel):
    name: str


class Image(BaseModel):
    height: int
    url: str
    width: int


class Album(BaseModel):
    artists: List[Artist]
    images: List[Image]
    name: str


class Artist1(BaseModel):
    name: str


class Item(BaseModel):
    id: str
    artists: List[Artist1]
    name: str


class Tracks(BaseModel):
    items: List[Item]


class Total(BaseModel):
    tracks: Optional[Tracks] = None
