from django.shortcuts import render, get_object_or_404
from .models import Innovation

def innovation_list(request):
    innovations = Innovation.objects.all()
    return render(request, 'innovations/list.html', {'innovations': innovations})

def innovation_detail(request, slug):
    innovation = get_object_or_404(Innovation, slug=slug)
    return render(request, 'innovations/detail.html', {'innovation': innovation})
