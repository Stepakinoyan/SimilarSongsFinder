from spotipy import Spotify
from fastapi import status, HTTPException

from app.exceptions import SongsAddedMessage
from app.finder.recommendations_schema import Recommendations
from app.finder.schema import Total


def get_autocomplete(q: str, token: str):
    spotify = Spotify(auth=token)

    search = spotify.search(q=q)
    total = Total(**search)
    return total.model_dump()


def find_similar_songs(song: str, token: str):
    spotify = Spotify(auth=token)

    get_recommendations = spotify.recommendations(seed_tracks=[song], limit=20)

    total = Recommendations(**get_recommendations)
    return total.model_dump()


def add_songs(tracks: list, token: str):
    spotify = Spotify(auth=token)
    user_id = spotify.current_user()["id"]

    playlist = spotify.user_playlist_create(user=user_id, name="Generated playlist")
    spotify.playlist_add_items(playlist_id=playlist["id"], items=tracks)

    raise SongsAddedMessage