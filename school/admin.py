from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RealTimeImage

admin.site.register(RealTimeImage)

from django.contrib import admin
from .models import Interested

# Register the Interest model to make it manageable in the admin panel
admin.site.register(Interested)

from .models import Trainers
admin.site.register(Trainers)
