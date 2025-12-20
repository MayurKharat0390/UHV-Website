import random
from quotes.models import Quote

def daily_quote(request):
    """Add a random quote to all templates"""
    quotes = Quote.objects.filter(is_active=True)
    if quotes.exists():
        quote = random.choice(quotes)
        return {'daily_quote': quote}
    return {'daily_quote': None}
