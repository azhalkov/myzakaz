# klient/admin
from django.contrib import admin
# from klient.models import User
from .models import User
# from django.conf import settings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone")


# admin.site.register(User, UserAdmin)
