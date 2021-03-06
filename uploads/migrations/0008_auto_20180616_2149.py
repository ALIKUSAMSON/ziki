# Generated by Django 2.0.4 on 2018-06-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20180614_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addsmodel',
            name='image_name',
            field=models.ImageField(blank=True, upload_to='adds_picture_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='audiomodel',
            name='file_name',
            field=models.FileField(upload_to='audios_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gallerymodel',
            name='image_name',
            field=models.ImageField(blank=True, upload_to='gallery_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='story_image',
            field=models.ImageField(blank=True, null=True, upload_to='picture_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='file_name',
            field=models.FileField(upload_to='video_files/%Y/%m/%d'),
        ),
    ]
