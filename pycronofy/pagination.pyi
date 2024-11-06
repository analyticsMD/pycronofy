from typing import Any, TypedDict

from _typeshed import Incomplete
from typing_extensions import Self

Options = TypedDict(
    "Options", {"delete": bool, "update": bool, "change_participation_status": bool}
)

Organizer = TypedDict("Organizer", {"email": str, "display_name": None})

Attendee = TypedDict("Attendee", {"email": str, "display_name": None, "status": str})

CronofyEvent = TypedDict(
    "CronofyEvent",
    {
        "calendar_id": str,
        "event_uid": str,
        "summary": str,
        "description": str,
        "start": str,
        "end": str,
        "deleted": bool,
        "created": str,
        "updated": str,
        "event_private": bool,
        "participation_status": str,
        "attendees": list[Attendee],
        "organizer": Organizer,
        "transparency": str,
        "extended_transparency": str,
        "status": str,
        "categories": list[Any],
        "recurring": bool,
        "series_identifier": str,
        "options": Options,
    },
)

PagesPayload = TypedDict(
    "PagesPayload", {"current": int, "total": int, "next_page": str}
)

EventPagesPayload = TypedDict(
    "EventPagesPayload", {"pages": Pages, "events": list[CronofyEvent]}
)

class Pages:
    request_handler: Incomplete
    current: int
    total: int
    next_page_url: str
    data_type: str
    data: dict[str, Any]
    index: int
    length: Incomplete
    automatic_pagination: bool
    def __init__(
        self, request_handler, data, data_type, automatic_pagination: bool = True
    ) -> None: ...
    def all(self) -> list[CronofyEvent]: ...
    def current_page(self) -> list[CronofyEvent]: ...
    def fetch_next_page(self) -> None: ...
    def json(self) -> EventPagesPayload: ...
    def next(self) -> CronofyEvent: ...
    def __delitem__(self, idx) -> None: ...
    def __getitem__(self, idx): ...
    def __iter__(self) -> Self: ...
    def __len__(self) -> int: ...
    def __next__(self) -> CronofyEvent: ...
    def __setitem__(self, idx, value) -> None: ...
