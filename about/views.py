from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import AboutUs
from .forms import AboutUsForm

# Create your views here.

@staff_member_required
def create_about_us(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_us:create')
    else:
        form = AboutUsForm()
    return render(request, 'about_us/create_about_us.html', {'form': form})

@staff_member_required
def edit_about_us(request, pk):
    about_us = get_object_or_404(AboutUs, pk=pk)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('about_us:create')
    else:
        form = AboutUsForm(instance=about_us)
    return render(request, 'about_us/edit_about_us.html', {'form': form})