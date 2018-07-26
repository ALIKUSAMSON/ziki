from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from uploads.models import GalleryModel, AddsModel, NewsModel, VideoModel, AudioModel


# Create your views here.
def home(request):
	gallery = GalleryModel.objects.all()
	context = {'gallery':gallery}
	template = 'index.html'
	return render(request, template, context)

def audios_view(request):
	aud = AudioModel.objects.all()
	context = {'aud':aud}
	template = 'audios.html'
	return render(request, template, context)

def audio_view(request, id):
	auds = AudioModel.objects.get(id=id)
	context = {'auds':auds}
	template = 'audio.html'
	return render(request, template, context)

def news_view(request):
	context = locals()
	template = 'news.html'
	return render(request, template, context)

def videos_view(request):
	context = locals()
	template = 'videos.html'
	return render(request, template, context)

@login_required
def dashboard_view(request):
	context  = locals()
	template = 'dashbaord.html'
	return render(request, template, context)