from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:home')

@login_required
def profile(request):
    from progress.models import UserProgress
    from journals.models import JournalEntry
    from reflections.models import UserResponse
    
    # Get or create user progress
    progress, created = UserProgress.objects.get_or_create(user=request.user)
    
    # Get recent journal entries
    recent_journals = JournalEntry.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    # Get recent reflections
    recent_reflections = UserResponse.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    context = {
        'progress': progress,
        'recent_journals': recent_journals,
        'recent_reflections': recent_reflections,
    }
    return render(request, 'users/profile.html', context)
