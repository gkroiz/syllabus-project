# Generated by Django 3.2.8 on 2021-10-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_file', models.FileField(upload_to='syllabi/')),
                ('title', models.CharField(max_length=8)),
                ('instructor_name', models.TextField()),
                ('instructor_email', models.CharField(max_length=41)),
                ('ta_name', models.TextField()),
                ('ta_email', models.CharField(max_length=41)),
                ('course_site', models.TextField()),
                ('instructor_phone', models.CharField(max_length=14)),
                ('office_hours', models.TextField()),
                ('course_time', models.TextField()),
                ('course_description', models.TextField()),
                ('course_objectives', models.TextField()),
                ('prereqs', models.TextField()),
                ('textbook', models.TextField()),
                ('instruct_methods', models.TextField()),
                ('attendance_rule', models.TextField()),
                ('class_preparation', models.TextField()),
                ('course_requirements', models.TextField()),
                ('grade_breakdown', models.TextField()),
                ('quizzes', models.TextField()),
                ('exams', models.TextField()),
                ('prog_assignments', models.TextField()),
                ('participation', models.TextField()),
                ('hands_on', models.TextField()),
                ('assignments', models.TextField()),
                ('homework', models.TextField()),
                ('late_policy', models.TextField()),
                ('makeup_policy', models.TextField()),
            ],
        ),
    ]
