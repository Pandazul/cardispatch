from django.db import models


# Create your models here.
class PersonType(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class PaymentType(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Provider(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    nif = models.CharField('NIPC', max_length=9, blank=False, null=False, unique=True)
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    telephone1 = models.CharField('Telephone', max_length=12, blank=False, null=False)
    telephone2 = models.CharField('Mobile Phone', max_length=12, blank=False, null=False)
    address = models.CharField('Dirección', max_length=120, blank=False, null=False)
    zipCode = models.CharField('Zip Code', max_length=8, blank=False, null=False)
    email = models.EmailField('Email', max_length=254, unique=True)
    personType = models.ForeignKey(PersonType, on_delete=models.PROTECT, default='')
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class ProviderFinance(models.Model):
    provider_id = models.OneToOneField(Provider, on_delete=models.CASCADE, primary_key=True)
    paymentType = models.ForeignKey(PaymentType, on_delete=models.PROTECT, default='')
    bank = models.CharField('Bank Name', max_length=80)
    iban = models.CharField('Iban', max_length=60)
    swift = models.CharField('Swift', max_length=10)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.bank
