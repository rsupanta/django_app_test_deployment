# Generated by Django 3.0.4 on 2020-03-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDB_app', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
