from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView

from notes.models import Note

# Create your views here.

class NoteListView(ListView):
    model = Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['summary', 'details', 'done']
    success_url = reverse_lazy('index')

class NoteCreateView(CreateView):
    model = Note
    fields = ['summary', 'details', 'done']
    success_url = reverse_lazy('index')

def setdone(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.done = True
    note.save()
    return HttpResponseRedirect(reverse('index'))

def setundone(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.done = False
    note.save()
    return HttpResponseRedirect(reverse('index'))
