from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy 
from django.contrib import messages 
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth import logout
from django.views import View
# Create your views here.

class AddMusicianView(CreateView):
    model = models.Musician
    template_name = 'musician.html'
    form_class = forms.MusicianForm 
    success_url = reverse_lazy('homepage')
    
    
class MusicianUpdateView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    
    
class DeleteMusicianView(DeleteView):
    model = models.Musician
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context

class UserLoginView(LoginView):
    template_name = 'register.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Information is incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('homepage')