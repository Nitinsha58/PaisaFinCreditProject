# Generated by Django 5.0.2 on 2024-03-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_addressdetails_id_alter_bankdetails_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetails',
            name='current_address_proof',
            field=models.ImageField(blank=True, null=True, upload_to='address_proofs/'),
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='permanent_address_proof',
            field=models.ImageField(blank=True, null=True, upload_to='address_proofs/'),
        ),
    ]
