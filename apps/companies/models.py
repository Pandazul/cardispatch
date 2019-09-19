from django.db import models


# Create your models here.
class CompanyType(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    nif = models.CharField('NIPC', max_length=9, blank=False, null=False, unique=True)
    company = models.CharField('Company Name', max_length=60, blank=False, null=False)
    telephone1 = models.CharField('Telephone', max_length=12, blank=False, null=False)
    telephone2 = models.CharField('Mobile Phone', max_length=12, blank=False, null=False)
    email = models.EmailField('Email', max_length=254, unique=True)
    address = models.CharField('Address', max_length=120, blank=False, null=False)
    zipCode = models.CharField('Zip Code', max_length=8, blank=False, null=False)
    companyType = models.ForeignKey(CompanyType, on_delete=models.PROTECT, default='')
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['id']

    def __str__(self):
        return self.company

