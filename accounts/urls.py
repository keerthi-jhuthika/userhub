from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),            # Root of accounts app
    path('dashboard/', views.dashboard_view, name='dashboard'),
]