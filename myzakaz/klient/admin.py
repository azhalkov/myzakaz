# klient/admin


from klient.models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone")


# admin.site.register(User, UserAdmin)
