# Generated by Django 4.2.5 on 2023-10-07 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0002_category_product_catetory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catetory',
            new_name='category',
        ),
    ]
