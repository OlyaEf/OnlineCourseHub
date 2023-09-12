# Generated by Django 4.2.5 on 2023-09-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='video URL'),
        ),
    ]