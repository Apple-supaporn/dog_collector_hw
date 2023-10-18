from django.contrib import admin
from .models import Dog #import it

# Register your models here. (for admin site)
admin.site.register(Dog) #add this to see dog data in admin site

