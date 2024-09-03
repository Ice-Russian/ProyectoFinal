
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  PostForm
from .models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()

    return render(request, 'profile_post/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        # Verificar si se ha solicitado eliminar el archivo
        if 'delete_image' in request.POST and request.POST['delete_image'] == 'true':
            if post.media:
                post.media.delete(save=False)  # Elimina el archivo de disco
            post.media = None  # Elimina la referencia en el modelo
            post.save()  # Guarda el modelo sin el archivo

        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')  # O la URL que corresponda
    else:
        form = PostForm(instance=post)

    return render(request, 'profile_post/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    return render(request, 'profile_post/delete_post.html', {'post': post})