from _typeshed import Incomplete

class RequestHandler:
    auth: Incomplete
    user_agent: Incomplete
    base_url: Incomplete
    def __init__(self, auth, data_center: Incomplete | None = None) -> None: ...
    def get(
        self,
        endpoint: str = "",
        url: str = "",
        params: Incomplete | None = None,
        use_api_key: bool = False,
    ): ...
    def delete(
        self,
        endpoint: str = "",
        url: str = "",
        params: Incomplete | None = None,
        data: Incomplete | None = None,
    ): ...
    def post(
        self,
        endpoint: str = "",
        url: str = "",
        data: Incomplete | None = None,
        use_api_key: bool = False,
        omit_api_version: bool = False,
    ): ...
