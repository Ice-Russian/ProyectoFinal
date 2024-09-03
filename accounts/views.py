from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm, UserForm
from .models import UserProfile
from profile_post.models import Post


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user)
            # Create a UserProfile instance
            UserProfile.objects.create(
                user=user,
                profile_image=form.cleaned_data.get('profile_image'),
                biography=form.cleaned_data.get('biography')
            )
            # Redirect to the success page or profile page
            return redirect('register_success')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid login'})
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    posts = Post.objects.filter(user=request.user)  

    return render(request, 'accounts/profile.html', {'user_profile': user_profile, 'posts': posts})

@login_required
def profile_edit(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=user_profile, data=request.POST, files=request.FILES)

        # Procesar eliminación de la imagen de perfil
        if 'delete_profile_image' in request.POST:
            user_profile.profile_image.delete(save=False)  # Elimina el archivo de la imagen
            user_profile.profile_image = None  # Establece el campo a None
            user_profile.save()  # Guarda los cambios en el modelo
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def register_success(request):
    return render(request, 'accounts/register_success.html')
