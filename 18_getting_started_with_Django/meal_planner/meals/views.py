from django.shortcuts import render

def index(request):
    """The home page for Meal."""
    return render(request, 'meals/index.html')

