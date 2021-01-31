# Generated by Django 3.1.5 on 2021-01-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditCardChallenge', '0002_auto_20210131_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='brand',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='exp_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=models.CharField(max_length=16),
        ),
    ]