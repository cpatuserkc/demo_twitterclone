# Generated by Django 3.2.9 on 2021-11-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tweetlike',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
