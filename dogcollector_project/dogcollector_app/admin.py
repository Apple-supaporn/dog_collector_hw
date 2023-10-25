from django.contrib import admin
from .models import Dog, Feeding, Accessory #import Dog and Feeding

# Register your models here. (for admin site)
admin.site.register(Dog) #add this to see dog data in admin site

# register the new 'Feeding' Model 
admin.site.register(Feeding)


# register Accessory model
admin.site.register(Accessory)