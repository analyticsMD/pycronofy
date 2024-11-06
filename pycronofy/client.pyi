import datetime
from typing import Any, List, Optional, TypedDict, Union

from _typeshed import Incomplete
from pycronofy.auth import Auth
from pycronofy.batch import BatchBuilder, BatchResponse
from pycronofy.pagination import Pages
from pycronofy.request_handler import RequestHandler


class AvailabilityOptional(TypedDict, total=False):
    max_results: int
    response_format: str

class Availability(AvailabilityOptional):
    participants: dict                    
    required_duration: dict                   
    available_periods: dict
    start_interval: int
    buffer: dict 


class OAuthParam(TypedDict):
    scope: str             
    redirect_uri: str            
    state: str
                        


class CallbackURLs(TypedDict):
    completed_url: str                      
    no_times_suitable_url: str             
    no_times_displayed_url : str

class RedirectURLs(TypedDict):
    completed_url: str


class Recipient(TypedDict):
    email: str

class AuthorizationFromCode(TypedDict):
    access_token: str
    refresh_token: str
    token_expiration: str

ProfileCalendar = TypedDict(
    "ProfileCalendar",
    {
        "calendar_id": str,
        "calendar_name": str,
        "calendar_readonly": bool,
        "calendar_deleted": bool,
        "calendar_primary": bool,
        "calendar_integrated_conferencing_available": bool,
        "calendar_attachments_available": bool,
        "permission_level": str,
    },
)

Profile = TypedDict(
    "Profile",
    {
        "provider_name": str,
        "provider_service": str,
        "profile_id": str,
        "profile_name": str,
        "profile_connected": bool,
        "profile_initial_sync_required": bool,
        "profile_calendars": List[ProfileCalendar],
    },
)

Authorization = TypedDict("Authorization", {"scope": str, "status": str})

CronofyData = TypedDict(
    "CronofyData",
    {
        "authorization": Authorization,
        "profiles": List[Profile],
        "conferencing_profiles": List[Any],
    },
)

UserInfo = TypedDict(
    "UserInfo",
    {
        "sub": str,
        "email": str,
        "name": str,
        "zoneinfo": str,
        "cronofy.type": str,
        "cronofy.data": CronofyData,
    },
)

Conferencing = TypedDict("Conferencing", {"profile_id": str})

class Offset(TypedDict):
    minutes: int

class Transition(TypedDict):
    before: str
    offset: Offset

class Subscription(TypedDict):
    type: str
    uri: str
    transitions: list[Transition]

class Private(TypedDict):
    value: str

class Tags(TypedDict):
    private: list[Private]

class InviteOrRemoveOptional(TypedDict, total=False):
    display_name: str

class InviteOrRemove(InviteOrRemoveOptional):
    email: str

class Attendees(TypedDict):
    invite: list[InviteOrRemove]
    remove: list[InviteOrRemove]

class Reminder(TypedDict):
    minutes: int

class EventParametersLocation(TypedDict):
    description: str

class RuleOptional(TypedDict, total=False):
    interval: int
    count: int
    until: str
    by_day: list[str]
    exceptions: dict[str, list[dict[str, str]]]

class Rule(RuleOptional):
    frequency: str

class Rules(TypedDict):
    rule: list[Rule]

class EventParametersOptional(TypedDict, total=False):
    description: str
    location: EventParametersLocation
    event_private: bool
    conferencing: Conferencing
    subscriptions: list[Subscription]
    locale: str
    include_userinfo: bool
    tags: Private
    attendees: list[Attendees]
    reminders: list[Reminder]
    recurrence: Rules

class EventParameters(EventParametersOptional):
    event_id: str
    summary: str
    start: str
    end: str
    tzid: str

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
    "EventPagesPayload", {"pages": PagesPayload, "events": list[CronofyEvent]}
)

ChannelFilters = TypedDict(
    "ChannelFilters", {"calendar_ids": list[str], "only_managed": bool}
)

Channel = TypedDict(
    "Channel", {"channel_id": str, "callback_url": str, "filters": ChannelFilters}
)

Notification = TypedDict("Notification", {"type": str, "changes_since": str})

CronofyWebhookData = TypedDict(
    "CronofyWebhookData", {"notification": Notification, "channel": Channel}
)

EmptyResponse = TypedDict("EmptyResponse", {})

Calendar = TypedDict(
    "Calendar",
    {
        "provider_name": str,
        "profile_id": str,
        "profile_name": str,
        "calendar_id": str,
        "calendar_name": str,
        "calendar_readonly": bool,
        "calendar_deleted": bool,
    },
)
CalendarResponse = TypedDict("CalendarResponse", {"calendar": Calendar})

LinkingProfile = TypedDict(
    "LinkingProfile", {"provider_name": str, "profile_id": str, "profile_name": str}
)

class ApplicationCalendarOptional(TypedDict, total=False):
    linking_profile: LinkingProfile

class ApplicationCalendar(ApplicationCalendarOptional):
    token_type: str
    access_token: str
    expires_in: int
    refresh_token: str
    scope: str
    application_calendar_id: str
    sub: str


