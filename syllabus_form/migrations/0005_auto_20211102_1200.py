# Generated by Django 3.2.5 on 2021-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_form', '0004_courseform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='CourseForm',
        ),
    ]