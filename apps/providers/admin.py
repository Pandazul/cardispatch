from django.contrib import admin
from .models import Provider, PersonType, PaymentType, ProviderFinance
# Register your models here.

class ProviderFinanceAdmin(admin.ModelAdmin):
    list_display = ('provider_id', 'paymentType', 'bank', 'created_at')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'nif', 'name', 'personType', 'created_at')

class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(Provider, ProviderAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(ProviderFinance, ProviderFinanceAdmin)
