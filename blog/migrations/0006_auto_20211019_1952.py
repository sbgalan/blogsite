# Generated by Django 2.2 on 2021-10-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
