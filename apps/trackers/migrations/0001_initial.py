# Generated by Django 2.2.5 on 2019-09-21 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarTrackers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('lat', models.CharField(max_length=20, null=True, verbose_name='Lat')),
                ('long', models.CharField(max_length=20, null=True, verbose_name='Long')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
            options={
                'verbose_name': 'Car Position',
                'verbose_name_plural': 'Car Positions',
                'ordering': ['id'],
            },
        ),
    ]
