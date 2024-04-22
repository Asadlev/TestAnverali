from django.urls import path
from .views import profile_view, profile_success_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('profile/success/', profile_success_view, name='profile_success'),
]