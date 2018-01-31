from django.contrib import admin
from django.contrib import admin
from opacity.api.models import Location, UserData, Rating
# Register your models here.
admin.site.register(Location)
admin.site.register(Rating)
admin.site.register(UserData)

