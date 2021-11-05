# Generated by Django 3.2.8 on 2021-10-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='office_hours',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='office_phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='hours',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='+1 (000) 000-0000', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='None', max_length=200),
        ),
    ]