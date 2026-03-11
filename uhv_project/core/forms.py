from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl border-2 border-gray-100 focus:border-primary-500 focus:ring-4 focus:ring-primary-500/10 transition-all outline-none text-lg bg-gray-50/50',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl border-2 border-gray-100 focus:border-primary-500 focus:ring-4 focus:ring-primary-500/10 transition-all outline-none text-lg bg-gray-50/50',
                'placeholder': 'your@email.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl border-2 border-gray-100 focus:border-primary-500 focus:ring-4 focus:ring-primary-500/10 transition-all outline-none text-lg bg-gray-50/50',
                'placeholder': 'What can we help with?'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl border-2 border-gray-100 focus:border-primary-500 focus:ring-4 focus:ring-primary-500/10 transition-all outline-none text-lg bg-gray-50/50 min-h-[150px]',
                'placeholder': 'Tell us more about your inquiry...'
            }),
        }
