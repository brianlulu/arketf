# Generated by Django 2.1 on 2021-06-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
    ]