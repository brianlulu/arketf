# Generated by Django 2.1 on 2021-06-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210621_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]