# Generated by Django 4.1.2 on 2022-10-26 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="Kind",
            new_name="kind",
        ),
    ]
