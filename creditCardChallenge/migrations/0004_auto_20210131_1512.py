# Generated by Django 3.1.5 on 2021-01-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditCardChallenge', '0003_auto_20210131_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='brand',
            field=models.CharField(max_length=30),
        ),
    ]
