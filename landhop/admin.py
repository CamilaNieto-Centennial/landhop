from django.contrib import admin

from .models import User, Section, City

# Register your models here.
admin.site.register(User)
admin.site.register(Section)
admin.site.register(City)