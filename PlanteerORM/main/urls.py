from django.urls import path 
from . import views

app_name='main'
urlpatterns = [
    path('main/', views.home_massge,name="massge"),
    path('contact/', views.contact_views ,name="contact"),

]
