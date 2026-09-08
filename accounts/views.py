from django.shortcuts import render

def signup_view(request):
    return render(request, 'accounts/index.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')