from django.contrib import admin
from .models import VideoModel, AudioModel, NewsModel, GalleryModel, AddsModel
# Register your models here.
admin.site.register(AudioModel)
admin.site.register(VideoModel)
admin.site.register(NewsModel)
admin.site.register(GalleryModel)
admin.site.register(AddsModel)

