import datetime

from _typeshed import Incomplete

class Auth:
    client_id: str | None
    client_secret: str | None
    access_token: str | None
    refresh_token: str | None
    token_expiration: datetime.datetime | str | None
    redirect_uri: str
    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        token_expiration: datetime.datetime | str | None = None,
    ) -> None: ...
    def get_authorization(self) -> str: ...
    def get_api_key(self) -> str: ...
    def update(self, **kwargs) -> None: ...
