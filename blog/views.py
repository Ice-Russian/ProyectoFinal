from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from blog.forms import BlogForm
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, UpdateView
def inicio(request):
    return render(request, 'blog/index.html')

def pages_list(request):
    blogs = Blog.objects.all()
    if not blogs:
        return render(request, 'blog/no_pages.html')
    return render(request, 'blog/pages_list.html', {'blogs': blogs})

def page_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('success')  
    else:
        form = BlogForm()

    return render(request, 'blog/page_form.html', {'form': form})
class PageDetailView(DetailView):
    model = Blog
    template_name = 'blog/page_detail.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'page_id'
class PageUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/page_edit.html'
    success_url = '/success/' 

def page_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author:
        return render(request, 'blog/success.html', {'blog': blog})

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('pages_list')  # Redirige a la lista de blogs
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/page_edit.html', {'form': form})

class PageDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')  # Ajusta 'pages_list' al nombre correcto de tu URL

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Blog, pk=pk)
    

def form_valid(self, form):
    form.save()
    return redirect(reverse('page_detail', kwargs={'page_id': self.object.id}))

def page_success(request):
    return render(request, 'blog/success.html')

def about_view(request):
    return render(request, 'blog/about.html')
