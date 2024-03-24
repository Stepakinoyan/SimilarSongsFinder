from spotipy.oauth2 import SpotifyOAuth
from app.config import settings


oauth = SpotifyOAuth(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    scope=['playlist-modify-private','playlist-modify-public', 'playlist-read-private'],
    redirect_uri="http://localhost:8000/auth/authorize",
)