from django.urls import path
from . import views     # .  is everything from views


urlpatterns = [
    path('', views.home, name='home'),  # '' leaving that empty, it's home page. views.home is views.py
    path('about/', views.about, name='about'),  #Map the route to a view named views.about.


    ## DOG URLs ##
    path('dogs/', views.dogs_index, name='index'),
    #Below is new route to show page each ID
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    #new route used to show a form and create a dog
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    # add the two new routes for Update and Delete
    # Updating & Deleting Data Using a CBV (Class-Based Views)
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'), #pk is primary key
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),


    ## FEEDING & ACCESSORY URLS ##
    path('dogs/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dogs/<int:pk>/assoc_accessory/<int:accessory_pk>/', views.assoc_accessory, name='assoc_accessory'),


    ## All ACCESSORIES URLs ##
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]