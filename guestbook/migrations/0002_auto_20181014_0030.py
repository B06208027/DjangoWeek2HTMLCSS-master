# Generated by Django 2.1.1 on 2018-10-13 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textmessage',
            old_name='message',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='textmessage',
            old_name='talker',
            new_name='name',
        ),
    ]
