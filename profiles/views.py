from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ChangeDetailsForm, ChangePasswordForm


@login_required
def profile_view(request):
    # Assuming the user is logged in and their profile exists
    user = request.user
    profile = UserProfile.objects.get(user=user)
    return render(request, 'account/profile.html', {'user': user, 'profile': profile})


@login_required
def account_settings(request):
    if request.method == 'POST':
        details_form = ChangeDetailsForm(request.POST, instance=request.user)
        password_form = ChangePasswordForm(request.user, request.POST)
        if details_form.is_valid() and password_form.is_valid():
            details_form.save()
            password_form.save()
            return redirect('profiles:profile')  # Redirect to the user's profile page after successful change
    else:
        details_form = ChangeDetailsForm(instance=request.user)
        password_form = ChangePasswordForm(request.user)
    return render(request, 'account/account_settings.html', {'details_form': details_form, 'password_form': password_form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('core:home') 
    return render(request, 'account/delete_account.html')
