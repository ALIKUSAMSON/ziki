from django import forms

IMAGE_LOCATION = (
		('Gallery', 'Gallery'),
		('Advertisement', 'Advertisement'),
				)
Music_location = (
		("Audio","Audio"),
		("Video","Video"),
	)

class UploadMusicForm(forms.Form):
	selection = forms.CharField(label='Select Music Type', widget=forms.Select(choices=Music_location))
	artist_name = forms.CharField(label='Artist Name', max_length=50)
	album_name = forms.CharField(label='Album Name', max_length=50)
	song_title = forms.CharField(label='Song Title', max_length=50)
	file_name = forms.FileField()


class UploadImageForm(forms.Form):
	selection = forms.CharField(label = 'Select category', max_length=255, widget=forms.Select(choices=IMAGE_LOCATION))
	#title = forms.CharField(label = 'Image title' ,max_length=50)
	image_name = forms.ImageField()


class NewsForm(forms.Form):
	story_title = forms.CharField(label='Story Title', max_length=50)
	story_image = forms.FileField()
	body = forms.CharField(required=True,widget=forms.Textarea)
