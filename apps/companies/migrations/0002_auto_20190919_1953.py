# Generated by Django 2.2.5 on 2019-09-19 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
