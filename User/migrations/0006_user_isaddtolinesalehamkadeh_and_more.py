# Generated by Django 4.0 on 2023-10-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_user_isforward'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isAddToLineSaleHamkadeh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isListeningSaleHamkadeh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isMonitoringSaleHamkadeh',
            field=models.BooleanField(default=False),
        ),
    ]
