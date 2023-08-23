from django.contrib import admin
from .models import User, item, Category

# Register your models here.
admin.site.register(User)
admin.site.register(item)
admin.site.register(Category)
