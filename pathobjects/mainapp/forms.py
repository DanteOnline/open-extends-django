from django import forms
from .models import FilePath

class FilePathForm(forms.ModelForm):
    class Meta:
        model = FilePath
        fields = '__all__'