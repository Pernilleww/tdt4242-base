# Generated by Django 3.1 on 2020-09-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="stale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="offer",
            name="status",
            field=models.CharField(
                choices=[("a", "Accepted"), ("p", "Pending"), ("d", "Declined")],
                default="p",
                max_length=8,
            ),
        ),
        migrations.DeleteModel(
            name="OfferResponse",
        ),
    ]
