from django import forms
from .models import StudentVoice

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'multiple': True, 'accept': 'image/*,video/*'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class VoiceForm(forms.ModelForm):
    media = MultipleFileField(
        required=False,
        label="Photos / Videos",
        help_text="Upload optional photos or videos to accompany your story."
    )

    class Meta:
        model = StudentVoice
        fields = ['name_display', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your impact story (100-150 words)...'}),
            'name_display': forms.TextInput(attrs={'placeholder': 'Your Name or Anonymous'})
        }
