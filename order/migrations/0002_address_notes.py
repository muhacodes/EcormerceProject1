# Generated by Django 3.2.9 on 2022-01-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]