# Generated by Django 3.2.8 on 2021-11-14 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabi',
            name='class_id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='syllabi',
            name='semester_held',
            field=models.CharField(max_length=6),
        ),
    ]
