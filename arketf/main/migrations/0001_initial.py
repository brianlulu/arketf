# Generated by Django 2.1 on 2021-05-29 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ticker', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cusip', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('direction', models.CharField(max_length=5)),
                ('shares', models.BigIntegerField()),
                ('etf_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Stock')),
            ],
        ),
    ]
