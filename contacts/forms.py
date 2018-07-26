from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(required=True,max_length=100,help_text='50 characters max')
	email = forms.EmailField(required=True)
	comment = forms.CharField(required=True,widget=forms.Textarea)