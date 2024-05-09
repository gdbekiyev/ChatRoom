# Generated by Django 4.2.5 on 2024-05-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatRoomApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=55),
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='UsersChat',
        ),
    ]