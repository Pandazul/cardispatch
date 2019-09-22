from django.contrib import admin
from .models import CarTrackers, ProviderTrackers


# Register your models here.
class CarTrackerAdmin(admin.ModelAdmin):
    list_display = ('id','car_id','lat','long','created_at')


class TruckTrackerAdmin(admin.ModelAdmin):
     list_display = ('id','provider_truck_id','lat','long','created_at')


admin.site.register(CarTrackers, CarTrackerAdmin)
admin.site.register(ProviderTrackers, TruckTrackerAdmin)
