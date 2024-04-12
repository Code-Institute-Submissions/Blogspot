from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    # Assuming the user is logged in and their profile exists
    user = request.user
    profile = UserProfile.objects.get(user=user)
    return render(request, 'account/profile.html', {'user': user, 'profile': profile})