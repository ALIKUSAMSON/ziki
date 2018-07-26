# Generated by Django 2.0.4 on 2018-06-10 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('selection', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('selection', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='MusicanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
                ('album_name', models.CharField(max_length=50)),
                ('song_title', models.CharField(max_length=50)),
                ('file_name', models.FileField(upload_to='')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=50)),
                ('story_image', models.ImageField(blank=True, upload_to='')),
                ('body', models.TextField(default='Type text')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
    ]
