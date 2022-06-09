from django.http import JsonResponse
from rest_framework import status

def SuccessResponse(data: dict):
    return JsonResponse({
        "status": 1,
        "data": data
    })

def ErrorResponse(errors, _status: status, request = None, error_id = None):

    # Store Exception
    errors = [error.json() for error in errors]
    error = None

    return JsonResponse({
        "status": 0,
        'errors': errors,
        'error_id': error.id if error is not None else error_id
    }, status=_status)
