from django.shortcuts import render
from .models import FacultyProfile

def faculty_list(request):
    faculty_members = FacultyProfile.objects.all()
    return render(request, 'faculty/list.html', {'faculty_members': faculty_members})
