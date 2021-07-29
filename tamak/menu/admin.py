from django.contrib import admin
from .models import PrimaryMeal, GeneralMeal, Wine

admin.site.register(PrimaryMeal)
admin.site.register(GeneralMeal)
admin.site.register(Wine)