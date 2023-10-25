from django.shortcuts import render, redirect #add redirect to redirect after create new feeding
from .models import Dog, Accessory #don't forget to import data from database
from .forms import FeedingForm # Import the FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView #add import to CreateView, UpdateView and DeleteView
from django.views.generic import ListView, DetailView


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
  accessories = Accessory  #defind accessory with the model
  # Get the accessories the dog doesn't have...
  # First, create a list of the accessory ids that the dog DOES have
  id_list = dog.accessories.all().values_list('id')
  # Now we can query for accessories whose ids are not in the list using exclude
  accessories_dog_doesnt_have = Accessory.objects.exclude(id__in=id_list)

  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', 
    { 
      'dog': dog, 
      'feeding_form': feeding_form,
      # Add the accessories to be displayed
      'accessories': accessories_dog_doesnt_have 
    })


def add_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
    # don't save the form to the db until it has the dog_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = pk
    new_feeding.save()
  return redirect('detail', dog_id=pk)


def assoc_accessory(request, pk, accessory_pk):
  #Note that you can pass an accessory's id instead of the whole accessory object
  Dog.objects.get(id=pk).accessories.add(accessory_pk)
  return redirect('detail', dog_id=pk)




#class based 'VIEWS'
class DogCreate(CreateView):  #passed the (CreateView)
  #first thing to tell is 'model' 
  model = Dog
  #to tell what field to use. This one is '__all__' means to contain all of the Dog Model's attributes.
  fields = ['name', 'breed', 'description', 'age', 'gender', 'color', 'favorite_toy']
  # optional 1 way 
  #success_url = '/dogs/{dog_id}'


class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age', 'gender', 'color', 'favorite_toy']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'


# put this at the bottom of views.py
class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'type', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'