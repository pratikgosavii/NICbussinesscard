# Generated by Django 4.1.5 on 2024-05-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicbussinesscard', '0005_client_random_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='random_key',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]