# Generated by Django 2.2 on 2019-04-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_room_booking', '0006_rooms_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
