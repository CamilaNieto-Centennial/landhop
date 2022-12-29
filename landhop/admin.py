from django.contrib import admin

from .models import User, Section, City, Sight

# Register your models here.
admin.site.register(User)
admin.site.register(Section)
admin.site.register(City)
admin.site.register(Sight)