from django.urls import path
from .views import SignUpView, PostCreateView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
]