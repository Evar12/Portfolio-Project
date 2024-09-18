from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, DetailView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

