#IMPORT NECESSARY MODULES
from django.db import models
from django.urls import reverse # Import the reverse function


# DEFINE A TUPLE FOR MEAL TYPES
# MEAL is all capitals letter, do not change | A tuple of 2-tuples
# The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


# DEFINE A MODEL FOR ACCESSORIES
# Order is doesn't matter | This is Many-to-many relationships
class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})


# Each Model is defined as a Python class that inherits from 'django.db.models.Model.'
# An ERD Entity maps to a 'Model' in Django, which maps to a 'table' in the database.


# DEFINE THE MAIN DOG MODEL | Note: don't forget to migreate when update model/schema #
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=100, blank=True)
    # Add the M:M relationship
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name

    # Add this method for handle redirecting for update and create
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id}) #point to 'detail page'


# DEFINE THE FEEDING MODEL (ONE-TO-MANY) | MODELS & MODELFORMS
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS, # Choices from the MEALS tuple
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
        )

    # syntax / column made for FK = (Model)_id, in the db the column is call dog_id 
    # Create a ForeignKey to Dog model | dog_id
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


    def __str__(self):
        # syntax for getting our meal visuals get_(Model)_display()
        return f"{self.get_meal_display()} on {self.date}"

    # reorder our dates so the newest date is first (DESC) the default is (ASC)
    class Meta:
        # the default for ASC is just 'date' but we put a '-' in front of the field to reverse the order (DESC)
        ordering = ['-date']


# DEFINE THE PHOTO MODEL (ONE-TO-MANY)
class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dog_id: {self.dog_id} @{self.url}"