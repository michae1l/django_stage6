from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,"index/index.html")

def beauty(request):
    return render(request,"index/beauty.html")

def contact(request):
    return render(request,"index/contact.html")

def fashion(request):
    return render(request,"index/fashion.html")