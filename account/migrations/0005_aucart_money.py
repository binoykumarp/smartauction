# Generated by Django 4.2.4 on 2023-09-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_product_au_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='aucart',
            name='money',
            field=models.IntegerField(null=True),
        ),
    ]
