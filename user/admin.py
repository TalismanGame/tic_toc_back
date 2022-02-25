from django.contrib import admin
from .models import MyUser
# Register your models here.

# user class and @admin.register for better UI in admin
admin.site.register(MyUser)
