from django.contrib import admin
from .models import Dog, Feeding, Accessory, Photo

## REGISTER MODELS HERE (FOR ADMIN SITE) ##

# register Dog Model 
admin.site.register(Dog)

# register Feeding Model 
admin.site.register(Feeding)

# register Accessory model
admin.site.register(Accessory)

# register Photo model
admin.site.register(Photo)