# Generated by Django 2.2.6 on 2020-05-14 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='total_words',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
