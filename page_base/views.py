from django.shortcuts import render

def about_view(request):
    return render(request, 'page_base/aboutme.html')

def inicio(request):
    return render(request, 'page_base/index.html')
