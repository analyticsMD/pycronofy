from _typeshed import Incomplete

class PyCronofyException(Exception): ...

class PyCronofyDateTimeError(PyCronofyException):
    argument: Incomplete
    message: Incomplete
    def __init__(self, message, argument) -> None: ...

class PyCronofyRequestError(PyCronofyException):
    message: Incomplete
    request: Incomplete
    response: Incomplete
    def __init__(self, request, response) -> None: ...

class PyCronofyValidationError(PyCronofyException):
    message: Incomplete
    method: Incomplete
    fields: Incomplete
    values: Incomplete
    def __init__(
        self,
        message,
        method,
        fields: Incomplete | None = None,
        values: Incomplete | None = None,
    ) -> None: ...

class PyCronofyPartialSuccessError(PyCronofyException):
    message: Incomplete
    batch_response: Incomplete
    def __init__(self, message, batch_response) -> None: ...
