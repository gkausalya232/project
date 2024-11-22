from django.contrib import admin

# Register your models here.
from .models import FetalHealthData,UserImageModel,Profile

admin.site.register(FetalHealthData)
admin.site.register(UserImageModel)
admin.site.register(Profile)