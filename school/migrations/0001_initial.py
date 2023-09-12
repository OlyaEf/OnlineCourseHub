# Generated by Django 4.2.5 on 2023-09-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='course')),
                ('preview', models.ImageField(upload_to='', verbose_name='preview')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='lesson')),
                ('preview', models.ImageField(upload_to='', verbose_name='preview')),
                ('description', models.TextField(verbose_name='description')),
                ('video_url', models.URLField(verbose_name='video URL')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]