from django.shortcuts import render
from .models import Resource

def resource_list(request):
    category = request.GET.get('category', 'all')
    
    try:
        if category == 'all':
            resources = list(Resource.objects.all())
        else:
            resources = list(Resource.objects.filter(category=category))
    except Exception:
        resources = []
    
    categories = [
        ('all', 'All Resources'),
        ('integrity', 'Integrity'),
        ('responsibility', 'Responsibility'),
        ('trust', 'Trust'),
        ('respect', 'Respect'),
        ('harmony', 'Harmony'),
        ('general', 'General'),
    ]
    
    context = {
        'resources': resources,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'resources/list.html', context)

def resource_detail(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
        resource.views_count += 1
        # Try-save but catch if DB is readonly
        try:
            resource.save()
        except Exception:
            pass
    except Exception:
        from django.http import Http404
        raise Http404("Resource not found or DB error")
    
    context = {'resource': resource}
    return render(request, 'resources/detail.html', context)
