
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from blog.forms import BlogForm

def inicio(request):
    return render(request, 'blog/index.html')

def pages_list(request):
    blogs = Blog.objects.all()
    if not blogs:
        return render(request, 'blog/no_pages.html')
    return render(request, 'blog/pages_list.html', {'blogs': blogs})

def page_detail(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)
    return render(request, 'blog/page_detail.html', {'blog': blog})

def page_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages_list')
    else:
        form = BlogForm()
    return render(request, 'blog/page_form.html', {'form': form})

def page_edit(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('page_detail', page_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/page_form.html', {'form': form})

def page_delete(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('pages_list')
    return render(request, 'blog/page_confirm_delete.html', {'blog': blog})
# Ruta about
def about_view(request):
    return render(request, 'admin_user/about.html')