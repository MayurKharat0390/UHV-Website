from django.shortcuts import render, get_object_or_404
from .models import Activity

def activity_list(request):
    activities = Activity.objects.order_by('-date')
    return render(request, 'activities/list.html', {'activities': activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activities/detail.html', {'activity': activity})
