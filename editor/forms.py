from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove labels for all fields in the form
        for field_name, field in self.fields.items():
            field.label = ''
