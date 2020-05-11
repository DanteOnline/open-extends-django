from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import FilePath
from .forms import FilePathForm


class FilePathCreateView(CreateView):
    model = FilePath
    form_class = FilePathForm
    success_url = reverse_lazy('mainapp:index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_paths'] = FilePath.objects.all()
        return context

