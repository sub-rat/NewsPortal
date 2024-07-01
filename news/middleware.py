from news.models import News


class RouteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.record_route_visit(request, response)
        return response

    def record_route_visit(self, request, response):
        path = str.replace(request.path, '/', '_')
        key = f'{path.__str__()}_{request.method}'
        count = request.COOKIES.get(key, 0)
        response.cookies[key] = int(count) + 1
        # RouteVisit.objects.create(
        #     path=request.path,
        #     method=request.method,
        #     timestamp=datetime.datetime.now()
        # )
