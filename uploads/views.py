from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadMusicForm, UploadImageForm, NewsForm
from .models import VideoModel, AudioModel, NewsModel, GalleryModel, AddsModel
from django.views.decorators.http import require_POST

from accounts.models import User


# Create your views here.

def upload_news_view(request):
	form = NewsForm()
	if request.method == "POST":
		form = NewsForm(request.POST, request.FILES)
		if form.is_valid():
			story_title = form.cleaned_data['story_title']
			story_image = request.FILES['story_image']
			body = form.cleaned_data['body']
			news = NewsModel(story_image = story_image, story_title=story_title, body=body)
			news.save()
			return redirect('dashbaord')
		else:
			return HttpResponse('Failed')
	else:
		return	render(request, 'uploads/uploads_news.html', {'form':form})

def upload_music_view(request):
	form = UploadMusicForm()
	if request.method == "POST":
		form = UploadMusicForm(request.POST, request.FILES)
		if form.is_valid():
			selection = form.cleaned_data['selection']
			if (selection == 'Audio'):
				artist_name = form.cleaned_data['artist_name']
				album_name = form.cleaned_data['album_name']
				song_title = form.cleaned_data['song_title']
				file_name = request.FILES['file_name']
				audio = AudioModel(artist_name=artist_name,album_name=album_name,song_title=song_title,file_name=file_name)
				audio.save()
				return redirect('dashbaord')
			elif (selection == 'Video'):
				artist_name = form.cleaned_data['artist_name']
				album_name = form.cleaned_data['album_name']
				song_title = form.cleaned_data['song_title']
				file_name = request.FILES['file_name']
				video = VideoModel(artist_name=artist_name,album_name=album_name,song_title=song_title,file_name=file_name)
				video.save()
				return redirect('dashbaord')
			else:
				return HttpResponse('Select a category')
		else:
			return HttpResponse('Failed')
	else:
		return	render(request, 'uploads/upload_music.html', {'form':form})

def upload_image_view(request):
	form = UploadImageForm()
	if request.method == "POST":
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			selection = form.cleaned_data['selection']
			if(selection == 'Gallery'):

				gall = GalleryModel(image_name = request.FILES['image_name'])
				gall.save()
				return redirect('dashbaord')
			elif(selection == 'Advertisement'):
				adds = AddsModel(image_name = request.FILES['image_name'])
				adds.save()
				return redirect('dashbaord')
			else:
				return HttpResponse("Unkown selected field")
			return redirect('dashbaord')
		else:
			print(form.errors)
			return HttpResponse('Failed')
	else:
		return	render(request, 'uploads/upload_image.html', {'form':form})



