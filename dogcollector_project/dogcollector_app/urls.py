from django.urls import path
from . import views     # .  is everything from views


urlpatterns = [
    path('', views.home, name='home'),  # '' leaving that empty, it's home page. views.home is views.py
    path('about/', views.about, name='about'),  #Map the route to a view named views.about.
    path('dogs/', views.dogs_index, name='index'),

    #Below is new route to show page each ID
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
]