from django import forms
from .models import FilePath


# def path_validator(value):
#     if not value.startswith('/'):
#         raise forms.ValidationError("f Путь должен начинаться со /")


# class PathField(forms.CharField):
#     # default_validators = [path_validator]
#
#     def validate(self, value):
#         super().validate(value)
#         if not value.startswith('/'):
#             raise forms.ValidationError("f Путь должен начинаться со /")


class FilePathForm(forms.ModelForm):
    # path = forms.CharField(validators=[path_validator])
    path = forms.CharField()
    # path = PathField()

    class Meta:
        model = FilePath
        fields = '__all__'

    # def clean_path(self):
    #     path = self.cleaned_data['path']
    #     if not path.startswith('/'):
    #         raise forms.ValidationError("Путь должен начинаться со /")
    #     return path

    # def clean(self):
    #     cleaned_data = super().clean()
    #     path = cleaned_data['path']
    #     if not path.startswith('/'):
    #         raise forms.ValidationError("Путь должен начинаться со /")
