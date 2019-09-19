from django.db import models


# Create your models here.
class CarTrackers(models.Model):
    id = models.AutoField('Id', primary_key=True, serialize=False)
    car_id = models.ForeignKey('cars.Car',on_delete=models.CASCADE, null=True)
    lat = models.CharField('Lat', max_length=20, null=True)
    long = models.CharField('Long', max_length=20, null=True)
    created_at = models.DateTimeField('Created At', auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Car Position'
        verbose_name_plural = 'Car Positions'
        ordering = ['id']
