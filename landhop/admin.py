from django.contrib import admin

from .models import User, Section

# Register your models here.
admin.site.register(User)
admin.site.register(Section)