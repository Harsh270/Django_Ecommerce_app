# Generated by Django 3.2 on 2021-07-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Company',
            field=models.CharField(default='', max_length=50),
        ),
    ]
