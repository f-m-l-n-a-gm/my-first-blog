# Generated by Django 2.0.6 on 2019-04-27 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authour',
            new_name='author',
        ),
    ]
