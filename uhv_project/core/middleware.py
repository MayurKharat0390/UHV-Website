from .models import SiteVisitor
from django.utils import timezone

class VisitorTrackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if ip:
            visitor, created = SiteVisitor.objects.get_or_create(ip_address=ip)
            if not created:
                # If seen before, just update the last visit and increment count
                visitor.visit_count += 1
                visitor.save()

        response = self.get_response(request)
        return response
