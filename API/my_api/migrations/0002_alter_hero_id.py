# Generated by Django 3.2 on 2021-06-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
