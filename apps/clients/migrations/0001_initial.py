# Generated by Django 2.2.5 on 2019-09-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('lastname', models.CharField(max_length=80, verbose_name='LastName')),
                ('telephone', models.CharField(max_length=12, verbose_name='Telephone')),
                ('iddni', models.IntegerField(max_length=12, verbose_name='DNI')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['id'],
            },
        ),
    ]