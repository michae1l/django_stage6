## app (web_app)

from django.urls import path
from .views import index, beauty, contact, fashion

urlpatterns = [
    path('',index),
    path('beauty/contact',beauty),
    path('contact/',contact),
    path('fashion/',fashion)
]