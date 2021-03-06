# Generated by Django 3.1 on 2020-09-07 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200907_1200"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_offers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
