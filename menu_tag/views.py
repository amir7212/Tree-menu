from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu(request, menu_slug ):
    return render(request, "menu.html",{"cat_slug":menu_slug})

def index(request):
    return render (request, "menu.html",{"cat_slug":"main-category"})
