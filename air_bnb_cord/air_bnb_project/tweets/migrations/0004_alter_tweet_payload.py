# Generated by Django 4.1.4 on 2022-12-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0003_alter_like_twitter_alter_tweet_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="payload",
            field=models.CharField(max_length=180),
        ),
    ]