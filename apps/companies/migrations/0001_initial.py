# Generated by Django 2.2.5 on 2019-09-21 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nif', models.CharField(max_length=9, unique=True, verbose_name='NIPC')),
                ('company', models.CharField(max_length=60, verbose_name='Company Name')),
                ('telephone1', models.CharField(max_length=12, verbose_name='Telephone')),
                ('telephone2', models.CharField(max_length=12, verbose_name='Mobile Phone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('zipCode', models.CharField(max_length=8, verbose_name='Zip Code')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('companyType', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='companies.CompanyType')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['id'],
            },
        ),
    ]
