# Generated by Django 5.0.4 on 2024-04-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]