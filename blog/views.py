from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from blog.forms import BlogForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

def pages_list(request):
    blogs = Blog.objects.all()
    if not blogs:
        return render(request, 'blog/no_pages.html')
    return render(request, 'blog/pages_list.html', {'blogs': blogs})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)  
            blog_post.author = request.user      
            blog_post.save()                     
            return redirect('success') 
    else:
        form = BlogForm()

    return render(request, 'blog/page_form.html', {'form': form})


@login_required
def page_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    # Pasa el objeto blog al template
    return render(request, 'blog/page_detail.html', {'blog': blog})

@login_required
def page_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author and not request.user.is_superuser:
        return redirect('pages_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('pages_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/page_edit.html', {'form': form})

@login_required
def page_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author and not request.user.is_superuser:
        return redirect('pages_list')

    if request.method == 'POST':
        blog.delete()
        return redirect('pages_list')

    return render(request, 'blog/page_delete.html', {'blog': blog})

@login_required
def page_success(request):
    return render(request, 'blog/success.html')




