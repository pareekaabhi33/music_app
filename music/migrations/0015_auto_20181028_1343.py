# Generated by Django 2.1.1 on 2018-10-28 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20181028_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='user_name',
            new_name='user',
        ),
    ]
