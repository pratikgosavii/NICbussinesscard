# Generated by Django 4.1.5 on 2024-05-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicbussinesscard', '0004_client_company_name_alter_client_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='random_key',
            field=models.CharField(default=1, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
