# Generated by Django 5.1.2 on 2024-10-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0002_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
