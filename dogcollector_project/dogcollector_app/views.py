from django.shortcuts import render
from .models import Dog #don't forget to import data from database


# dogs = [
#   {'name': 'Mello', 'breed': 'husky', 'description': 'beautiful fur and playful husky', 'age': 3},
#   {'name': 'Blu', 'breed': 'husky and corgi mix', 'description': 'full energy and need lots of love', 'age': 4},
#   {'name': 'Oli', 'breed': 'golden retriver', 'description': 'friendly and only need pat', 'age': 5},
#   {'name': 'Luigi', 'breed': 'terrier and dachshund mix', 'description': 'lap dog and food looker', 'age': 15 },
#   {'name': 'Pak gard', 'breed': 'Bangkaew', 'description': 'playful and smiley', 'age': 10},
# ]


# Create your views here.
# these are function
def home(request):
    return render(request, 'dogs/home.html')

#Define another route with a path of about/. The path's trailing slash instead of a leading slash is the Django way and is critical to follow.
def about(request):
    return render(request, 'dogs/about.html')


def dogs_index(request):
  dogs = Dog.objects.all() #import from database
  return render(request, 'dogs/index.html', {'dogs' : dogs})


def dogs_detail(request, dog_id): #The dogs_detail function is using the get method to obtain the dog object by its id.
  dog = Dog.objects.get(id=dog_id) #dog id match with ID 
  return render(request, 'dogs/detail.html', { 'dog': dog })