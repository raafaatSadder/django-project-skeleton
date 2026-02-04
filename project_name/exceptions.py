from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Custom exception handler
    to customize error responses
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "error": response.data,
        }

    return response
