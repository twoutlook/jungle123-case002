# Generated by Django 2.2.6 on 2019-10-27 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case002', '0004_data2_points'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='data2',
            unique_together={('name', 'date1', 'member')},
        ),
    ]
