from django.db import models

# Create your models here.
CONDITION_CHOICE = (('new', 'NEW'),
                    ('used', 'USED'))


class Car(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    mat = models.CharField('License Plate', max_length=10, blank=False, null=False)
    make = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    year = models.DateField(blank=False, null=False)
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICE, default='used')
    color = models.CharField(max_length=20, blank=False, null=False)
    odometer = models.IntegerField(null=False, blank=False)
    observations = models.TextField(max_length=300, null=True)
    cartype = models.CharField(max_length=30, blank=False, null=False)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    @property
    def only_year(self):
        return self.year.strftime('%Y')

    def __str__(self):
        return self.mat