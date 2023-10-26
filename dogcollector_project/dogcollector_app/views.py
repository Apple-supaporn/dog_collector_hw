# IMPORT NECESSARY MODULES
from django.shortcuts import render, redirect #add redirect to redirect after create new feeding
from .models import Dog, Accessory, Photo #don't forget to import data from database
from .forms import FeedingForm # Import the FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView #add import to CreateView, UpdateView and DeleteView
from django.views.generic import ListView, DetailView

#IMPORT FOR PHOTO AWS
import uuid
import boto3
#ADD THIS IMPORT TO ACCESS THE .ENV (THOSE SECRET KEYS)
import os

##----^----IMPORT ABOVE----^----##

# dogs = [
#   {'name': 'Mello', 'breed': 'husky', 'description': 'beautiful fur and playful husky', 'age': 3},
#   {'name': 'Blu', 'breed': 'husky and corgi mix', 'description': 'full energy and need lots of love', 'age': 4},
#   {'name': 'Oli', 'breed': 'golden retriver', 'description': 'friendly and only need pat', 'age': 5},
#   {'name': 'Luigi', 'breed': 'terrier and dachshund mix', 'description': 'lap dog and food looker', 'age': 15 },
#   {'name': 'Pak gard', 'breed': 'Bangkaew', 'description': 'playful and smiley', 'age': 10},
# ]



### DEFINE VIEWS HERE ###


# DEFINE THE HOME VIEW
def home(request):
    return render(request, 'dogs/home.html')


# DEFINE THE ABOUT VIEW
#Define another route with a path of about/. The path's trailing slash instead of a leading slash is the Django way and is critical to follow.
def about(request):
    return render(request, 'dogs/about.html')


# DEFINE THE DOG INDEX VIEW
def dogs_index(request):
  dogs = Dog.objects.all() #import from database
  return render(request, 'dogs/index.html', {'dogs' : dogs})


# DEFINE THE DOG DETAIL VIEW
def dogs_detail(request, dog_id): #The dogs_detail function is using the get method to obtain the dog object by its id.
  dog = Dog.objects.get(id=dog_id) #dog id match with ID 
  accessories = Accessory  #defind accessory with the model
  # Get the accessories the dog doesn't have...
  # First, create a list of the accessory ids that the dog DOES have
  id_list = dog.accessories.all().values_list('id')
  # Now we can query for accessories whose ids are not in the list using exclude
  accessories_dog_doesnt_have = Accessory.objects.exclude(id__in=id_list)

  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()

  return render(request, 'dogs/detail.html', 
    # include the dog and feeding_form in the context
    { 
      'dog': dog, 
      'feeding_form': feeding_form,
      # Add the accessories to be displayed
      'accessories': accessories_dog_doesnt_have 
    })


# DEFINE THE ADD FEEDING VIEW
def add_feeding(request, pk):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # check if the form is 'clean' with proper data and confirm all data returns to the server
  if form.is_valid():
    # don't save the form to the db until it has the dog_id assigned
    # it saves the data from the FeedingForm, BUT doesn't save it to the database when we use commit=False
    new_feeding = form.save(commit=False)
    # this is Feeding model, so we can still access dog_id column with our form
    new_feeding.dog_id = pk
    #puts the date, meal, and dog_id into our db
    new_feeding.save()
  return redirect('detail', dog_id=pk)


# DEFINE THE ASSOCIATION OF AN ACCESSORY WITH A DOG VIEW
def assoc_accessory(request, pk, accessory_pk):
  #Note that you can pass an accessory's id instead of the whole accessory object
  Dog.objects.get(id=pk).accessories.add(accessory_pk)
  return redirect('detail', dog_id=pk)


# DEFINE THE DELETION OF AN ACCESSORY FROM A DOG VIEW
# Delete accessory just in each dog <----ADD THIS TO DELETE ONLY ACCESSORY IN DOG
def assoc_delete(request, pk, accessory_pk):
  Dog.objects.get(id=pk).accessories.remove(accessory_pk)
  return redirect('detail', dog_id=pk)


# DEFINE THE ADD PHOTO VIEW
def add_photo(request, dog_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    # make variable to use sdk to talk with aws
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    print(f'this is the key {key}')
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      # build the full url string
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      # we can assign to dog_id or dog (if you have a dog object)
      Photo.objects.create(url=url, dog_id=dog_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
    return redirect('detail', dog_id=dog_id)


# DEFINE CLASS-BASED VIEWS (CBVs) FOR DOGS
class DogCreate(CreateView):  #passed the (CreateView)
  #first thing to tell is 'model' 
  model = Dog
  #to tell what field to use. This one is '__all__' means to contain all of the Dog Model's attributes.
  fields = ['name', 'breed', 'description', 'age', 'gender', 'color', 'favorite_toy']
  # optional 1 way 
  #success_url = '/dogs/{dog_id}'


class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age', 'gender', 'color', 'favorite_toy'] # Let's disallow the renaming of a dog by excluding the name field!


class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'


# DEFINE CLASS-BASED VIEWS (CBVs) FOR ACCESSORIES
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