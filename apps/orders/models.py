from django.db import models
import datetime

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField('Status', max_length=30)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    modified_at = models.DateTimeField('Modified At', auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default='')
    fhalta = models.DateTimeField('Fecha de Alta', auto_now_add=True)
    fhocurre = models.DateTimeField('Fecha de Ocurrencia', blank=False, null=False)
    oCountry = models.CharField('Pais Origen', max_length=50, null=False, blank=False)
    oState = models.CharField('Localidad', max_length=50, null=False, blank=False)
    oAddress1 = models.CharField('Dirección', max_length=100, null=False, blank=False)
    oAddress2 = models.CharField('Dirección', max_length=100, blank=True, null=True)
    oZipCode = models.CharField('Zip Code', max_length=8, blank=False, null=False)
    dCountry = models.CharField('Pais Origen', max_length=50, null=False, blank=False)
    dState = models.CharField('Localidad', max_length=50, null=False, blank=False)
    dAddress1 = models.CharField('Dirección', max_length=100, null=False, blank=False)
    dAddress2 = models.CharField('Dirección', max_length=100, blank=True, null=True)
    dZipCode = models.CharField('Zip Code', max_length=8, blank=False, null=False)
