from rest_framework.exceptions import APIException

CRITICAL = 50
ERROR = 40
NOTSET = 0

class UMSAPIException(APIException):
    severity = CRITICAL

    def __init__(self, detail=None, code=None):
        if code is None:
            code = self.default_code
        self.code = code

        super(UMSAPIException, self).__init__(detail=detail, code=code)


class ResourceException(UMSAPIException):
    severity = ERROR
    status_code = 422
    default_code = "RESOURCE_EXCEPTION"


class ValidationException(UMSAPIException):
    severity = ERROR
    status_code = 400
    default_code = "VALIDATION_EXCEPTION"


class NotFoundException(UMSAPIException):
    severity = ERROR
    status_code = 404
    default_code = "NOT_FOUND_EXCEPTION"


class DatabaseException(UMSAPIException):
    severity = CRITICAL
    status_code = 500
    default_code = "DATABASE_EXCEPTION"
