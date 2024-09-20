from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . forms import NotesForm

# Create your views here.
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/mit/notes'
    form_class = NotesForm
    # template_name = 'notes/notes_form.html'

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text',]
    success_url = '/mit/notes'
    form_class = NotesForm
    template_name = 'notes/notes_form.html'

    
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

