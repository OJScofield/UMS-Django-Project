from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException


def custom_response(data, message_code, message_detail, status_code, headers=None, exception=False):

    response_data = {
        'message_code': message_code,
        'message_detail': message_detail,
        'data': data
    }

    return Response(response_data, status=status_code, headers=headers, exception=exception)


def ums_exception_handler(exc, context):
    headers = None
    message_code = None
    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        request_method = getattr(getattr(context['request'], '_request', {}), 'method', '').lower()
        view_action = getattr(context['view'],
                              context['view'].action if context['view'].action else request_method,
                              None)

        if hasattr(view_action, 'deprecation_date'):
            headers['Deprecation'] = view_action.deprecation_date
        if hasattr(view_action, 'sunset_date'):
            headers['Sunset'] = view_action.sunset_date

        message_detail = exc.detail
        message_code = getattr(exc, 'code', None)
        status_code = exc.status_code

    elif isinstance(exc, Http404):
        message_detail = 'Not found.'
        status_code = status.HTTP_404_NOT_FOUND

    elif isinstance(exc, PermissionDenied):
        message_detail = 'Permission denied.'
        status_code = status.HTTP_403_FORBIDDEN

    else:
        message_detail = str(exc)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return custom_response({}, message_code=message_code, message_detail=message_detail, status_code=status_code, headers=headers, exception=True)