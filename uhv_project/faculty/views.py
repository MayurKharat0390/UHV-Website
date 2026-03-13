from django.shortcuts import render
from .models import FacultyProfile

def faculty_list(request):
    try:
        faculty_members = list(FacultyProfile.objects.all())
    except Exception:
        faculty_members = []
    return render(request, 'faculty/list.html', {'faculty_members': faculty_members})
