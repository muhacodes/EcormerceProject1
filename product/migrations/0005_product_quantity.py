# Generated by Django 3.2 on 2022-08-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_moq'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
