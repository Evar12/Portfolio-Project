from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text',]
    success_url = '/mit/notes'
    template_name = 'notes/notes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

