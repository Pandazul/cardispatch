from django.contrib import admin
from .models import Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('mat','make','model','only_year','created_at')


admin.site.register(Car, CarAdmin)

