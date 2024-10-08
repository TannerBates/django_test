from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, PostCreateForm
from .models import Post
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    success_url = reverse_lazy('home')
    template_name = 'post_form.html'
