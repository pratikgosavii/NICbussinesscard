# Generated by Django 4.1.5 on 2024-05-07 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nicbussinesscard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='whatsapp',
        ),
    ]
