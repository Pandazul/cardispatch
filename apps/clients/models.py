from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    lastname = models.CharField('LastName', max_length=80, blank=False, null=False)
    telephone = models.CharField('Telephone', max_length=12, blank=False, null=False)
    iddni = models.CharField('DNI', max_length=12, blank=False, null=False)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']

    def __str__(self):
        return self.name
