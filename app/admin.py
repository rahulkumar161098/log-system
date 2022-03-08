from django.contrib import admin
from .models import UserReg

# Register your models here.


class UserView(admin.ModelAdmin):
    list_display=('name','email', 'password')
admin.site.register(UserReg, UserView)