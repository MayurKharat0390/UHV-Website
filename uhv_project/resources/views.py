from django.shortcuts import render
from .models import Resource

def resource_list(request):
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        resources = Resource.objects.all()
    else:
        resources = Resource.objects.filter(category=category)
    
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
    resource = Resource.objects.get(pk=pk)
    resource.views_count += 1
    resource.save()
    
    context = {'resource': resource}
    return render(request, 'resources/detail.html', context)
