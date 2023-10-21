from django.db import models
from django.urls import reverse # Import the reverse function


#MEAL is all capitals letter, do not change
# A tuple of 2-tuples
# The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)



# Each Model is defined as a Python class that inherits from 'django.db.models.Model.'
# An ERD Entity maps to a 'Model' in Django, which maps to a 'table' in the database.


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=100, blank=True)


# add this // don't forget to migreate when update model/shegema
    def __str__(self):
        return self.name

# Add this method for handle redirecting for update and create
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
        )

    # Create a dog_id FK
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
