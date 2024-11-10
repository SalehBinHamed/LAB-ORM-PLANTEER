from django.urls import path 
from . import views


app_name = 'plant'
urlpatterns = [

    path('',views.home_views,name="home"),
    path('all/', views.all_views,name='all_views'),
    path('search/', views.search_views ,name="search_views"),
    path('details/<int:plant_id>/', views.details_views, name='details_views'),
    path('create/', views.create_views, name="create_views"),
    path('delete/<int:plant_id>/', views.delete_views, name='delete'),
    path('update/<int:plant_id>/', views.update_views, name='update'),


]