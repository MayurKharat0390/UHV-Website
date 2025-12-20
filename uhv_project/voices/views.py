from django.shortcuts import render, redirect
from .models import StudentVoice
from .forms import VoiceForm

def voice_list(request):
    voices = StudentVoice.objects.filter(is_approved=True).order_by('-created_at')
    
    if request.method == 'POST':
        form = VoiceForm(request.POST)
        if form.is_valid():
            voice = form.save(commit=False)
            if request.user.is_authenticated:
                voice.user = request.user
            # If user wants anonymity, they can set name_display to 'Anonymous' in form, or we handle it.
            # Let's assume the form handles name_display.
            voice.save()
            return redirect('voices:list')
    else:
        form = VoiceForm()

    return render(request, 'voices/list.html', {'voices': voices, 'form': form})
