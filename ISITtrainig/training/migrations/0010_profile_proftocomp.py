# Generated by Django 4.0.2 on 2023-05-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_remove_profile_proftocomp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='proftocomp',
            field=models.ManyToManyField(through='training.ProfileToCompanies', to='training.Company'),
        ),
    ]