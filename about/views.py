from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

def about_view(request):
    return render(request, 'about/about.html')
