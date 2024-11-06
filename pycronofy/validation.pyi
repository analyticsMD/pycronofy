from _typeshed import Incomplete

ISO_8601_FORMATS: Incomplete
ISO_8601_REGEX: Incomplete
METHOD_RULES: Incomplete

def check_exists_in_object(method, obj, required_fields) -> None: ...
def check_datetime(
    method, dictionary, fields, label: Incomplete | None = None
) -> None: ...
def check_exists_in_dictionary(
    method, dictionary, required_fields, label: Incomplete | None = None
) -> None: ...
def validate(method, auth, *args, **kwargs) -> None: ...
