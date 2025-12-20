from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from .forms import JournalEntryForm

@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journals/list.html', {'entries': entries})

@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            
            # Update progress
            from progress.models import UserProgress
            progress, created = UserProgress.objects.get_or_create(user=request.user)
            progress.total_journal_entries = JournalEntry.objects.filter(user=request.user).count()
            progress.save()
            
            return redirect('journals:list')
    else:
        form = JournalEntryForm()
    return render(request, 'journals/create.html', {'form': form})

@login_required
def journal_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journals/detail.html', {'entry': entry})
