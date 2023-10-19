from django.shortcuts import render
from .models import Dog #don't forget to import data from database
from django.views.generic.edit import CreateView, UpdateView, DeleteView #add import to CreateView, UpdateView and DeleteView


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

#Code for the view page each dog
def dogs_detail(request, dog_id): #The dogs_detail function is using the get method to obtain the dog object by its id.
  dog = Dog.objects.get(id=dog_id) #dog id match with ID 
  return render(request, 'dogs/detail.html', { 'dog': dog })


#class based 'VIEWS'
class DogCreate(CreateView):  #passed the (CreateView)
  #first thing to tell is 'model' 
  model = Dog
  #to tell what field to use. This one is '__all__' means to contain all of the Dog Model's attributes.
  fields = '__all__'
  # optional 1 way 
  #success_url = '/dogs/{dog_id}'


class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age', 'gender', 'color', 'favorite_toy']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'