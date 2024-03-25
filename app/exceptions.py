from fastapi import HTTPException
from fastapi import status


class BaseHTTPException(HTTPException):
    status_code = 500

    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UnauthorizedException(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "UNAUTHORIZED"


class AddSongException(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Adding error"


class FindSimilarSongsException(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Recommendations error"


class SongsAddedMessage(BaseHTTPException):
    status_code = status.HTTP_201_CREATED
    detail = "Songs added successfully"
