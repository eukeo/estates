# Generated by Django 4.0.2 on 2022-04-19 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_realtor_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='images',
            new_name='image',
        ),
    ]