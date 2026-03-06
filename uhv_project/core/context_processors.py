from .models import NewsUpdate

def news_ticker(request):
    updates = NewsUpdate.objects.filter(is_active=True).order_by('order', '-created_at')
    return {
        'ticker_updates': updates
    }
