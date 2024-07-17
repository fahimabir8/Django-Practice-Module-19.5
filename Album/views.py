from django.shortcuts import render,redirect
from . import forms 
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

# def add_album(request):
#     if request.method == "POST":
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')
        
#     else:
#         album_form = forms.AlbumForm()
#     return render(request, 'album.html' ,{'form' : album_form})

class AlbumCreationView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')

    return render(request, 'album.html' , {'form': album_form})
