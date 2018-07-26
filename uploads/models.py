from django.db import models
from accounts.models import Account

# Create your models here.

class AudioModel(models.Model):
	#user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	artist_name = models.CharField(max_length=50)
	album_name = models.CharField(max_length=50, null=True)
	song_title = models.CharField(max_length=50)
	file_name = models.FileField(upload_to = 'audios_files/%Y/%m/%d')


class VideoModel(models.Model):
	#user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	artist_name = models.CharField(max_length=50)
	album_name = models.CharField(max_length=50, null=True)
	song_title = models.CharField(max_length=50)
	file_name = models.FileField(upload_to='video_files/%Y/%m/%d')


class NewsModel(models.Model):
	#user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	story_title = models.CharField(max_length = 50)
	story_image = models.ImageField(upload_to = 'picture_files/%Y/%m/%d', blank = True, null=True)
	body = models.TextField(default='Type text')
	
class GalleryModel(models.Model):
	#user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	#title = models.CharField(max_length=50)
	image_name = models.ImageField(upload_to = 'gallery_files/%Y/%m/%d',blank=True)

class AddsModel(models.Model):
	#user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	#title = models.CharField(max_length=50)
	image_name = models.ImageField(upload_to = 'adds_picture_files/%Y/%m/%d',blank=True)
