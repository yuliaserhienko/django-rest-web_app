# Generated by Django 3.0.7 on 2020-06-13 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_shop_user_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='user_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL),
        ),
    ]
