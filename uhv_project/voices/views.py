from django.shortcuts import render, redirect
from .models import StudentVoice, StoryMedia
from .forms import VoiceForm

def voice_list(request):
    voices = StudentVoice.objects.filter(is_approved=True).prefetch_related('media').order_by('-created_at')
    
    if request.method == 'POST':
        form = VoiceForm(request.POST, request.FILES)
        if form.is_valid():
            voice = form.save(commit=False)
            if request.user.is_authenticated:
                voice.user = request.user
            # If user wants anonymity, they can set name_display to 'Anonymous' in form, or we handle it.
            # Let's assume the form handles name_display.
            voice.save()

            # Handle multiple file uploads
            files = request.FILES.getlist('media')
            for f in files:
                StoryMedia.objects.create(story=voice, file=f)

            return redirect('voices:list')
    else:
        form = VoiceForm()

    return render(request, 'voices/list.html', {'voices': voices, 'form': form})
