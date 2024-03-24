from typing import List, Optional

from pydantic import BaseModel


class Artist(BaseModel):
    name: str


class Image(BaseModel):
    height: int
    url: str
    width: int


class Artist1(BaseModel):
    name: str


class Track(BaseModel):
    id: str
    artists: List[Artist1]
    name: str
    preview_url: Optional[str]
    uri: str


class Recommendations(BaseModel):
    tracks: Optional[List[Track]] = None
