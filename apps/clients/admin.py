from django.contrib import admin
from.models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'lastname', 'iddni', 'telephone', 'created_at')


admin.site.register(Client, ClientAdmin)

