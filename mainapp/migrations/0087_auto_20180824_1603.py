# Generated by Django 2.1 on 2018-08-24 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0086_merge_20180824_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privaterescuecamp',
            name='city',
        ),
        migrations.RemoveField(
            model_name='privaterescuecamp',
            name='is_inside_kerala',
        ),
        migrations.RemoveField(
            model_name='privaterescuecamp',
            name='lsg_type',
        ),
    ]
