from .models import ContactMessage
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control glass-input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control glass-input', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control glass-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control glass-input', 'rows': 5, 'placeholder': 'Your Message'}),
        }