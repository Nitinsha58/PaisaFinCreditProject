# Generated by Django 4.2.6 on 2024-03-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_addressdetails_user_alter_bankdetails_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressdetails',
            name='first_time',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='first_time',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='first_time',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