class Client:
    auth: Auth
    request_handler: RequestHandler
    app_base_url: str
    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        token_expiration: datetime.datetime | str | None = None,
        data_center: str | None = None,
    ) -> None: ...
    def account(self) -> dict[str, Any]: ...
    def userinfo(self) -> UserInfo: ...
    def close_notification_channel(self, channel_id) -> None: ...
    def change_participation_status(self, calendar_id, event_uid, status) -> None: ...
    def create_notification_channel(
        self, callback_url, calendar_ids=(), only_managed: bool = False
    ): ...
    def delete_all_events(self, calendar_ids=()) -> None: ...
    def delete_event(self, calendar_id, event_id) -> None: ...
    def delete_external_event(self, calendar_id, event_uid) -> None: ...
    def elevated_permissions(
        self, permissions, redirect_uri: Incomplete | None = None
    ): ...
    def upsert_smart_invite(
        self,
        smart_invite_id,
        recipient,
        event,
        callback_url: Incomplete | None = None,
        organizer: Incomplete | None = None,
    ): ...
    def get_smart_invite(self, smart_invite_id: str, recipient_email: str): ...
    def cancel_smart_invite(self, smart_invite_id: str, recipient: Recipient): ...
    def get_authorization_from_code(
        self, code: str, redirect_uri: str = ""
    ) -> AuthorizationFromCode: ...
    def application_calendar(
        self, application_calendar_id: str
    ) -> ApplicationCalendar: ...
    def is_authorization_expired(self): ...
    def list_calendars(self) -> list[Calendar]: ...
    def list_profiles(self): ...
    def list_notification_channels(self): ...
    def resources(self): ...
    def read_events(
        self,
        calendar_ids:tuple[str]|list[str]=tuple(),
        from_date: datetime.datetime | datetime.date | str | None = None,
        to_date: datetime.datetime | datetime.date | str | None = None,
        last_modified: datetime.datetime | str | None = None,
        tzid=str|None,
        only_managed: bool = False,
        include_managed: bool = True,
        include_deleted: bool = False,
        include_moved: bool = False,
        include_geo: bool = False,
        localized_times: bool = False,
        automatic_pagination: bool = True,
    ) -> Pages: ...
    def read_free_busy(
        self,
        calendar_ids:tuple[str]|list[str]=tuple(),
        from_date: datetime.datetime | datetime.date | str | None = None,
        to_date: datetime.datetime | datetime.date | str | None = None,
        last_modified: datetime.datetime | str | None = None,
        tzid=str|None,
        include_managed: bool = True,
        localized_times: bool = False,
        automatic_pagination: bool = True,
    ): ...
    def availability(
        self,
        participants=(),
        required_duration=dict[str, int]|int,
        available_periods: Incomplete | None = None,
        start_interval: Incomplete | None = None,
        buffer=(),
        response_format: Incomplete | None = None,
        query_slots: Incomplete | None = None,
        max_results: Incomplete | None = None,
    ): ...
    def sequenced_availability(self, sequence=(), available_periods=()): ...
    def refresh_authorization(self): ...
    def revoke_authorization(self) -> None: ...
    def revoke_profile(self, profile_id: str) -> None: ...
    def upsert_event(
        self, calendar_id: str, event: EventParameters
    ) -> Union[EmptyResponse, UserInfo]: ...
    def authorize_with_service_account(
        self, email: str, scope: str, callback_url: str, state: str | None = None
    ) -> None: ...
    def authorize_multiple_accounts_via_service_account(
        self, service_account_authorizations, state: str | None = None
    ) -> None: ...
    def real_time_scheduling(
        self,
        availability: Availability,
        oauth: OAuthParam,
        event,
        target_calendars=(),
        minimum_notice: dict[str, Any] | None = None,
        callback_url: str | None = None,
        callback_urls: CallbackURLs | None = None,
        redirect_urls: RedirectURLs | None = None,
        event_creation: str | None = None,
    ): ...
    def get_real_time_scheduling_status(
        self,
        token: str | None = None,
        real_time_scheduling_id: str | None = None,
    ): ...
    def disable_real_time_scheduling_link(
        self, real_time_scheduling_id: str, display_message: str
    ): ...
    def real_time_sequencing(
        self,
        availability: Availability,
        oauth: OAuthParam,
        event,
        target_calendars=(),
        minimum_notice: dict[str, Any] | None = None,
    ): ...
    def user_auth_link(
        self,
        redirect_uri: str,
        scope: str = "",
        state: str = "",
        provider_name: str = "",
        avoid_linking: bool = False,
    ) -> str: ...
    def validate(self, method, *args, **kwargs) -> None: ...
    def batch(self, builder: BatchBuilder) -> BatchResponse: ...
    def translate_available_periods(self, periods) -> None: ...
    def translate_query_slots(self, query_slots) -> None: ...
    def map_availability_sequence(self, sequence): ...
    def map_availability_buffer(self, buffer): ...
    def map_buffer_details(self, buffer): ...
    def map_sequence_item(self, sequence_item): ...
    def map_availability_participants(self, participants): ...
    def map_availability_participants_group(self, participants): ...
    def map_availability_member(self, member): ...
    def map_availability_duration(self, required_duration): ...
    def create_calendar(
        self,
        profile_id: str,
        calendar_name: str,
        error_on_duplicate: bool = True,
        color: Optional[str] = None,
    ) -> CalendarResponse: ...
    def upsert_availability_rule(self, availability_rule): ...
    def list_availability_rules(self): ...
    def get_availability_rule(self, availability_rule_id): ...
    def delete_availability_rule(self, availability_rule_id) -> None: ...
    def hmac_valid(self, hmac_string, body): ...
    def get_conferencing_services_auth_link(
        self, redirect_uri, provider_name: Incomplete | None = None
    ): ...
    def get_ui_element_token(self, permissions, subs, origin, version: str = "1"): ...
