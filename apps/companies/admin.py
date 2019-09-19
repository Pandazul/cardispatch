from django.contrib import admin
from .models import Company, CompanyType
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'nif', 'company', 'companyType', 'created_at')


class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)