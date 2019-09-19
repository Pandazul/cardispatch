from django.contrib import admin
from .models import CarTrackers


# Register your models here.
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('id','car_id','lat','long','created_at')


admin.site.register(CarTrackers, TrackerAdmin)
