# Generated by Django 4.0.2 on 2023-05-10 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], default=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
