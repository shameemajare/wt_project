# Generated by Django 2.2 on 2019-04-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_room_booking', '0007_auto_20190407_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfaction', models.CharField(max_length=20)),
                ('comments', models.TextField(default='null')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
