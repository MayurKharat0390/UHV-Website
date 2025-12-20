from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['content', 'mood', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 12,
                'placeholder': 'Reflect on your week... What did you learn? How did you grow? (Minimum 150 words)',
                'class': 'journal-content'
            }),
            'mood': forms.Select(attrs={
                'class': 'mood-select'
            }),
            'tags': forms.TextInput(attrs={
                'placeholder': 'e.g., growth, challenges, gratitude (comma-separated)'
            }),
        }
    
    def clean_content(self):
        """Validate that content has at least 150 words"""
        content = self.cleaned_data.get('content', '')
        word_count = len(content.split())
        
        if word_count < 150:
            raise forms.ValidationError(
                f'Journal entry must be at least 150 words. You have {word_count} words. '
                f'Please add {150 - word_count} more words.'
            )
        
        return content
