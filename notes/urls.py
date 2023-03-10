from django.urls import path

from notes.views import NoteCreateView, NoteUpdateView, NoteListView, setdone, setundone

urlpatterns = [
    path("", NoteListView.as_view(), name="index"),
    path("setdone/<int:pk>", setdone, name="setdone"),
    path("setundone/<int:pk>", setundone, name="setundone"),
    path("create", NoteCreateView.as_view(), name="create"),
    path("<int:pk>", NoteUpdateView.as_view(), name="detail"),
]
