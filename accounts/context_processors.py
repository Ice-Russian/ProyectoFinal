# accounts/context_processors.py
from django.shortcuts import get_object_or_404
from .models import UserProfile

def user_profile(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        return {'user_profile': user_profile}
    return {}
