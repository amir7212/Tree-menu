from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("category/<slug:menu_slug>", menu,name="menu_slug")
    ]
