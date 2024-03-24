from typing import Annotated
from fastapi import APIRouter, Query, Request
from fastapi import status

from spotipy import SpotifyException
from app.exceptions import (
    AddSongException,
    FindSimilarSongsException,
    UnauthorizedException,
)
from app.finder.clients import get_autocomplete, add_songs, find_similar_songs


router = APIRouter(prefix="/find")


@router.get("/autocomplete")
def autocomplete(q: str, request: Request):
    if not request.cookies.get("token"):
        return status.HTTP_401_UNAUTHORIZED
    else:
        return get_autocomplete(q=q, token=request.cookies.get("token"))


@router.get("/get_similar_songs")
def get_similar_songs(song: str, request: Request):
    try:
        if not request.cookies.get("token"):
            raise UnauthorizedException
        else:
            return find_similar_songs(song, token=request.cookies.get("token"))
    except SpotifyException:
        raise FindSimilarSongsException


@router.get("/generate/")
def generate(tracks: Annotated[list[str], Query()], request: Request):
    try:
        if not request.cookies.get("token"):
            raise UnauthorizedException
        else:
            return add_songs(tracks=tracks, token=request.cookies.get("token"))

    except SpotifyException:
        raise AddSongException
