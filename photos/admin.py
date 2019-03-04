from django.contrib import admin
from .models import Location,Category,Image

# image details
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)