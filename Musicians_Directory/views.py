from django.shortcuts import render
from Album.models import Album
from django.views.generic import ListView


class HomeView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'ans'
    queryset = Album.objects.select_related('musician').all()
    
    