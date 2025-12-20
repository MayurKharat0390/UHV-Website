from django import forms
from .models import StudentVoice

class VoiceForm(forms.ModelForm):
    class Meta:
        model = StudentVoice
        fields = ['name_display', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your reflection (100-150 words)...'}),
            'name_display': forms.TextInput(attrs={'placeholder': 'Your Name or Anonymous'})
        }
