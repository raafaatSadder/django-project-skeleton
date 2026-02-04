class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to run before the view

        response = self.get_response(request)
        # Code to run after the view

        return response
