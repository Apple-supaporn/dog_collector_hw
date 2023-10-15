from django.shortcuts import render


dogs = [
  {'name': 'Mello', 'breed': 'husky', 'description': 'beautiful fur and playful husky', 'age': 3},
  {'name': 'Blu', 'breed': 'husky and corgi mix', 'description': 'full energy and need lots of love', 'age': 4},
  {'name': 'Oli', 'breed': 'golden retriver', 'description': 'friendly and only need pat', 'age': 5},
  {'name': 'Luigi', 'breed': 'terrier and dachshund mix', 'description': 'lap dog and food looker', 'age': 15 },
  {'name': 'Pak gard', 'breed': 'Bangkaew', 'description': 'playful and smiley', 'age': 10},
]


# Create your views here.
# these are function
def home(request):
    return render(request, 'dogs/home.html')

def about(request):
    return render(request, 'dogs/about.html')


def dogs_index(request):
  return render(request, 'dogs/index.html', {'dogs' : dogs})