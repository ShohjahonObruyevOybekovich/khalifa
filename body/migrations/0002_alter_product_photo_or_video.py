# Generated by Django 5.0.4 on 2024-04-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_or_video',
            field=models.FileField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]